# **Git Commands Reference Table**

|Command  |Description               |
|-----------------------------|----------------------------------------------------------------------------|
|`git config`|Set your user name and email for commits|
|`git init`|Initialize the current directory as a new Git repository|
|`git clone <url>`|Copy a remote repository to your local device|
|`git pull`|Fetch from and integrate with the remote branch (fetch+merge)|
|`git fetch`|Fetch (download) objects and refs from the remote repository|
|`git add <file>`|Add file changes to the staging area|
|`git restore --staged <file>`|Remove file from staging area|
|`git push`|Push the local submission to the remote repository|
|`git remote -v`|Check the detailed information(urls) of the remote repositories|
|`git status`|Check the status of files in the working directory and staging area|
|`git diff`|Compare the differences among the working directory, staging area, and version repository|
|`git diff --staged`|Compare the differences in the staging area|
|`git log`|View submission history|
|`git branch`|List, create or delete branches|
|`git checkout <branch-name>`|Switch to the specified branch and update the files in the working directory|
|`git switch <branch>`|Switch to existing branch (newer, safer)|
|`git merge <from-branch>`|Merge commits from other branches to the currentone|
|`git rebase <from-branch>`|Rebase current branch on another one|
|`git rm <file>`|Remove files from working directory and staging area|
|`git mv <old> <new>`|Move or rename a file|
|`git clean -fd`|Remove the untracked files and directories|
|`git stash`|Stage the modifications that haven't been submitted yet|
|`git stash pop`|Restore the temporarily stored mdifications|
|`git tag <tagname>`|Create a new tag for the current commit|

## **Undo Commands**

|Command|Description|
|-----------------------------|-----------------------------------------------------------------|
|`git restore <file>`|Revert file to last committed state|
|`git restore --staged <file>`|Unstage files, keep modifications|
|`git checkout --<file>`|Discard the modifications in the working directory|
|`git commit --amend`|Fix last commit message|
|`git reset --soft HEAD~1`|Undo commit but keep changes|
|`git reset HEAD~1`|Undo commit and cancel staging|
|`git reset --hard HEAD~1`|Completely remove last commit|
|`git revert <commit-bash>`|Create new commit that reverses changes|
|`git stash`|Stage the modifications that haven't been submitted yet|