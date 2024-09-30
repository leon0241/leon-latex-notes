# Leon's UoE Math LaTeX Notes

LaTeX lecture notes and exam notes for a variety of courses in UoE CompSci and Maths. Feel free to use / fork / customise to your liking

:coffee: [(Optional) Buy me a coffee :)](https://ko-fi.com/leon024)

## Links to 6-page Exam Sheets!
- My magnum opus: **Fundamentals of Pure Mathematics** - [click here!](FPM/notes_colour.pdf)
- **Honours Algebra** - [click here!](algebra-6p/algebra-6p.pdf) *(6 pages babyyyy)*
- **Honours Analysis** - [click here!](analysis-6p/analysis-6p.pdf) *done :)*
- **Honours Analysis** - [click here!](analysis-6p/analysis-6p-no-examples.pdf) *(without examples - basically 5 pages)*

- **Metric Spaces** - [click here!](metric-6p/metric-6p.pdf) *(without examples or applications - 5 and a bit pages)*

- **Honours Algebra** everything - [click here!](algebra-10p/algebra-10p.pdf) *(it's 10 pages lol)*

- Y3 **Geometry** - [click here!](Geometry/geometry_notes.pdf) *(they are terrible tho)*
- **Introduction to Theoretical Computer Science** - [click here!](ITCS/itcs_notes.pdf) *(Adapted from Chris Dalziel's LaTeX notes)*

## Links to LaTeX Notes! (probably none of these are getting finished lol)
- **Honours Algebra** (WIP) - [click here!](algebra/algebra-notes.pdf) 
- **Metric Spaces** (WIP) - [click here!](Metric%20Spaces/metric-notes.pdf)
- **Foundations of Natural Language Processing** (BIG WIP) - [click here!](FNLP/fnlp-notes.pdf)


## Info

### Theorem Boxes

Theorem boxes are created using `thmboxes_v2.sty`. Go to [leon-latex-thmboxes](https://github.com/leon0241/leon-latex-thmboxes) for more details

The files `thmboxes_col` and `thmboxes_white` are legacy from the FPM notes. `thmboxes_v2.sty`  might be cross compatible but I'm not going to try. 

Additional Note: `\usepackage{../thmboxes_v2)` to import, but all of my notes will backreference by 1 level since they are in separate folders. If you want to fork and put them in the same folder you just need to `\usepackage{thmboxes_v2)`

### Template Note

A template file is provided in `template/template_note.tex` or `template/template_6p.tex`

`template_note` for article style notes, and `template_6p` for horizontal 6-page notes (check FPM notes for ways to ultra condense as many thmboxes into 6 pages as possible (hint: a lot of negative vspace abuse))

Check thmboxes section on how to use


### Writing LaTeX

Currently using a NeoVim / VimTex / LuaSnip setup to write notes. [Link to nvim config](https://github.com/leon0241/nvim-leon). The actual snippets are in `lua/snippets/tex`. Using TeXLive full installation, but a mini one should work decent, I don't think I use that many obscure packages

nvim is mostly for more flexibility in terms of customising autocomplete (I use `jl` to navigate snippet tabs, `jp` to navigate back which afaik you can't do in VSCode and Obsidian). Obviously though the biggest advantage is the superiority complex and ego boost of using vim :) (i use arch btw 🤓)

Obviously inspired by the late Gilles Castel [Link to his setup](https://castel.dev/)

LuaSnip / UltiSnip on nvim setup guide: [Click Here!](https://ejmastnak.com/tutorials/vim-latex/intro/)

Documentation is not being made for my snippets any time soon, and probably will never be made. I recommend starting off with some basic snippets and find your own custom way of writing snippets :)

Other configs I've tried to use (the FPM notes were made entirely with VSCode, not entirely sure how I did it because I tried to use it again in third year and it wasn't nearly as smooth, might upload my DICE VSCode configs at some point)

- [VSCode with HSnips](https://github.com/leon0241/leon-latex-vscode-hsnip) - [Bonus video in action](https://youtu.be/LiLjxrPmJKo) (Quite possibly outdated)
- [LaTeX Suite with Obsidian](https://github.com/leon0241/latex-suite-config) - Very smooth, and obsidian has the potential to be a great cross-course note-taking app, just requires a lot of dedication and planning


## Legacy Info

**Note**: This is only relevant for the FPM notes

If you want to import into overleaf or anything, you will need `preamble.sty` and either `thmboxes_col.sty` or `thmboxes_white.sty` as well as the main `.tex` file

Included is a `template.tex` file if you want to start from scratch for another course :)

Dependencies that are not in a barebones TinyTeX installation are listed in the dependencies file, if you are using Overleaf / a larger TeX package they should be preinstalled already

If someone knows which package extarticle is included in then lmk :sob:, right now it's just sitting in the folder lol

(only for FPM) Any theorem number is the closest theorem to the lecture notes (some are taken from other sources)
