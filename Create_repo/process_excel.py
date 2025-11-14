#!/usr/bin/env python3
"""
Script to process group.xlsx file according to specifications:
- If column L is not empty, write emails from columns J, L, M, N (space-separated) to group.txt
- If column L is empty, write email from column J to individual.txt
- Includes duplicate removal functionality
"""

import pandas as pd
import os
import re
import logging
from typing import List, Set


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def is_valid_email(email: str) -> bool:
    """Check if the provided string is a valid email format."""
    if not email or not isinstance(email, str):
        return False
    # Basic email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email.strip()) is not None


def remove_duplicates_from_group(entries: List[str]) -> List[str]:
    """
    Remove duplicate entries from a group list.
    This includes both duplicate emails and duplicate names if they exist in the list.
    """
    if not entries:
        return []

    seen: Set[str] = set()
    unique_entries: List[str] = []

    for entry in entries:
        entry_str = str(entry).strip()
        if not entry_str:
            continue

        # For email validation, check if this looks like an email
        if is_valid_email(entry_str):
            # Normalize email by converting to lowercase for comparison
            normalized = entry_str.lower()
            if normalized not in seen:
                seen.add(normalized)
                unique_entries.append(entry_str)
        else:
            # For non-email entries (like names), just compare as-is but normalized
            normalized = entry_str.lower()
            if normalized not in seen:
                seen.add(normalized)
                unique_entries.append(entry_str)

    return unique_entries


