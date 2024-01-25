# Making the terminal look better

## How to display only current direcotry in bash prompt

https://superuser.com/questions/186743/how-do-i-only-display-the-base-dir-in-my-ubuntu-terminal

Instructions:

```bash
sudo vim ~/.bashrc
```

Change \w (lowercase) to \W (uppercase):

```vim
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
                                                                                       ^^
            this one waaaaaay over here ------------------------------------------------+ 
```

Finally, open a new terminal.

## Windows terminal relevant settings to change

After chaning the following settings, also make sure to change the default terminal to WSL2.

- Default font size 10
- Opacity 95%
- Columns 107
- Rows 25
