let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Códigos/grancv
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 index.py
badd +1 input_type.py
badd +1 app.py
badd +95 app/sidebar.py
badd +92 app/__init__.py
badd +1 app/config.json
badd +1 app/neural_style_transfer.py
badd +1 app/paper.py
badd +3 README.md
badd +61 app/histogram.py
badd +1 app/components/sidebar.py
badd +1 app/components/paper.py
badd +1 assets/style.css
badd +43 app/thresholding.py
badd +35 app/morphology.py
badd +1 app/vvapp/inputs.py
badd +1 app/vvapp/outputs.py
badd +1 ~/Códigos/grancv/app/smoothing.py
badd +1 Aptfile
badd +1 Procfile
badd +1 runtime.txt
badd +1 conda-requirements.txt
badd +1 environment.yml
badd +1 .gitignore
badd +1 app.yaml
badd +1 requirements.txt
argglobal
%argdel
$argadd app.py
set stal=2
edit assets/style.css
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
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe '3resize ' . ((&lines * 27 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
exe '4resize ' . ((&lines * 25 + 28) / 56)
exe 'vert 4resize ' . ((&columns * 75 + 113) / 227)
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 125 - ((44 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
125
normal! 02|
wincmd w
argglobal
if bufexists("app/config.json") | buffer app/config.json | else | edit app/config.json | endif
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
let s:l = 98 - ((95 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
98
normal! 0
wincmd w
argglobal
if bufexists("README.md") | buffer README.md | else | edit README.md | endif
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
exe s:l
normal! zt
1
normal! 0
wincmd w
argglobal
if bufexists("index.py") | buffer index.py | else | edit index.py | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 2 - ((1 * winheight(0) + 12) / 25)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
2
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe '3resize ' . ((&lines * 27 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
exe '4resize ' . ((&lines * 25 + 28) / 56)
exe 'vert 4resize ' . ((&columns * 75 + 113) / 227)
tabedit .gitignore
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
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
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe '2resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe '3resize ' . ((&lines * 11 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
exe '4resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 4resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 5resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 6resize ' . ((&columns * 75 + 113) / 227)
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((3 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 0
wincmd w
argglobal
if bufexists("runtime.txt") | buffer runtime.txt | else | edit runtime.txt | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 013|
wincmd w
argglobal
if bufexists("app.yaml") | buffer app.yaml | else | edit app.yaml | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((0 * winheight(0) + 5) / 11)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 0
wincmd w
argglobal
if bufexists("Procfile") | buffer Procfile | else | edit Procfile | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 6) / 13)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 012|
wincmd w
argglobal
if bufexists("requirements.txt") | buffer requirements.txt | else | edit requirements.txt | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((4 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 0
wincmd w
argglobal
if bufexists("environment.yml") | buffer environment.yml | else | edit environment.yml | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
wincmd w
5wincmd w
exe '1resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe '2resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe '3resize ' . ((&lines * 11 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
exe '4resize ' . ((&lines * 13 + 28) / 56)
exe 'vert 4resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 5resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 6resize ' . ((&columns * 75 + 113) / 227)
tabedit app/neural_style_transfer.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 65 - ((52 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
65
normal! 0
wincmd w
argglobal
if bufexists("app/__init__.py") | buffer app/__init__.py | else | edit app/__init__.py | endif
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
30
normal! zo
30
normal! zc
30
normal! zc
49
normal! zo
54
normal! zo
54
normal! zc
49
normal! zc
let s:l = 64 - ((46 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
64
normal! 0
wincmd w
argglobal
if bufexists("app/sidebar.py") | buffer app/sidebar.py | else | edit app/sidebar.py | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
24
normal! zo
26
normal! zo
112
normal! zo
145
normal! zo
145
normal! zo
145
normal! zc
145
normal! zc
26
normal! zc
24
normal! zc
let s:l = 31 - ((7 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
31
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
tabedit app/paper.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 113 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 113 + 113) / 227)
argglobal
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
let s:l = 11 - ((10 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
11
normal! 06|
wincmd w
argglobal
if bufexists("app/histogram.py") | buffer app/histogram.py | else | edit app/histogram.py | endif
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
let s:l = 76 - ((51 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
76
normal! 02|
wincmd w
exe 'vert 1resize ' . ((&columns * 113 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 113 + 113) / 227)
tabedit ~/Códigos/grancv/app/smoothing.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((4 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 03|
wincmd w
argglobal
if bufexists("app/morphology.py") | buffer app/morphology.py | else | edit app/morphology.py | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 38 - ((36 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
38
normal! 0
wincmd w
argglobal
if bufexists("app/thresholding.py") | buffer app/thresholding.py | else | edit app/thresholding.py | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 19 - ((17 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 02|
wincmd w
exe 'vert 1resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 75 + 113) / 227)
exe 'vert 3resize ' . ((&columns * 75 + 113) / 227)
tabedit app/vvapp/outputs.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 113 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 113 + 113) / 227)
argglobal
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
let s:l = 335 - ((319 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
335
normal! 0
wincmd w
argglobal
if bufexists("app/vvapp/inputs.py") | buffer app/vvapp/inputs.py | else | edit app/vvapp/inputs.py | endif
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 26) / 53)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 02|
wincmd w
exe 'vert 1resize ' . ((&columns * 113 + 113) / 227)
exe 'vert 2resize ' . ((&columns * 113 + 113) / 227)
tabnext 2
set stal=1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
