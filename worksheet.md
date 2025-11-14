# Git Worksheet 

For Git Workshop, Tech GC, November 16, 2025

## Activity Overview

**Activity Name**: ASCII Art Mascot Collaborative Puzzle\
**Objective**: Learn Git branch management, merging, and conflict resolution through collaborative ASCII art creation.\
**Group Size**: 2-4 people per group

## Exercises

- ### Exercise 0 : Environment Setup

#### **SSH Setup**

Generate SSH Key:
```
ssh-keygen -t ed25519 -C "your_sjtu_email@sjtu.edu.cn"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy Key and Add to GitHub:
```
cat ~/.ssh/id_ed25519.pub
```

- ### Exercise 1 : Remote to Local

Create and connect repository.
```
git init
git clone
```

- ### Exercise 2 : Modification I

Change your file and commit the changes.
```
git status
git add
git diff
git status
git commit
git reset
```

- ### Exercise 3 : Branch & Modification II

Create and switch branches.
```
git branch
git checkout
```

Change and commit again, and then push to the remote repository.
```
git push
```

- ### Exercise 4 : Merge & Conflict

Merge the branches and resolve conflict.
```
git merge
git rebase
```

## Activity Checklist

### Preparation Phase

- [ ] Git environment configuration completed
- [ ] Initial repository setup
- [ ] Participant Git basic training
- [ ] Role assignment clarified

### Execution Phase  

- [ ] Acquisition of basic Git commands
- [ ] All branches created successfully
- [ ] Individual creation by each role completed
- [ ] Merge conflict experience completed
- [ ] Conflict resolution discussion conducted
- [ ] Final integration successful

### Conclusion Phase

- [ ] Work showcase and sharing
- [ ] Git techniques review

Now that you have mastered the core workflow of Git, keep exploring and make it a powerful assistant in your collaborative projects! 