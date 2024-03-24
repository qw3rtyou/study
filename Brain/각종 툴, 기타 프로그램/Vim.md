---
sticker: lucide//text-selection
---

# 사용법

## 일반모드
다른 모드에서 `esc` 키를 클릭하면 일반 모드로 전환

- 커서 이동
<table><colgroup><col style="width: 29.6%"><col style="width: 17.6%"><col style="width: 17.6%"><col style="width: 17.6%"><col style="width: 17.6%"></colgroup><tbody><tr><td data-highlight-colour="#deebff"><p><strong>gg </strong></p><p>첫 행으로 이동</p></td><td data-highlight-colour="#ffffff"><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>k</strong></p><p>위로 이동</p></td><td data-highlight-colour="#ffffff"><p></p></td><td data-highlight-colour="#ffffff"><p></p></td></tr><tr><td data-highlight-colour="#deebff"><p><strong>0</strong></p><p>행의 처음으로 이동</p></td><td data-highlight-colour="#eae6ff"><p><strong>h</strong></p><p>왼쪽으로 이동</p></td><td data-highlight-colour="#eae6ff"><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>l</strong></p><p>오른쪽으로 이동</p></td><td data-highlight-colour="#deebff"><p><strong>$</strong></p><p>행의 끝으로 이동</p></td></tr><tr><td data-highlight-colour="#deebff"><p><strong>G</strong></p><p>마지막 행으로 이동</p></td><td><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>j</strong></p><p>아래로 이동</p></td><td><p></p></td><td><p></p></td></tr></tbody></table>

- 삭제, 복사 붙여넣기
<table><colgroup><col style="width: 21.4%"><col style="width: 78.6%"></colgroup><tbody><tr><th><p><strong>x</strong></p></th><td data-highlight-colour="#ffffff"><p>현재 커서가 위치한 글자 삭제 (del)</p></td></tr><tr><th><p><strong>X</strong></p></th><td><p>현재 커서 앞 글자 삭제 (backspace)</p></td></tr><tr><th><p><strong>dd</strong></p></th><td><p>현재 커서가 위치한 행 삭제</p></td></tr><tr><th><p><strong>yy</strong></p></th><td><p>현재 커서가 위치한 행 복사</p></td></tr><tr><th><p><strong>p</strong></p></th><td><p>복사한 내용을 현재 행 이후에 붙여넣기</p></td></tr><tr><th><p><strong>P</strong></p></th><td><p>복사한 내용을 현재 행 이전에 붙여넣기</p></td></tr></tbody></table>

- 문자열 찾기

|   |   |
|---|---|
|**/문자열, enter**|현재 커서 이후로 문자열 찾기|
|**n**|찾은 문자열 목록에서 다음 문자로 이동|

- 되돌리기

|   |   |
|---|---|
|**u**|이전 수정 사항 되돌리기|

## 입력모드

- 입력 모드 명령 키
<table><colgroup><col style="width: 29.6%"><col style="width: 17.6%"><col style="width: 17.6%"><col style="width: 17.6%"><col style="width: 17.6%"></colgroup><tbody><tr><td data-highlight-colour="#ffffff"><p></p></td><td data-highlight-colour="#ffffff"><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>O</strong></p><p>현재 커서 이전 줄에 입력</p></td><td data-highlight-colour="#ffffff"><p></p></td><td data-highlight-colour="#ffffff"><p></p></td></tr><tr><td data-highlight-colour="#deebff"><p><strong>I</strong></p><p>현재 커서가 위치한 행의 처음에 입력</p></td><td data-highlight-colour="#eae6ff"><p><strong>s</strong></p><p>현재 커서 한 글자 지우고 입력</p></td><td data-highlight-colour="#eae6ff"><p><strong>i</strong></p><p>현재 커서 위치에 입력</p></td><td data-highlight-colour="#eae6ff"><p><strong>a</strong></p><p>현재 커서 다음 칸에 입력</p></td><td data-highlight-colour="#deebff"><p><strong>A</strong></p><p>현재 커서가 위치한 행의 마지막에 입력</p></td></tr><tr><td><p></p></td><td><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>S </strong></p><p>현재 커서 한 줄 지우고 입력</p></td><td><p></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p></p></td><td data-highlight-colour="#eae6ff"><p><strong>o</strong></p><p>현재 커서 다음 줄에 입력</p></td><td><p></p></td><td><p></p></td></tr></tbody></table>




