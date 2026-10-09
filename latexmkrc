@default_files = ('main.tex');
$pdf_mode = 4; # LuaLaTeX is required for the theme font.
$lualatex = 'lualatex -shell-escape %O %S'; # Convert SVG artwork with Inkscape.
$ENV{'TEXINPUTS'} = './styles//:' . ($ENV{'TEXINPUTS'} // '');
