# How to setup **vim** the way you like it

Create the following:
```bash
mkdir ~/.vim/undodir
mkdir ~/.vim/colors
```

## .vimrc
If you dont have a `.vimrc` create a new one by using:
```bash
touch ~/.vimrc
```
or just upload your existing one in the home directory.

## Colorscheme
Move your color schemes in the `~/.vim/colors` directory and don't forget to set the colorscheme inside the `.vimrc` file.

## Plugins
Inside the `.vimrc` you may have some plugins.
<br>
If you want to install them run:
```bash
:PlugInstall
```
from inside the `.vimrc` file. It is very likely that you will have an error regarding the `YouCompleteMe` plugin. To fix this run the following commands:
```bash
cd ~/.vim/plugged/YouCompleteMe/
./install.py
```
and then **run `:PlugInstall` again** from inside the `.vimrc` file.


## Note
Try to keep up to the the `.vimrc` file and the **colorschemes**.