## 명령모드

- 명령 모드 명령어

|   |   |
|---|---|
|**:w**|저장|
|**:q**|종료|
|**:i**|취소|
|**:wq**|저장하고 종료|
|**:q!**|저장하지 않고 종료|
|**:%s/문자열1/문자열2/g**|전체에서 문자열1을 모두 찾아 문자열2로 치환|


# 창 관리
- `:split` 또는 `:sp`: 수평 분할
- `:vsplit` 또는 `:vsp`: 수직 분할
- `Ctrl + w` 후 화살표 키: 창 간 이동


# 추천 플러그인

`~/.vimrc`
```sh
" Basic Settings
set nu
syntax on
set termguicolors
let mapleader=","
set smartindent
set tabstop=3
set shiftwidth=3
set autoindent
set cindent
set ruler
set rnu
set showmatch
set title

map <C-h> <C-w>h
map <C-l> <C-w>l
map <C-k> <C-w>k
map <C-j> <C-w>j

highlight ColorColumn ctermbg=gray
set colorcolumn=80

set encoding=UTF-8
set noswapfile

" auto ()
inoremap ( ()<Left>
inoremap ( ()<Left>
inoremap { {}<Left>
inoremap [ []<Left>
inoremap " ""<Left>
inoremap ' ''<Left>
```

# Neovim, CoC 설치
- Neovim
```sh
sudo apt update
sudo apt install neovim
```

```sh
mkdir ~/.config/nvim
touch ~/.config/nvim/init.vim
```

`vim ~/.config/nvim/init.vim`
```sh
call plug#begin('~/.vim/plugged')

Plug 'altercation/vim-colors-solarized'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-commentary'
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-airline/vim-airline'
Plug 'Raimondi/delimitMate'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'preservim/tagbar'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'nanotech/jellybeans.vim'
Plug 'sainnhe/everforest'


call plug#end()
"theme
" if has('termguicolors')
"  set termguicolors
" endif
" let g:everforest_better_performance = 1
" set background=dark
" let g:everforest_background = 'hard'
" colorscheme everforest
"gruvbox
let g:gruvbox_contrast_dark="hard"
set background=dark
autocmd vimenter * ++nested colorscheme gruvbox

"Airline
let g:airline_theme='gruvbox'
let g:airline#extensions#tabline#enabled = 1

" coc
"just says autocomplete with the first option if pop up menu is open.
inoremap <silent><expr> <TAB> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<TAB>"

" TS
lua <<EOF
require'nvim-treesitter.configs'.setup {
	ensure_installed = { "c", "lua", "vim", "cpp" },
  highlight = {
    enable = true,              -- false will disable the whole extension
    disable = { "rust"},  -- list of language that will be disabled
	 additional_vim_regex_highlighting = false,
  },
}
EOF

" delimitMate
let delimitMate_expand_cr=1

" The-Nerd-Tree
autocmd BufEnter * lcd %:p:h
autocmd VimEnter * if !argc() | NERDTree | endif
nmap <leader>ne :NERDTreeToggle<cr>
let NERDTreeShowLineNumbers=1
let g:NERDTreeWinPos = "left"


" Basic Settings
set cursorline
set nu
syntax on
set termguicolors
let mapleader=","
set smartindent
set tabstop=3
set shiftwidth=3
set autoindent
set cindent
set ruler

map <C-h> <C-w>h
map <C-l> <C-w>l
map <C-k> <C-w>k
map <C-j> <C-w>j

highlight ColorColumn ctermbg=gray
set colorcolumn=80

set encoding=UTF-8

augroup templates
autocmd BufNewFile  [0-9]*.{c,cpp}	0r ~/.vim/skeleton.c
augroup END
```

- CoC (Conquer of Completion)
```sh
curl -sL install-node.now.sh/lts | sudo bash
```

```sh
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

모두 설치 후 Neovim 실행하고, `:PlugInstall` 으로 플러그인 설치

