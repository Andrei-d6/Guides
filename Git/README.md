# Git and Github

[Cheatsheet](https://supersimpledev.github.io/references/git-github-reference.pdf)

<br>

## Part 1 - Replicating Google Docs Version History

This path of the guide is based on this [tutorial](https://www.youtube.com/watch?v=hrTQipWp6co)

### How to correct mistakes (e.g. forgot to add changes or misspelled comments)

```bash
git add <new changes>
git commit -m "Correctly spelled comment" --amend
```

### How to take changes out of the staging area (reset changes)

```bash
# staging => working
git reset <file | folder>

# working => remove the changes
git checkout -- <file | folder>
```

### Viewing previous versions of our code

```bash
git checkout <commit hash>
git log [--all] [--graph] [--pretty=oneline] [-n 10] [--skip=10]
```

### Restoring code to the previous version (Google docs Version History)

```bash
git checkout <commit hash> <file | folder>
git commit -m "Version updated without branching"
```

### Undoing the last commit 

```bash
# Reset without losing uncommited changes (will change the commit history!)
git reset --soft HEAD~1

# Remove all unstaged changes
git reset --hard HEAD~1

# Creates a new commit with the changes that are rolled back 
git revert <commit hash to revert>
```

<br>
<br>

## Part 2 - Branching and Merging

[Tutorial](https://www.youtube.com/watch?v=Q1kHG842HoI)


### Creating (and switching to) a branch

```bash
git branch <name of branch>

# Also switching to the new branch
git checkout <name of branch>
```

### Merging

The result of the merge will be on the branch that you are **currently working on**. That said, the result should usually go on the **master branch**.

```bash
# First go back to the branch that the result will go onto (e.g., master)
git checkout master

# Merge the branch onto mater (since we are now on master)
git merge <name of branch> -m "Message for the merge commit"
```

### Merge conflicts

If merging a branch leads to a conflict (the merge couldn't be done automatically), the places where git cannot decide the merge result will look something like this:

```text
<<<<<<< HEAD (Current Change)
code1
=======
code2
>>>>>>> branch (Incoming Change)
```

To resolve the conflict, simply keep the final code and delete everything else. For example:

```text
code2
```

Actually, the result can also be something entirely different. The conflict is resolved as long as you tell git what the result should be. To finish the merge, add a commit after all conflicts are resolved:

```bash
git add .
git commit -m "Merge conflict resolved"
```

### TL;DR (feature branch workflow)

The Feature Branch Workflow:

1. Create a feature branch
2. Upload feature branch to GitHub
3. Create a "Pull Request" (do code reviews)
4. Merge feature branch into master branch


```bash                         
# 1. Create feature branch
git branch <feature branch>
git checkout <feature branch>

# (Suppose we do some changes)
git add .
git commit -m "New feature"


# 2. Upload feature branch to GitHub
git push origin <feature branch>


# 3. Creating the pull request (manually)
# This part is done from GitHub interface
# [base: master] <-- [compare <new-feature branch>]
#
# Then add a simple description and press "Create Pull Request"


# 4. Merge feature branch into master branch
# Again this is done in the GitHub interface
# After resolving conflicts and comments press:
# Merge pull request -> Confirm merge
#
# To update the changes locally (sync local repo):
git fetch
git checkout master
git pull origin master
```

### Resolving conflicts locally

The idea is to merge `master` into the `feature branch` with the conflict

```bash
git checkout master
git pull origin master

git checkout <feature branch>
git merge master

# Now actually resolve the conflicts
git add .
git commit -m "Conflict resolved"

git push origin <feature branch>
```

