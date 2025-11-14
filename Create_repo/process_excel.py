#!/usr/bin/env python3
"""
Script to process group.xlsx file according to specifications:
- If column L is not empty, write emails from columns J, L, M, N (space-separated) to group.txt
- If column L is empty, write email from column J to individual.txt
"""

import pandas as pd
import os


def process_excel_file(excel_path="group.xlsx", group_output="group.txt", individual_output="individual.txt"):
    """
    Process the Excel file according to specified rules.

    Args:
        excel_path: Path to the input Excel file
        group_output: Path to the output file for group entries
        individual_output: Path to the output file for individual entries
    """
    print(f"Reading Excel file: {excel_path}")

    # Read the Excel file
    df = pd.read_excel(excel_path)

    # Print column names to verify the structure
    print(f"Columns in the Excel file: {list(df.columns)}")

    # Based on the file structure we found:
    # Q3. 邮箱 (column 9) corresponds to column J
    # Q5. 请填写本项内容 (column 11) corresponds to column L
    # Q6. 请填写本项内容 (column 12) corresponds to column M
    # Q7. 请填写本项内容 (column 13) corresponds to column N

    # Map column names to the expected columns
    col_j = 'Q3. 邮箱'  # Column J
    col_l = 'Q5. 请填写本项内容'  # Column L
    col_m = 'Q6. 请填写本项内容'  # Column M
    col_n = 'Q7. 请填写本项内容'  # Column N

    # Check if required columns exist
    missing_cols = []
    for col in [col_j, col_l]:
        if col not in df.columns:
            missing_cols.append(col)

    if missing_cols:
        print(f"Error: Required columns missing: {missing_cols}")
        return

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
                    # Write J, L, M, N to group.txt separated by spaces
                    values_to_write = []
                    for val in [j_value, l_value, m_value, n_value]:
                        if pd.notna(val) and str(val).strip() != "":
                            values_to_write.append(str(val).strip())

                    if values_to_write:  # Only write if there are non-empty values
                        group_file.write(' '.join(values_to_write) + '\n')
                        group_entries += 1
                        print(f"Row {index}: Added to {group_output} - {values_to_write}")
                else:
                    # Write J to individual.txt
                    if pd.notna(j_value) and str(j_value).strip() != "":
                        individual_file.write(str(j_value).strip() + '\n')
                        individual_entries += 1
                        print(f"Row {index}: Added to {individual_output} - {j_value}")

                processed_rows += 1

            except Exception as e:
                print(f"Error processing row {index}: {e}")
                continue

    print(f"\nProcessing complete!")
    print(f"Total rows processed: {processed_rows}")
    print(f"Entries written to {group_output}: {group_entries}")
    print(f"Entries written to {individual_output}: {individual_entries}")
    print(f"Files created: {group_output}, {individual_output}")


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
        print(f"Error: {excel_file} does not exist in the current directory")
        return

    process_excel_file(excel_file, group_output, individual_output)


if __name__ == "__main__":
    main()