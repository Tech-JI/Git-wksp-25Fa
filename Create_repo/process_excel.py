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


def process_excel_file(excel_path="group.xlsx", group_output="group.txt", individual_output="individual.txt"):
    """
    Process the Excel file according to specified rules.

    Args:
        excel_path: Path to the input Excel file
        group_output: Path to the output file for group entries
        individual_output: Path to the output file for individual entries
    """
    logger.info(f"Reading Excel file: {excel_path}")

    # Read the Excel file with error handling
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
    col_j = 'Q3. 邮箱 Email'  # Column J
    col_l = 'Q5. 请填写本项内容'  # Column L
    col_m = 'Q6. 请填写本项内容'  # Column M
    col_n = 'Q7. 请填写本项内容'  # Column N
    col_name = 'Q1. 姓名 Name'  # Name column for additional duplicate detection

    # Check if required columns exist
    required_cols = [col_j, col_l]
    missing_cols = [col for col in required_cols if col not in df.columns]
    optional_cols = [col_m, col_n]

    if missing_cols:
        logger.error(f"Required columns missing: {missing_cols}")
        return

    # Warn about missing optional columns
    missing_optional = [col for col in optional_cols if col not in df.columns]
    if missing_optional:
        logger.warning(f"Optional columns missing: {missing_optional}")

    # Open output files
    with open(group_output, 'w', encoding='utf-8') as group_file, \
         open(individual_output, 'w', encoding='utf-8') as individual_file:

        processed_rows = 0
        group_entries = 0
        individual_entries = 0

        for index, row in df.iterrows():
            try:
                # Get values from columns J, L, M, N
                j_value = row[col_j] if col_j in df.columns else None
                l_value = row[col_l] if col_l in df.columns else None
                m_value = row[col_m] if col_m in df.columns else None
                n_value = row[col_n] if col_n in df.columns else None

                # Check if l_value is not empty (not null and not empty string)
                if pd.notna(l_value) and str(l_value).strip() != "":
                    # Write J, L, M, N to group.txt separated by spaces, but remove duplicates
                    values_to_write = []
                    for val in [j_value, l_value, m_value, n_value]:
                        if pd.notna(val) and str(val).strip() != "":
                            values_to_write.append(str(val).strip())

                    if values_to_write:  # Only write if there are non-empty values
                        # Remove duplicates from the group
                        unique_values = remove_duplicates_from_group(values_to_write)

                        if unique_values:  # Only write if there are still values after deduplication
                            group_file.write(' '.join(unique_values) + '\n')
                            group_entries += 1
                            logger.info(f"Row {index}: Added to {group_output} - {unique_values}")
                else:
                    # Write J to individual.txt
                    if pd.notna(j_value) and str(j_value).strip() != "":
                        # Validate email before writing
                        email_str = str(j_value).strip()
                        if is_valid_email(email_str):
                            individual_file.write(email_str + '\n')
                            individual_entries += 1
                            logger.info(f"Row {index}: Added to {individual_output} - {email_str}")
                        else:
                            logger.warning(f"Row {index}: Skipped invalid email - {email_str}")

                processed_rows += 1

            except Exception as e:
                logger.error(f"Error processing row {index}: {e}")
                continue

    logger.info(f"Processing complete!")
    logger.info(f"Total rows processed: {processed_rows}")
    logger.info(f"Entries written to {group_output}: {group_entries}")
    logger.info(f"Entries written to {individual_output}: {individual_entries}")
    logger.info(f"Files created: {group_output}, {individual_output}")


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

    if not os.path.exists(excel_file):
        logger.error(f"{excel_file} does not exist in the current directory")
        return

    process_excel_file(excel_file, group_output, individual_output)


if __name__ == "__main__":
    main()