# Git Workshop: ASCII Art Collaboration

## Workshop Overview
Collaborate with your team to create an ASCII art mascot while learning Git version control through 5 progressive exercises.

---

## Exercise 0: Foundation & Setup
**Duration:** 15 minutes
**Objective:** Set up Git configuration and practice basic shell commands
**Key Concept:** ssh-key, git config, shell commands

### Instructions:
1. Configure Git globally with your name and email:
   - `git config --global user.name "Your Full Name"`
   - `git config --global user.email "your.email@domain.com"`

2. Practice basic shell commands:
   - `pwd` - Print working directory
   - `ls` - List directory contents
   - `mkdir ascii-project` - Create project directory
   - `cd ascii-project` - Change to project directory
   - `touch README.md` - Create README file
   - `ls -l` - List files with details
   - `cp README.md README_backup.md` - Copy file
   - `mv README_backup.md docs/` - Move file (first create docs dir with `mkdir docs`)
   - `rm [filename]` - Remove file

3. Generate SSH key pair for secure repository access:
   - You can refer to <https://git-scm.com/install>
   - `ssh-keygen -t ed25519 -C "your_email@domain.com"`
   - Add to SSH agent: `eval "$(ssh-agent -s)"` then `ssh-add ~/.ssh/id_ed25519`
   - Copy public key: `cat ~/.ssh/id_ed25519.pub`
   - Add to your Gitea -> Settings -> SSH/GPG Keys -> Manage SSH keys -> Add key

---

## Exercise 1: Local Repository Basics
**Duration:** 10 minutes
**Objective:** Clone an existing repository
**Key Concepts:** clone

### Instructions:
1. Clone the team repository: `git clone [repository-url]`
2. Navigate to the repository: `cd [repository-name]`
3. Edit your ASCII canvas
4. Add ASCII canvas to the repository: `git add ascii_canvas.txt`
5. Make initial commit: `git commit -m "Initial canvas setup"`

---

## Exercise 2: Branching

**Duration:** 20 minutes
**Objective:** Create and switch between feature branches, make local commits
**Key Concepts:** switch branch

### Instructions:

1. Each designer works on their assigned section in their branch
2. Add and commit changes locally without pushing: `git add [file]` then `git commit -m "[descriptive message]"`
3. Practice undoing changes by resetting to staging area: `git reset --soft HEAD~1`

---

## Exercise 3: Collaboration & Pushing Changes

**Duration:** 15 minutes
**Objective:** Switch branches, commit changes, and push to remote
**Key Concepts:** change & commit, push

### Instructions:
1. Switch to your assigned role branch: `git switch [your-branch-name]`
2. Make changes to your assigned ASCII section
3. Add and commit your changes locally: `git add [files]` then `git commit -m "[descriptive message]"`
4. Push your committed changes to the remote repository: `git push origin [branch-name]`
5. Each team member pushes their role branch
6. Practice pulling updates: `git pull origin [branch-name]`

---

## Exercise 4: Merging & Conflict Resolution
**Duration:** 20 minutes
**Objective:** Combine team changes and resolve conflicts
**Key Concepts:** merge, rebase, resolve conflict

### Instructions:
1. Switch to main branch: `git switch main`
2. Update main with latest changes: `git pull origin main`
3. Merge feature branches into main: `git merge [feature-branch]`
4. Handle conflicts that arise when multiple designers edit similar sections
5. Resolve conflicts manually by selecting best design elements
6. Complete integration and push final result: `git push origin main`

---

## Team Roles Reference
- **Head Designer:** Focus on head/mouth/eyes area
- **Body Designer:** Focus on torso area
- **Leg Designer:** Focus on legs/feet area
- **Background Designer:** Add special effects/background elements