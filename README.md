# Leon's UoE Math LaTeX Notes

LaTeX lecture notes and exam notes for a variety of courses in UoE CompSci and Maths. Feel free to use / fork / customise to your liking

### :coffee: [(Optional) Buy me a coffee :)](https://ko-fi.com/leon024)

## Links to 6-page Exam Sheets

<details>
<summary>Year 2</summary>
<b>Fundamentals of Pure Mathematics</b> - <a href="exam-sheets/FPM/notes_colour.pdf">click here!</a>
</details>

<details>
    <summary>Year 3</summary>
    <ul>
        <li> <b>Honours Algebra</b> - <a href="exam-sheets/algebra-6p/algebra-6p.pdf">click here!</a> </li>
        <li> <b>Honours Analysis</b> - <a href="exam-sheets/analysis-6p/analysis-6p.pdf">click here!</a> <i>(without examples - basically 5 pages)</i> </li> 
        <li> <b>Honours Analysis</b> - <a href="exam-sheets/analysis-6p/analysis-6p-no-examples.pdf">click here!</a> <i>*(without examples or applications - 5 and a bit pages)*</i> </li>
        <li> <b>Metric Spaces</b> - <a href="exam-sheets/metric-6p/metric-6p.pdf">click here!</a> </li>
        <li> <b>Honours Algebra</b> everything - <a href="exam-sheets/algebra-10p/algebra-10p.pdf">click here!</a> <i>*(10 pages)*</i> </li>
        <li> <b>Geometry</b> - <a href="exam-sheets/Geometry/geometry_notes.pdf">click here!</a> <i>(they are terrible tho)</i> </li>
        <li> <b>Introduction to Theoretical CS</b> - <a href="exam-sheets/ITCS/itcs_notes.pdf">click here!</a> <i>(Adapted from Chris Dalziel's LaTeX notes)</i> </li>
    </ul>
</details>

<details>
    <summary>Year 4</summary>
    <ul>
        <li> <b>General Topology</b> - <a href="exam-sheets/gentop-6p/gentop-6p.pdf">click here!</a> </li>
        <li> <b>Group Theory</b> - <a href="exam-sheets/group-theory-6p/group-theory-6p.pdf">click here!</a> </li>
        <li> <b>Algebraic Topology</b> - <a href="exam-sheets/algtop-6p/algtop-6p.pdf">click here!</a> </li>
        <li> <b>Galois Theory</b> - <a href="exam-sheets/galois-6p/galois-6p.pdf">click here!</a> </li>
    </ul>
</details>


## Links to LaTeX Lecture Notes! (none of these are getting finished lol)
<details>
    <summary>Click Here</summary>
    <ul>
        <li> <b>Honours Algebra</b> (WIP) - <a href="algebra/algebra-notes.pdf">click here!</a></li>
        <li> <b>Metric Spaces</b> (WIP) - <a href="Metric%20Spaces/metric-notes.pdf">click here!</a></li>
        <li> <b>Foundations of Natural Language Processing</b> (BIG WIP) - <a href="FNLP/fnlp-notes.pdf">click here!</a></li>
    </ul>
    these probably also don't compile properly as well because I changed the file structure a while back and never updated them.
</details>


## Additional Information

### 🎁 Theorem Boxes

Theorem boxes are created using `thmboxes_v3.sty`. Go to [leon-latex-thmboxes](https://github.com/leon0241/leon-latex-thmboxes) for more details

Additional Note: `\usepackage{../thmboxes_v2)` to import, but all of my notes will backreference by 1 level since they are in separate folders. If you want to fork and put them in the same folder you just need to `\usepackage{thmboxes_v2)`

### 📁 Respository Structure
This repo is laid out in the following way
- `exam-sheets/` for 6-page exam cheat sheets. 
- `lecture-notes/` for lecture notes. 
- `legacy/` contains old files for Y2 or Y3 notes such old versions of `thmboxes.sty`.
- `other/` includes anything else such as a script to convert lecture notes to 6 page ones, or a script to convert obsidian callouts to thmboxes.
- `packages/` includes external latex packages.
- `rss/` includes the following LaTeX files:
    - `customs.sty` has custom definitions for commands such as page wide bars
    - `thmboxes.sty` includes the definition for the custom theorem boxes
- `template/` includes a template for both lecture notes and 6 page cheat sheets
- `preamble.sty` includes prerequisite imported packages for any 6 page notes.

### ✏️ LaTeX File Structure
The following files are imported for a cheat sheet:

```

\usepackage{../../preamble}
\usepackage{symbols}
```

`preamble` is the master preamble for the repo (note the double layers of backreferencing), while `symbols` is a local sty file for any custom symbol definitions which would change per file. 

Additionally imported from within `preamble` is `rss/thmboxes` and `rss/customs`.

### ⌨️ Writing LaTeX

Currently using a NeoVim / VimTex / LuaSnip setup to write notes. [Link to nvim config](https://github.com/leon0241/nvim-leon). The actual snippets are in `lua/snippets/tex`. Using TeXLive full installation, but a mini one should work decent, I don't think I use that many obscure packages

nvim is mostly for more flexibility in terms of customising autocomplete (I use `jl` to navigate snippet tabs, `jp` to navigate back which afaik you can't do in VSCode and Obsidian). Obviously though the biggest advantage is the superiority complex and ego boost of using vim :) (i use arch btw 🤓)

Obviously inspired by the late Gilles Castel [Link to his setup](https://castel.dev/)

LuaSnip / UltiSnip on nvim setup guide: [Click Here!](https://ejmastnak.com/tutorials/vim-latex/intro/)

Documentation is not being made for my snippets any time soon, and probably will never be made. I recommend starting off with some basic snippets and find your own custom way of writing snippets :)

Other configs I've tried to use (the FPM notes were made entirely with VSCode, not entirely sure how I did it because I tried to use it again in third year and it wasn't nearly as smooth, might upload my DICE VSCode configs at some point)

- [VSCode with HSnips](https://github.com/leon0241/leon-latex-vscode-hsnip) - [Bonus video in action](https://youtu.be/LiLjxrPmJKo) (Quite possibly outdated)
- [LaTeX Suite with Obsidian](https://github.com/leon0241/latex-suite-config) - Very smooth, and obsidian has the potential to be a great cross-course note-taking app, just requires a lot of dedication and planning


## 🪦 Legacy Info

**Note**: This is only relevant for the FPM notes

If you want to import into overleaf or anything, you will need `preamble.sty` and either `thmboxes_col.sty` or `thmboxes_white.sty` as well as the main `.tex` file

Included is a `template.tex` file if you want to start from scratch for another course :)

Dependencies that are not in a barebones TinyTeX installation are listed in the dependencies file, if you are using Overleaf / a larger TeX package they should be preinstalled already

If someone knows which package extarticle is included in then lmk :sob:, right now it's just sitting in the folder lol

(only for FPM) Any theorem number is the closest theorem to the lecture notes (some are taken from other sources)
