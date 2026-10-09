@default_files = ('main.tex');
$pdf_mode = 4; # LuaLaTeX is required for the theme font.
$ENV{'TEXINPUTS'} = './styles//:' . ($ENV{'TEXINPUTS'} // '');
