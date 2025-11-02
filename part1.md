---
title:
  - Git Workshop
author:
  - Tech GC
theme:
  - Copenhagen
date:
  - November 2025
colorlinks: true
linkcolor: .
urlcolor: blue
aspectratio: 169
header-includes: |
  \setbeamertemplate{headline}{}
---

\tableofcontents

# The what and why

- Git is a free and open source distributed version control system

- Famous software developed with Git
  - [Linux](https://github.com/torvalds/linux)
  - [Vim](https://github.com/vim/vim)
  - [Visual Studio Code](https://github.com/microsoft/vscode)

- We learn Git because it's:
  - Required in ENGL1010J and ENGL1510J
  - Useful for version control
  - Useful for project collaboration

# Basic shell

## What is a shell

- A command dispatcher/process starter

- A more advanced and direct interface with the OS

- Gets you more productive

## Working with files and directories in a shell

- **Forward slashes** (i.e. "`/`") for separating directories

- One uniformed tree-like structure (non-Windows environment)

- Working directory

## Common directories

<!--prettier-ignore-->
| Description                  | Representation                                                  |
| ---------------------------- | ----------------------------------- |
| Home directory               | `~`                                                             |
| Root directory (non-Windows) | `/`                                                             |
| Drive directories (Windows)  | `/c/`, `/d/`, ... in Git Bash; `/mnt/c/`, `/mnt/d/`, ... in WSL |

`~` redirects to:

- `C:\Users\<username>` on Windows native
- `/home/<username>` on macOS/Linux

## Shell commands

\small

<!--prettier-ignore-->
| Command                     | Action                                                             |
| --------------------------- | --------------------------------------- |
| `cd [directory]`            | Change working directory                                           |
| `pwd`                       | Print working directory                                            |
| `ls [options] [directory]`  | List directory contents                                            |
| `touch <file>`              | Create a file (if it doesn't exist)                                |
| `mkdir <directory>`         | Make (i.e. "Create") a directory                                   |
| `mv <source> <destination>` | Move files/directories from `source` to `destination` |
| `cp <source> <destination>` | Copy files/directories from `source` to `destination` |
| `rm <file>`                 | Remove (i.e. Permanently delete) a file                            |

\normalsize

Further description can be found by executing `man <command>` in non-Windows shell or search online for **manpages**.

## Practice

Create a file structure like this:

```
~
|- git-wksp
   |
   |- exercise-1
   |  |
   |  |- question-1
   |
   |- exercise-2
```

## Practice

**Step-by-step instructions:**

1. Navigate to your home directory: `cd ~`

2. Create the main folder: `mkdir git-wksp`

3. Enter the folder: `cd git-wksp`

4. Create exercise-1 directory: `mkdir exercise-1`

5. Create exercise-2 directory: `mkdir exercise-2`

6. Enter exercise-1: `cd exercise-1`

7. Create question-1: `touch question-1`

8. Verify: `ls -la`

## Advanced file management tips

1. Create multiple directories at once: `mkdir -p project/{src,docs,tests}`

2. Copy a file: `cp question-1 ../exercise-2/new-question-1`

3. Move a file: `mv ../exercise-2/new-question-1 .`

4. Remove a file: `rm question-1`

5. List all files recursively: `find . -type f`

# Get ready for your first repository

## Identify your coding environment

| Environment type | Recommended Shell   |
| ---------------- | ------------------- |
| Linux native/WSL | Bash/Zsh            |
| Windows native   | Powershell/Git Bash |
| macOS            | Zsh                 |

## Installing Git

**Linux native/WSL**

Install using your package manager:

- Debian-based (Debian, Ubuntu, ...): `sudo apt-get install git`

- CentOS/RHEL/Fedora: `sudo yum install git` or `sudo dnf install git`

- Arch-based (Arch, Manjaro ...): `sudo pacman -S git`

...

## Installing Git

**Windows native**

1. Download Git from [git-scm.com](https://git-scm.com/download/win) or [TsingHua mirror](https://mirrors.tuna.tsinghua.edu.cn/github-release/git-for-windows/git/LatestRelease/)

2. Run the installer with default settings

NOTE: It's best suggested that you add the `git` executable to your `PATH` environment variable.

3. Choose your preferred text editor (Vim, VS Code, etc.)

4. Choose terminal emulator (Git Bash is recommended)

5. Complete the installation

**macOS**

Install Xcode command line tools: `xcode-select --install`

Or install using Homebrew: `brew install git`

## Git configuration

- `git config --global user.name <NAME>`

- `git config --global user.email <EMAIL>`

- Enclose `NAME` in double quotes if it contains spaces

- For [FOCS Git](https://focs.ji.sjtu.edu.cn/git/), `EMAIL` must be your SJTU email

# Get your hands dirty

## The starting point - repository

A repository is:

- a central storage location for a project's files and their complete revision history

- stored in a `.git` folder in your project root directory

## How to create a repository

**Create a repository = Create a standardized `.git` folder**

- `git init` in local existing project directory

- `git clone <url>` to copy a remote (i.e. stored on a server) directory with all its files and histories (i.e. its `.git` folder) to your local computer

## The three zones

\center

```{.mermaid caption="The three zones" format=pdf width=300}
sequenceDiagram
    participant wd as Working Directory
    participant sa as Staging Area
    participant repo as Repository
    repo->>wd: Checkout the project
    wd->>sa: Stage Fixes
    sa->>repo: Commit
```

- Working directory: "Ready", status quo of files on your computer

- Staging area: "Set", files to be committed

- Repository: "Go", snapshot permanently stored and **immutable**

## The four states

\center

```{.mermaid caption="Four states of a file" format=pdf width=300}
sequenceDiagram
    participant ut as Untracked
    participant um as Unmodified
    participant m as Modified
    participant s as Staged
    ut->>s: Add the file
    um->>m: Edit the file
    m->>s: Stage the file
    um->>ut: Remove the file
    s->>um: Commit
```

- Untracked: files Git has yet to know about

- Unmodified: files that haven't been modified since last snapshot (can also be called committed from a different POV)

- Modified: files that have been modified but not staged

- Staged: files that are modified and marked to be included in the next snapshot

## How to move files between these zones and states

\small

<!--prettier-ignore-->
| Command                       | Description                                            |
| ----------------------------- | ----------------------------------------------- |
| `git add <file>`              | Add file to staging area                               |
| `git restore --staged <file>` | Remove file from staging area                          |
| `git commit -m <message>`     | Commit (i.e. Take a snapshot of) files in staging area |

\normalsize

## Additional Git Commands

\small

<!--prettier-ignore-->
| Command                  | Description                                           |
| ------------------------ | ---------------------------------------------- |
| `git status`             | Show current status of files in working directory     |
| `git log`                | Show commit history                                   |
| `git diff`               | Show changes between commits, commit and working tree |
| `git diff --staged`      | Show changes between staging area and last commit     |
| `git checkout -- <file>` | Discard changes in working directory                  |
| `git reset HEAD <file>`  | Unstage files from staging area                       |

\normalsize

# About branches

## What are branches?

Branches are:

- Different paths the codebase will grow on

- Isolated histories that don't interfere with each other

- Used to separate different feature changes and on-going fixes

The branches can be visualized by a tree-like structure.

Type `git log --graph --no-color --pretty=oneline --abbrev-commit` to see a graph of this tree-like structure.

## And why are branches important?

- Cleaner working tree without disturbance from other changes

- Safer environment in case something devastating happens

- Parallel development to maximize productivity

## Working with branches

<!--prettier-ignore-->
|Command|Description|
|----|-------|
|`git branch <name>`|Create a branch with `name`|
|`git checkout <name>`|Switch current branch to `name`|
|`git merge <from-branch>`|Merge commits from other branches to the current one|
|`git rebase <from-branch>`|Rebase current branch on another one|

## Practice

Create a branch structure like this:

```
          G---H---I (fix)
         /
        E---F (feature-a)
       /
      /       J---K (feature-b)
     /       /
A---B---C---D---E (master)
```

## Merge vs. Rebase

Branches can be merged or rebased together to combine changes from multiple sources.

**Merge**

```
      E---F---G (fix)              E---F---G (fix)
     /                  ==>       /         \
A---B---C---D (master)       A---B---C---D---H (master)
```

- `H` is a new commit containing all files' latest snapshots from `E`, `F` and `G`.
- Keep complete historical records.
- Non destructive operation.

**Rebase**

```
      E---F---G (fix)              E---F---G (fix)
     /                  ==>       /
A---B---C---D (master)       A---B---E'---F'---G'---C---D (master)
```

- `E'` has the same snapshot as `E`, `F'` has the same snapshot as `F`, ...
- Create linear history and Rewrite submission history.

## What's this 'fast-forward' thing?

**Merge** (without fast-forward)

```
      C---D---E (fix)             C---D---E (fix)
     /                 ==>       /         \
A---B (master)              A---B-----------F (master)
```

- `F` is a new commit.

**Merge** (with fast-forward)

```
      C---D---E (fix)
     /                 ==>
A---B (master)              A---B---C---D---E (master & fix)
```

- No new commit is created.

## Practice

Extend the previous branch structure to this:

```
         E---F---G---H---I (feature-a & fix)
        /                 \
       /                   \
      /       J---K (feature-b)
     /       /               \
A---B---C---D---E---J'---K'---M (master)
```

# Remote repositories

## What are remote repositories?

- Versions of your project hosted on the web (GitHub, GitLab, Bitbucket, self-hosted, etc.)

- Can serve as your code backup

- Multiple developers can collaborate on the same project

## Common remote operations

\small

<!--prettier-ignore-->
| Command                       | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| `git remote add <name> <url>` | Add a remote repository                            |
| `git remote -v`               | List remote repositories                           |
| `git push <remote> <branch>`  | Upload local commits to a remote repository        |
| `git pull <remote> <branch>`  | Download and merge from a remote repository        |
| `git fetch <remote>`          | Download objects and refs from a remote repository |

\normalsize

### Popular Git hosting platforms

- **GitHub**: Most popular platform, owned by Microsoft
- **GitLab**: Offers both cloud and self-hosted solutions
- **Bitbucket**: Popular among enterprise users, owned by Atlassian
- **FOCS Git**: The internal SJTU Git platform mentioned in this workshop

# Solving Conflicts in Git

## What is a merge conflict?

A merge conflict occurs when Git cannot automatically reconcile differences between two commits during a merge operation. This typically happens when the same lines in the same file have been modified in different branches that are being merged.

## How to identify a conflict

When a merge conflict occurs, Git will:

1. Mark the conflicted files as "unmerged"

2. Insert conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) directly into the affected files

3. Report which files have conflicts

Check the status with: `git status`

## Understanding conflict markers

When you open a conflicted file, you'll see sections like this:

```
<<<<<<< HEAD
This is the content from the current branch
=======
This is the content from the branch being merged
>>>>>>> branch-name
```

The content between `<<<<<<< HEAD` and `=======` is from your current branch.

The content between `=======` and `>>>>>>> branch-name` is from the branch you're merging.

## Steps to resolve a conflict

1. Identify conflicted files using `git status`

2. Open each conflicted file and look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

3. Edit the file to resolve the conflict by:

- Deciding which changes to keep (from either branch or a combination)

- Removing the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

- Making any additional changes needed to properly integrate the code

4. Add the resolved files to the staging area:

- Use `git add <filename>` or `git add .` to stage all resolved files

5. Complete the merge:

- `git commit -m "Resolve merge conflict in <filename>"`

## Practical example

Let's say we have a conflict in `README.md`:

```
<<<<<<< HEAD
# My Project
This is the main branch content
=======
# My Project
This is the feature branch content
>>>>>>> feature-branch
```

After deciding which content to keep (or combining both), the resolved file should look like:

```
# My Project
This is the content I want to keep after resolving the conflict
```

## Tips for conflict resolution

- Use a text editor with syntax highlighting to better see conflict markers

- Some editors have special features for visualizing and resolving conflicts

- Communicate with team members when you're unsure which changes to keep

- Test your code after resolving conflicts to ensure everything still works

- Use `git diff` to review what you've changed before committing

- Consider using `git merge-tool` for complex conflicts

## Common tools for resolving conflicts

- **VS Code**: Has built-in conflict resolution interface

- **Vim**: Use `:Gdiff` with vim-fugitive plugin

- **Dedicated tools**: `meld`, `p4merge`, `bc` (Beyond Compare)

# Other common Git issues and troubleshooting

## Common issues

**1. Forgot to stage files before committing:**

- Error: `nothing to commit, working tree clean`
- Solution: Use `git add <filename>` to stage files, then commit again

**2. Made a mistake in the commit message:**

- Solution: `git commit --amend -m "corrected message"` to update the last commit message

**3. Forgot to add a file to the last commit:**

- Solution: Add the file with `git add <filename>`, then use `git commit --amend` to include it in the previous commit

## Common issues

**4. Accidentally modified the wrong branch:**

- Solution: Use `git stash` to save changes, switch to correct branch, then `git stash pop` to apply changes there

**5. Conflicts during merge:**

- Solution: Manually edit conflicted files to resolve conflicts (look for `<<<<<<<`, `=======`, `>>>>>>>` markers), then add and commit the resolved files

**6. How to undo things:**

- To unstage a file: `git restore --staged <file>`
- To discard changes in working directory: `git restore <file>`
- To go back to a previous commit: `git reset --hard <commit-hash>` (WARNING: This is destructive!)

## Undoing changes in Git

Git provides several ways to undo changes depending on where you are in the workflow:

### Undoing changes in the Working Directory

`git restore <file>` (or `git checkout -- <file>` in older Git versions)

### Unstaging a file

`git restore --staged <file>` (or `git reset HEAD <file>` in older Git versions)

### Undoing commits (locally only!)

**Soft Reset**: Moves the branch pointer back but keeps changes in staging area

::: columns
:::: {.column width=8%}
::::
:::: {.column width=20%}

Before:

```
A---B---C
        ^
      HEAD
```

::::
:::: {.column width=60%}

After `git reset --soft HEAD~1`:

```
A---B---C
    ^
  HEAD (C's changes in staging area)
```

::::
:::: {.column width=12%}
::::
:::

## Undoing Changes in Git

### Undoing commits (locally only!)

**Mixed Reset**: Moves the branch pointer back and keeps changes in working directory

::: columns
:::: {.column width=8%}
::::
:::: {.column width=20%}

Before:

```
A---B---C
        ^
      HEAD
```

::::
:::: {.column width=70%}

After `git reset --mixed HEAD~1`:

```
A---B---C
    ^
  HEAD (C's changes in working directory)
```

::::
:::: {.column width=2%}
::::
:::

\quad

**Hard Reset**: Moves the branch pointer back and discards all changes

::: columns
:::: {.column width=8%}
::::
:::: {.column width=20%}

Before:

```
A---B---C
        ^
      HEAD
```

::::
:::: {.column width=50%}

After `git reset --hard HEAD~1`:

```
A---B
    ^
  HEAD (C's changes discarded)
```

::::
:::: {.column width=22%}
::::
:::

# Beyond this workshop

- Google

- [Pro Git](https://git-scm.com/book/en/v2)

- AI assistant
