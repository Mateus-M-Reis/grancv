let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Códigos/grancv
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 README.md
badd +1 index.py
badd +1 input_type.py
badd +1 app.py
badd +2 app/sidebar.py
badd +92 app/__init__.py
badd +1 app/config.json
badd +1 app/neural_style_transfer.py
badd +1 app/paper.py
badd +79 app/histogram.py
badd +1 app/components/sidebar.py
badd +1 app/components/paper.py
badd +1 assets/style.css
badd +43 app/thresholding.py
badd +35 app/morphology.py
badd +1 app/vvapp/inputs.py
badd +1 app/vvapp/outputs.py
badd +1 app/smoothing.py
badd +1 Aptfile
badd +1 Procfile
badd +1 runtime.txt
badd +1 conda-requirements.txt
badd +1 environment.yml
badd +1 .gitignore
badd +1 app.yaml
badd +1 requirements.txt
badd +1 app/watershed.py
argglobal
%argdel
$argadd app.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit assets/style.css
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe '3resize ' . ((&lines * 26 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
exe '4resize ' . ((&lines * 27 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 64 + 97) / 194)
argglobal
balt index.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 129 - ((48 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 129
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/config.json", ":p")) | buffer app/config.json | else | edit app/config.json | endif
if &buftype ==# 'terminal'
  silent file app/config.json
endif
balt assets/style.css
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
2
normal! zo
2
normal! zo
let s:l = 42 - ((40 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 42
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("README.md", ":p")) | buffer README.md | else | edit README.md | endif
if &buftype ==# 'terminal'
  silent file README.md
endif
balt assets/style.css
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 08|
wincmd w
argglobal
if bufexists(fnamemodify("index.py", ":p")) | buffer index.py | else | edit index.py | endif
if &buftype ==# 'terminal'
  silent file index.py
endif
balt assets/style.css
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
3wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe '3resize ' . ((&lines * 26 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
exe '4resize ' . ((&lines * 27 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 64 + 97) / 194)
tabnext
edit .gitignore
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
3wincmd k
wincmd w
wincmd w
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 14 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 96 + 97) / 194)
exe '2resize ' . ((&lines * 14 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 96 + 97) / 194)
exe '3resize ' . ((&lines * 8 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 96 + 97) / 194)
exe '4resize ' . ((&lines * 15 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 96 + 97) / 194)
exe 'vert 5resize ' . ((&columns * 97 + 97) / 194)
argglobal
balt assets/style.css
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 8 - ((5 * winheight(0) + 7) / 14)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("runtime.txt", ":p")) | buffer runtime.txt | else | edit runtime.txt | endif
if &buftype ==# 'terminal'
  silent file runtime.txt
endif
balt .gitignore
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 7) / 14)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 013|
wincmd w
argglobal
if bufexists(fnamemodify("app.yaml", ":p")) | buffer app.yaml | else | edit app.yaml | endif
if &buftype ==# 'terminal'
  silent file app.yaml
endif
balt .gitignore
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((0 * winheight(0) + 4) / 8)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("Procfile", ":p")) | buffer Procfile | else | edit Procfile | endif
if &buftype ==# 'terminal'
  silent file Procfile
endif
balt .gitignore
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 7) / 15)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 012|
wincmd w
argglobal
if bufexists(fnamemodify("requirements.txt", ":p")) | buffer requirements.txt | else | edit requirements.txt | endif
if &buftype ==# 'terminal'
  silent file requirements.txt
endif
balt .gitignore
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((5 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
wincmd w
exe '1resize ' . ((&lines * 14 + 28) / 57)
exe 'vert 1resize ' . ((&columns * 96 + 97) / 194)
exe '2resize ' . ((&lines * 14 + 28) / 57)
exe 'vert 2resize ' . ((&columns * 96 + 97) / 194)
exe '3resize ' . ((&lines * 8 + 28) / 57)
exe 'vert 3resize ' . ((&columns * 96 + 97) / 194)
exe '4resize ' . ((&lines * 15 + 28) / 57)
exe 'vert 4resize ' . ((&columns * 96 + 97) / 194)
exe 'vert 5resize ' . ((&columns * 97 + 97) / 194)
tabnext
edit app/neural_style_transfer.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
argglobal
balt .gitignore
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 50 - ((37 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 50
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/__init__.py", ":p")) | buffer app/__init__.py | else | edit app/__init__.py | endif
if &buftype ==# 'terminal'
  silent file app/__init__.py
endif
balt app/neural_style_transfer.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=3
setlocal fml=1
setlocal fdn=20
setlocal fen
23
normal! zo
23
normal! zc
23
normal! zc
let s:l = 64 - ((13 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 64
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/sidebar.py", ":p")) | buffer app/sidebar.py | else | edit app/sidebar.py | endif
if &buftype ==# 'terminal'
  silent file app/sidebar.py
endif
balt app/neural_style_transfer.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
18
normal! zo
18
normal! zc
let s:l = 4 - ((3 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
tabnext
edit app/paper.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
argglobal
balt app/neural_style_transfer.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
9
normal! zo
14
normal! zo
22
normal! zo
22
normal! zc
let s:l = 13 - ((12 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/histogram.py", ":p")) | buffer app/histogram.py | else | edit app/histogram.py | endif
if &buftype ==# 'terminal'
  silent file app/histogram.py
endif
balt app/sidebar.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
11
normal! zo
17
normal! zo
37
normal! zo
37
normal! zo
37
normal! zc
71
normal! zo
let s:l = 79 - ((3 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 79
normal! 02|
wincmd w
argglobal
if bufexists(fnamemodify("app/sidebar.py", ":p")) | buffer app/sidebar.py | else | edit app/sidebar.py | endif
if &buftype ==# 'terminal'
  silent file app/sidebar.py
endif
balt app/histogram.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
4
normal! zo
4
normal! zo
18
normal! zo
18
normal! zc
let s:l = 18 - ((17 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 18
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
tabnext
edit app/smoothing.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
argglobal
balt app/paper.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 7 - ((6 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 04|
wincmd w
argglobal
if bufexists(fnamemodify("app/morphology.py", ":p")) | buffer app/morphology.py | else | edit app/morphology.py | endif
if &buftype ==# 'terminal'
  silent file app/morphology.py
endif
balt app/smoothing.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 38 - ((0 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 38
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/thresholding.py", ":p")) | buffer app/thresholding.py | else | edit app/thresholding.py | endif
if &buftype ==# 'terminal'
  silent file app/thresholding.py
endif
balt app/smoothing.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 19 - ((0 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 19
normal! 02|
wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 64 + 97) / 194)
exe 'vert 3resize ' . ((&columns * 64 + 97) / 194)
tabnext
edit app/watershed.py
argglobal
balt app/smoothing.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 2 - ((1 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 02|
tabnext
edit app/vvapp/outputs.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 96 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 97 + 97) / 194)
argglobal
balt app/watershed.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
326
normal! zo
let s:l = 374 - ((359 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 374
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("app/vvapp/inputs.py", ":p")) | buffer app/vvapp/inputs.py | else | edit app/vvapp/inputs.py | endif
if &buftype ==# 'terminal'
  silent file app/vvapp/inputs.py
endif
balt app/vvapp/outputs.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 2 - ((1 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 96 + 97) / 194)
exe 'vert 2resize ' . ((&columns * 97 + 97) / 194)
tabnext 1
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
