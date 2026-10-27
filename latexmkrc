@default_files = ('main.tex');
$pdf_mode = 4; # LuaLaTeX, needed for the theme font
$lualatex = 'lualatex -shell-escape %O %S'; # shell escape for the Inkscape SVG conversion
$ENV{'TEXINPUTS'} = './styles//:' . ($ENV{'TEXINPUTS'} // ''); # for the older \usepackage{amurmaplewvu}
