#!/usr/bin/env python3
"""
Script to add students to specific Gitea repositories based on email addresses in group.txt.

This script leverages the Joint Teapot framework to:
1. Read email addresses from group.txt file
2. Add students as collaborators to GitWksp_teamXX repositories based on line number
3. Use the underlying Gitea API for repository management
"""

from joint_teapot.teapot import Teapot
from typing import List


def add_student_to_repo_by_email(teapot: Teapot, student_email: str, org_name: str, repo_name: str) -> bool:
    """
    Add a student to a specific repository using their email address.

    Args:
        teapot: The initialized Teapot instance
        student_email: The student's email address (typically in format username@sjtu.edu.cn)
        org_name: The organization name
        repo_name: The name of the repository to add the student to

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Extract username from email (assumes SJTU email format)
        if not student_email.endswith("@sjtu.edu.cn"):
            print(f"Warning: Email {student_email} is not an SJTU email address")
            return False

        username = student_email.split("@")[0]

        # Add student to the repository as a collaborator
        teapot.gitea.repository_api.repo_add_collaborator(
            org_name,
            repo_name,
            username
        )
        print(f"Successfully added {username} to {repo_name}")
        return True

    except Exception as e:
        print(f"Error adding {student_email} to {repo_name}: {e}")
        return False


def add_students_from_group_file(teapot: Teapot, group_file: str, org_name: str):
    """
    Add students to repositories by reading email addresses from group.txt file.
    Each line creates a team repository named GitWksp_teamXX where XX is the line number.

    Args:
        teapot: The initialized Teapot instance
        group_file: Path to the group.txt file containing space-separated email addresses
        org_name: The organization name where repositories are located
    """
    try:
        with open(group_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        print(f"Processing {len(lines)} groups from {group_file}")

        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Create repository name with group ID (line number)
            repo_name = f"GitWksp_team{i+1:02d}"  # GitWksp_team01, GitWksp_team02, etc.

            # Split the line by spaces to get email addresses
            emails = line.split()
            print(f"Group {i+1}: Processing emails - {emails} -> {repo_name}")

            for email in emails:
                email = email.strip()
                if email:  # Make sure email is not empty
                    success = add_student_to_repo_by_email(teapot, email, org_name, repo_name)
                    if success:
                        print(f"  Successfully added {email} to {repo_name}")
                    else:
                        print(f"  Failed to add {email} to {repo_name}")

        print(f"Completed processing {group_file}")

    except FileNotFoundError:
        print(f"Error: {group_file} not found")
    except Exception as e:
        print(f"Error processing {group_file}: {e}")


def main():
    """
    Main function to add students from group.txt to GitWksp_teamXX repositories.
    """
    print("Initializing Joint Teapot...")
    teapot = Teapot()

    ORGANIZATION_NAME = ""  # Leave blank now

    print(f"\n--- Adding students from group.txt to GitWksp_teamXX repositories ---")
    print(f"Using organization: {ORGANIZATION_NAME or '(default from config)'}")

    # Add students from group.txt to the GitWksp_teamXX repositories
    add_students_from_group_file(teapot, "group.txt", ORGANIZATION_NAME or teapot.gitea.org_name)

    print("\nScript completed!")


if __name__ == "__main__":
    main()
