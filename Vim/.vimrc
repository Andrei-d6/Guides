syntax on
syntax enable

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
"set termguicolors
set scrolloff=8
set visualbell
set guicursor=

set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

set completeopt-=preview
"colorscheme molokai
colorscheme gruvbox

call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
Plug 'vim-utils/vim-man'
Plug 'lyuts/vim-rtags'
Plug 'git@github.com:Valloric/YouCompleteMe.git'
call plug#end()

set background=dark