def process_excel_file(excel_path="group.xlsx", group_output="group.txt", individual_output="individual.txt",
                      enrollment_path="enroll.xlsx"):
    """
    Process the Excel file according to specified rules using account names instead of emails.
    After initial processing, compares with enrollment form and adds missing participants to individual.txt.

    Args:
        excel_path: Path to the input Excel file
        group_output: Path to the output file for group entries
        individual_output: Path to the output file for individual entries
        enrollment_path: Path to the enrollment Excel file to find missing participants
    """
    logger.info(f"Reading Excel file: {excel_path}")

    # Read the main Excel file with error handling
    try:
        df = pd.read_excel(excel_path)
    except FileNotFoundError:
        logger.error(f"File '{excel_path}' not found.")
        return
    except Exception as e:
        logger.error(f"Error reading Excel file '{excel_path}': {e}")
        return

    # Print column names to verify the structure
    logger.info(f"Columns in the Excel file: {list(df.columns)}")

    # Map column names to the expected columns
    col_j_email = 'Q3. 邮箱 Email'  # Column J (for getting account from email)
    col_j_account = '账号'  # Column for account names
    col_l = 'Q5. 请填写本项内容'  # Column L
    col_m = 'Q6. 请填写本项内容'  # Column M
    col_n = 'Q7. 请填写本项内容'  # Column N
    col_name = 'Q1. 姓名 Name'  # Name column for name-account mapping

    # Check if required columns exist
    required_cols = [col_j_email, col_l]
    missing_cols = [col for col in required_cols if col not in df.columns]
    optional_cols = [col_m, col_n]

    if missing_cols:
        logger.error(f"Required columns missing: {missing_cols}")
        return

    # Warn about missing optional columns
    missing_optional = [col for col in optional_cols if col not in df.columns]
    if missing_optional:
        logger.warning(f"Optional columns missing: {missing_optional}")

    # Keep track of all participants (using account names instead of emails)
    processed_accounts = set()
    # Dictionary to map names to accounts for checking against enrollment
    name_to_account = {}

    # Process the main Excel file
    with open(group_output, 'w', encoding='utf-8') as group_file, \
         open(individual_output, 'w', encoding='utf-8') as individual_file:

        processed_rows = 0
        group_entries = 0
        individual_entries = 0

        for index, row in df.iterrows():
            try:
                # Get values from columns
                j_email_value = row[col_j_email] if col_j_email in df.columns else None
                j_account_value = row[col_j_account] if col_j_account in df.columns else None
                l_value = row[col_l] if col_l in df.columns else None
                m_value = row[col_m] if col_m in df.columns else None
                n_value = row[col_n] if col_n in df.columns else None
                name_value = row[col_name] if col_name in df.columns else None

                # Determine account name to use
                # Prefer the account column if available, otherwise extract from email
                account_to_use = None
                if pd.notna(j_account_value) and str(j_account_value).strip():
                    account_to_use = str(j_account_value).strip()
                elif pd.notna(j_email_value) and is_valid_email(str(j_email_value).strip()):
                    # Extract account from email (part before @)
                    email_str = str(j_email_value).strip()
                    account_to_use = email_str.split('@')[0]

                # Store name-account mapping for later comparison
                if pd.notna(name_value) and str(name_value).strip() and account_to_use:
                    name_str = str(name_value).strip()
                    name_to_account[name_str] = account_to_use

                # Check if l_value is not empty (not null and not empty string)
                if pd.notna(l_value) and str(l_value).strip() != "":
                    # Process group: J + L, M, N (but convert to accounts where possible)
                    values_to_write = []

                    # Add account for J (primary person)
                    if account_to_use:
                        values_to_write.append(account_to_use)

                    # For L, M, N, try to get accounts (these might be emails too)
                    for col_val in [l_value, m_value, n_value]:
                        if pd.notna(col_val) and str(col_val).strip() != "":
                            val_str = str(col_val).strip()
                            # Check if this is an email to extract account from
                            if is_valid_email(val_str):
                                account_from_email = val_str.split('@')[0]
                                values_to_write.append(account_from_email)
                            else:
                                # If not an email, treat as account directly (or try to extract from email format)
                                # Check if it looks like an email that was stored as text
                                if '@' in val_str:
                                    account_from_email = val_str.split('@')[0]
                                    values_to_write.append(account_from_email)
                                else:
                                    values_to_write.append(val_str)

                    if values_to_write:  # Only write if there are non-empty values
                        # Remove duplicates from the group
                        unique_values = remove_duplicates_from_group(values_to_write)

                        if unique_values:  # Only write if there are still values after deduplication
                            group_file.write(' '.join(unique_values) + '\n')
                            group_entries += 1
                            logger.info(f"Row {index}: Added to {group_output} - {unique_values}")
                            # Add all accounts from this group to the set
                            for account in unique_values:
                                processed_accounts.add(account.lower())
                else:
                    # Write account for J to individual.txt
                    if account_to_use:
                        individual_file.write(account_to_use + '\n')
                        individual_entries += 1
                        logger.info(f"Row {index}: Added to {individual_output} - {account_to_use}")
                        # Add to the set of processed accounts
                        processed_accounts.add(account_to_use.lower())

                processed_rows += 1

            except Exception as e:
                logger.error(f"Error processing row {index}: {e}")
                continue

    # Now, process enrollment file to find missing participants and add them to individual.txt
    if enrollment_path and os.path.exists(enrollment_path):
        logger.info(f"Processing enrollment file: {enrollment_path} to find missing participants")
        try:
            enroll_df = pd.read_excel(enrollment_path)
            logger.info(f"Columns in enrollment file: {list(enroll_df.columns)}")

            # Expected name column in enrollment file
            enroll_name_col = 'Q1. 姓名'  # This is the name column in enroll.xlsx

            if enroll_name_col not in enroll_df.columns:
                logger.warning(f"Expected column '{enroll_name_col}' not found in enrollment file. Skipping enrollment check.")
            else:
                # Get all names from the enrollment file
                enrolled_names = set()
                for _, row in enroll_df.iterrows():
                    name = row[enroll_name_col]
                    if pd.notna(name) and str(name).strip():
                        enrolled_names.add(str(name).strip())

                # The enrollment processing is handled in the second phase function
                # This phase only processes the main group.xlsx file
                pass

        except Exception as e:
            logger.error(f"Error processing enrollment file '{enrollment_path}': {e}")

    logger.info(f"First phase processing complete!")
    logger.info(f"Total rows processed: {processed_rows}")
    logger.info(f"Entries written to {group_output}: {group_entries}")
    logger.info(f"Entries written to {individual_output}: {individual_entries}")
    logger.info(f"Files created: {group_output}, {individual_output}")

    # Second phase: Compare with enrollment and add missing participants to individual.txt
    if enrollment_path and os.path.exists(enrollment_path):
        logger.info("Starting second phase: checking enrollment for missing participants")
        add_missing_enrollment_participants(enrollment_path, group_output, individual_output)


