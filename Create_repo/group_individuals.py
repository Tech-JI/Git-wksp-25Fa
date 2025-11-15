#!/usr/bin/env python3
"""
Script to sequentially group people from individual.txt into groups of 3,
then append these new groups to the existing group.txt file.
"""

import os
from typing import List


def group_individuals_to_file(individual_file: str = "individual.txt",
                             group_file: str = "group.txt",
                             group_size: int = 3):
    """
    Sequentially group people from individual.txt into groups of specified size,
    then append these new groups to the existing group.txt file.

    Args:
        individual_file: Path to the individual.txt file
        group_file: Path to the group.txt file
        group_size: Size of each group (default 3)
    """
    print(f"Reading individual accounts from {individual_file}")

    # Read individual.txt to get all accounts
    if not os.path.exists(individual_file):
        print(f"Error: {individual_file} does not exist")
        return

    accounts = []
    with open(individual_file, 'r', encoding='utf-8') as f:
        for line in f:
            account = line.strip()
            if account:
                accounts.append(account)

    print(f"Found {len(accounts)} accounts in individual.txt")

    if len(accounts) < group_size:
        print(f"Warning: Not enough accounts to form a group of {group_size}. Need at least {group_size}, but only have {len(accounts)}")
        # If not enough accounts for a group, just keep them in individual.txt
        print("No new groups created due to insufficient accounts.")
        return

    # Don't shuffle the accounts, just group them sequentially
    print("Grouping accounts sequentially (first 3, next 3, etc.)")

    # Create groups of specified size sequentially
    new_groups = []
    for i in range(0, len(accounts), group_size):
        group = accounts[i:i + group_size]
        if len(group) == group_size:  # Only create full groups
            new_groups.append(group)

    # Handle remaining accounts that don't form a complete group
    remaining_accounts = len(accounts) % group_size
    remaining = []
    if remaining_accounts > 0 and remaining_accounts < group_size:
        remaining = accounts[-remaining_accounts:]
        print(f"Found {remaining_accounts} accounts remaining that don't form a complete group of {group_size}: {remaining}")

    print(f"Created {len(new_groups)} new groups of {group_size} people each")

    # Read existing groups from group.txt
    existing_groups = []
    if os.path.exists(group_file):
        with open(group_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_groups.append(line)

    print(f"Found {len(existing_groups)} existing groups in {group_file}")

    # Prepare all groups (existing + new)
    all_groups_lines = existing_groups[:]

    # Add new groups to the list
    for group in new_groups:
        group_line = ' '.join(group)
        all_groups_lines.append(group_line)

    # Handle remaining accounts according to the new rules:
    # - If 1 left: add to the last group (making it a group of 4)
    # - If 2 left: create a group of 2
    if remaining:
        if remaining_accounts == 1 and all_groups_lines:
            # Add the single account to the last group
            last_group = all_groups_lines[-1].split()
            last_group.append(remaining[0])
            all_groups_lines[-1] = ' '.join(last_group)
            print(f"Added 1 remaining account '{remaining[0]}' to the last group")
        elif remaining_accounts == 2:
            # Create a new group with the 2 remaining accounts
            new_group_line = ' '.join(remaining)
            all_groups_lines.append(new_group_line)
            print(f"Created a new group with 2 remaining accounts: {new_group_line}")

    # Write all groups back to group.txt
    with open(group_file, 'w', encoding='utf-8') as f:
        for i, group_line in enumerate(all_groups_lines):
            f.write(group_line + '\n')

    print(f"Updated {group_file} with a total of {len(all_groups_lines)} groups")

    # Create a new individual.txt with any remaining ungrouped accounts (should be none based on new rules)
    new_individual_accounts = []
    # With the new logic, there should be no remaining accounts to write to individual.txt

    # Write updated individual.txt (should be empty or with original non-group members)
    with open(individual_file, 'w', encoding='utf-8') as f:
        for account in new_individual_accounts:
            f.write(account + '\n')

    print(f"Updated {individual_file} with {len(new_individual_accounts)} remaining accounts")

    print("Grouping completed successfully!")


def main():
    """
    Main function to execute the grouping.
    """
    import sys
    
    # Check command line arguments
    if len(sys.argv) >= 2:
        individual_file = sys.argv[1]
    else:
        individual_file = "individual.txt"
    
    if len(sys.argv) >= 3:
        group_file = sys.argv[2]
    else:
        group_file = "group.txt"
    
    if len(sys.argv) >= 4:
        try:
            group_size = int(sys.argv[3])
        except ValueError:
            print("Group size must be an integer. Using default value of 3.")
            group_size = 3
    else:
        group_size = 3
    
    group_individuals_to_file(individual_file, group_file, group_size)


if __name__ == "__main__":
    main()