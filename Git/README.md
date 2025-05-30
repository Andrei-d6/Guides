# Git and Github

[Cheatsheet](https://supersimpledev.github.io/references/git-github-reference.pdf)

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

# Part 2




# Branching and Merging


[Tutorial](https://www.youtube.com/watch?v=Q1kHG842HoI)