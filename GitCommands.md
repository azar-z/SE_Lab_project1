# Git Aliases 

## pr Command  
Add this to your ~/.gitconfig:
```ini
[alias]
    pr = "!f() { git fetch origin pull/$1/head:pr-$1 && git checkout pr-$1; }; f"

```

Then you can fetch & checkout a pull request (by number) with 'pr' command.

example:

```ini
git pr 123 
```