def add_missing_enrollment_participants(enrollment_path, group_output, individual_output):
    """
    Adds people from enrollment that are not in the output files to individual.txt using account names.

    Args:
        enrollment_path: Path to the enrollment Excel file
        group_output: Path to group output file
        individual_output: Path to individual output file
    """
    logger.info("Reading enrollment file to find missing participants")

    # Read enrollment file to get names and accounts
    try:
        enroll_df = pd.read_excel(enrollment_path)
        enroll_name_col = 'Q1. 姓名'  # This is the name column in enroll.xlsx
        enroll_account_col = '账号'  # This is the account column in enroll.xlsx

        if enroll_name_col not in enroll_df.columns:
            logger.warning(f"Expected column '{enroll_name_col}' not found in enrollment file.")
            return

        # Get all names and accounts from enrollment
        enrollment_name_to_account = {}
        for _, row in enroll_df.iterrows():
            name = row[enroll_name_col]
            account = row[enroll_account_col] if enroll_account_col in enroll_df.columns else None

            if pd.notna(name) and str(name).strip():
                name_str = str(name).strip()
                account_str = None
                if pd.notna(account) and str(account).strip():
                    account_str = str(account).strip()
                enrollment_name_to_account[name_str] = account_str

        logger.info(f"Found {len(enrollment_name_to_account)} entries in enrollment")

        # Get enrollment accounts that are not None
        enrollment_accounts = {name: account for name, account in enrollment_name_to_account.items()
                              if account is not None}
        logger.info(f"Found {len(enrollment_accounts)} participants in enrollment with account information")

    except Exception as e:
        logger.error(f"Error reading enrollment file: {e}")
        return

    # Check against the existing output files to see what accounts are already included
    try:
        existing_accounts = set()

        # Read group.txt
        if os.path.exists(group_output):
            with open(group_output, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        # Each line may contain multiple accounts separated by spaces
                        accounts = line.split()
                        for account in accounts:
                            if account.strip():
                                existing_accounts.add(account.strip().lower())

        # Read individual.txt
        if os.path.exists(individual_output):
            with open(individual_output, 'r', encoding='utf-8') as f:
                for line in f:
                    account = line.strip()
                    if account:
                        existing_accounts.add(account.lower())

        logger.info(f"Found {len(existing_accounts)} unique accounts already in output files")

        # Find accounts from enrollment that are not in the output files
        enrollment_only_accounts = []
        all_enrollment_accounts = set(enrollment_accounts.values())

        for name, account in enrollment_accounts.items():
            if account.lower() not in existing_accounts:
                enrollment_only_accounts.append(account)

        if enrollment_only_accounts:
            logger.info(f"Found {len(enrollment_only_accounts)} accounts from enrollment that are missing from output files")

            # Append these missing accounts to individual.txt
            with open(individual_output, 'a', encoding='utf-8') as f:
                for account in enrollment_only_accounts:
                    f.write(account + '\n')
                    logger.info(f"Added missing account to {individual_output}: {account}")
        else:
            logger.info("No missing participants with accounts found from enrollment")

    except Exception as e:
        logger.error(f"Error in second phase processing: {e}")


def main():
    """
    Main function to execute the Excel processing.
    """
    import sys

    # Check command line arguments
    if len(sys.argv) >= 2:
        excel_file = sys.argv[1]
    else:
        excel_file = "group.xlsx"

    # Allow custom output filenames as optional parameters
    group_output = sys.argv[2] if len(sys.argv) >= 3 else "group.txt"
    individual_output = sys.argv[3] if len(sys.argv) >= 4 else "individual.txt"
    enrollment_file = sys.argv[4] if len(sys.argv) >= 5 else "enroll.xlsx"

    if not os.path.exists(excel_file):
        logger.error(f"{excel_file} does not exist in the current directory")
        return

    process_excel_file(excel_file, group_output, individual_output, enrollment_file)


if __name__ == "__main__":
    main()