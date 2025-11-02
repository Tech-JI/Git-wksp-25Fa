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
header-includes: \newcommand{\faint}[1]{\textcolor{gray}{#1}}
---

# Contents

The what and why

Basic shell commands

Get ready for your first repository

Get your hands dirty

About branches

Beyond this workshop

# Contents

The what and why

\faint{Basic shell commands}

\faint{Get ready for your first repository}

\faint{Get your hands dirty}

\faint{About branches}

\faint{Beyond this workshop}

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

# Contents

\faint{The what and why}

Basic shell commands

\faint{Get ready for your first repository}

\faint{Get your hands dirty}

\faint{About branches}

\faint{Beyond this workshop}

# What is a shell

- A command dispatcher/process starter

- A more advanced and direct interface with the OS

- Gets you more productive

# Working with files and directories in a shell

- **Forward slashes** (i.e. "`/`") for separating directories

- One uniformed tree-like structure (non-Windows environment)

- Working directory

# Common directories

<!--prettier-ignore-->
| Description                  | Representation                                                  |
| ---------------------------- | ----------------------------------- |
| Home directory               | `~`                                                             |
| Root directory (non-Windows) | `/`                                                             |
| Drive directories (Windows)  | `/c/`, `/d/`, ... in Git Bash; `/mnt/c/`, `/mnt/d/`, ... in WSL |

`~` redirects to:

- `C:\Users\<username>` on Windows native
- `/home/<username>` on macOS/Linux

# Shell commands

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

# Practice

Exercise 1: Create a file structure like this:

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

# Contents

\faint{The what and why}

\faint{Basic shell commands}

Get ready for your first repository

\faint{Get your hands dirty}

\faint{About branches}

\faint{Beyond this workshop}

# Get ready for your first repository

Identify your Git environment:

| Installation type | Recommended Shell   |
| ----------------- | ------------------- |
| Windows native    | Powershell/Git Bash |
| WSL               | Bash/Zsh            |
| Linux native      | Bash/Zsh            |

NOTE: It's best suggested that you add which directory the `git` executable file is in to your `PATH` environment variable.

# Identify your environment

![Git Bash](git_bash.png)

# Identify your environment

![Obsolete Powershell](powershell.png)

TODO: switch to a modern version of Powershell

# Identify your environment

![Manjaro](manjaro_kitty.png)

TODO: provide screenshots for WSL

# Git configuration

- `git config --global user.name <NAME>`

- `git config --global user.email <EMAIL>`

- Enclose `NAME` in double quotes if it contains spaces

- For [FOCS Git](https://focs.ji.sjtu.edu.cn/git/), `EMAIL` must be your SJTU email

# Contents

\faint{The what and why}

\faint{Basic shell commands}

\faint{Get ready for your first repository}

Get your hands dirty

\faint{About branches}

\faint{Beyond this workshop}

# The starting point - repository

A repository is:

- a central storage location for a project's files and their complete revision history

- stored in a `.git` folder in your project root directory

# How to create a repository

**Create a repository = Create a standardized `.git` folder**

- `git init` in local existing project directory

- `git clone <url>` to copy a remote (i.e. stored on a server) directory with all its files and histories (i.e. its `.git` folder) to your local computer

# The three zones

![The three zones](zones.jpg){ width=300px }

- Working directory: "Ready", status quo of files on your computer

- Staging area: "Set", files to be committed

- Repository: "Go", snapshot permanently stored and **immutable**

# The four states

![Four states of a file](states.jpg){ width=300px }

- Untracked: files Git has yet to know about

- Unmodified: files that haven't been modified since last snapshot (can also be called committed from a different POV)

- Modified: files that have been modified but not staged

- Staged: files that are modified and marked to be included in the next snapshot

# How to move files between these zones and states

| Command                       | Description                                            |
| ----------------------------- | ------------------------------------------------------ |
| `git add <file>`              | Add file to staging area                               |
| `git restore --staged <file>` | Remove file from staging area                          |
| `git commit -m <message>`     | Commit (i.e. Take a snapshot of) files in staging area |

# Contents

\faint{The what and why}

\faint{Basic shell commands}

\faint{Get ready for your first repository}

\faint{Get your hands dirty}

About branches

\faint{Beyond this workshop}

# What are branches?

Branches are:

- Different paths the codebase will grow on

- Isolated histories that don't interfere with each other

- Used to separate different feature changes and on-going fixes

The branches can be visualized by a tree-like structure.

Type `git log --graph --no-color --pretty=oneline --abbrev-commit` to see a graph of this tree-like structure.

# And why are branches important?

- Cleaner working tree without disturbance from other changes

- Safer environment in case something devastating happens

- Parallel development to maximize productivity

# Working with branches

<!--prettier-ignore-->
|Command|Description|
|----|-------|
|`git branch <name>`|Create a branch with `name`|
|`git checkout <name>`|Switch current branch to `name`|
|`git merge <from-branch>`|Merge commits from other branches to the current one|
|`git rebase <from-branch>`|Rebase current branch on another one|

# Merge vs. Rebase

Branches can be merged or rebased together to combine changes from multiple sources.

**Merge**

```
      E---F---G (fix)              E---F---G (fix)
     /                  ==>       /         \
A---B---C---D (master)       A---B---C---D---H (master)
```

`H` is a new commit containing all files' latest snapshots from `E`, `F` and `G`.

**Rebase**

```
      E---F---G (fix)              E---F---G (fix)
     /                  ==>       /
A---B---C---D (master)       A---B---E'---F'---G'---C---D (master)
```

`E'` has the same snapshot as `E`, `F'` has the same snapshot as `F`, ...

# What's this 'fast-forward' thing?

**Merge** (without fast-forward)

```
      C---D---E (fix)             C---D---E (fix)
     /                 ==>       /         \
A---B (master)              A---B-----------F (master)
```

`F` is a new commit.

**Merge** (with fast-forward)

```
      C---D---E (fix)
     /                 ==>
A---B (master)              A---B---C---D---E (master & fix)
```

No new commit is created.

# Beyond this workshop

- Google

- [Pro Git](https://git-scm.com/book/en/v2)

- AI assistant
