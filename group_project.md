# ASCII Art Mascot Puzzle - Git Collaboration Workshop Activity Plan

## Activity Overview

**Activity Name**: ASCII Art Mascot Collaborative Puzzle  
**Objective**: Learn Git branch management, merge conflict resolution, and team collaboration through collaborative ASCII art creation  
**Duration**: 0.5 hours  
**Group Size**: 3-4 people per group

## Activity Preparation

### Environment Setup

```bash
# 1. Create activity repository
git init mascot-collaboration
cd mascot-collaboration

# 2. Prepare basic file structure
mkdir -p docs scripts templates
touch mascot_ascii.txt README.md .gitignore

# 3. Initial commit
git add .
git commit -m "Initialize ASCII art project"
```

### File Template

**`mascot_ascii.txt` initial content:**
```

ASCII Mascot Collaboration Project - Academy 2024

Head (5 lines, 20 characters each):
====================
====================
====================
====================
====================

Body (5 lines, 20 characters each):
====================
====================
====================
====================
====================

Legs (3 lines, 20 characters each):
====================
====================
====================

Roles:
- Head Designer
- Body Designer
- Leg Designer
- Effects Designer
```

## Detailed Activity Process

### Phase 1: Project Launch (15 minutes)

#### 1.1 Project Introduction

```bash
# Demonstrate basic operations
git clone [repository-url]
cd mascot-collaboration
cat mascot_ascii.txt
```

#### 1.2 Branch Strategy Explanation

```bash
# Create main development branch
git checkout -b main

# Each role creates feature branches
git checkout -b feature/head-design
git checkout -b feature/body-design  
git checkout -b feature/leg-design
git checkout -b feature/effects-design
```

### Phase 2: Independent Creation (30 minutes)

#### 2.1 Individual Work by Role

**Head Designer Example:**

```bash
git checkout feature/head-design

# Edit head section, save as:
Head (5 lines, 20 characters each):
     /\___/\    
    ( = . = )   
    >   ^   <   
    |       |   
    \_______/   
```

**Body Designer Example:**

```bash  
git checkout feature/body-design

# Edit body section:
Body (5 lines, 20 characters each):
    |       |   
    | "CS"  |   
    |-------|   
    | Code  |   
    \_______/   
```

#### 2.2 Commit Standards

```bash
# Use conventional commits
git add mascot_ascii.txt
git commit -m "feat(head): add cat face expression design"
git commit -m "feat(body): add CS theme body design"
```

### Phase 3: Merge Conflict Experience (25 minutes)

#### 3.1 First Merge Attempt

```bash
# Switch back to main branch
git checkout main

# Try merging head design
git merge feature/head-design

# Try merging body design → Conflict will occur here!
git merge feature/body-design
```

#### 3.2 Typical Conflict Scenarios

**Boundary Conflict Example:**
```
<<<<<<< HEAD
    \_______/
=======
    |       |
>>>>>>> feature/body-design
```

**Content Overlap Conflict:**
```
<<<<<<< HEAD (feature/head-design)
    |       |
    \_______/
=======
    | "CS"  |
    |-------|
>>>>>>> feature/body-design
```

### Phase 4: Conflict Resolution Workshop (20 minutes)

#### 4.1 Conflict Resolution Strategies

```bash
# Manually edit to resolve conflicts
# Select the best parts from both creative ideas

# Mark after resolution
git add mascot_ascii.txt
git commit -m "fix: resolve head and body boundary conflict"
```

#### 4.2 Team Collaboration Tools

```bash
# Use git diff to compare changes
git diff feature/head-design feature/body-design

# Use git log to view history
git log --oneline --graph --all
```

### Phase 5: Final Integration and Presentation (15 minutes)

#### 5.1 Complete Merge

```bash
# Merge all feature branches
git merge feature/leg-design
git merge feature/effects-design

# Push to main branch
git checkout main
git merge main
```

#### 5.2 Work Showcase

**Final Result Example:**
```
     /\___/\    
    ( = . = ) 
    >   ^   <   
    | "CS"  |   
    |-------|   
    | Code  |   
    \_______/   
    /       \   
   /         \   
  /_/\/\/\/\/\_\
     Academy 2024
```

## Activity Checklist

### Preparation Phase

- [ ] Git environment configuration completed
- [ ] Initial repository setup
- [ ] Participant Git basic training
- [ ] Role assignment clarified

### Execution Phase  

- [ ] All branches created successfully
- [ ] Individual creation by each role completed
- [ ] Merge conflict experience completed
- [ ] Conflict resolution discussion conducted
- [ ] Final integration successful

### Conclusion Phase

- [ ] Work showcase and sharing
- [ ] Git techniques review
- [ ] Project archiving

## Teaching Points

### Git Skills Focus

1. Branch management: create, switch, delete branches
2. Merge strategies: fast-forward merge, three-way merge
3. Conflict resolution: manual editing, tool usage

### Collaboration Skills Focus

1. Communication and coordination: boundary agreements, style unification
2. Problem solving: creative conflict handling
3. Quality assurance: format standards, visual coordination