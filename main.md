---
lang: en-EN
geometry: 
  - a4paper
  - top=2cm
  - bottom=2cm
  - left=2cm
  - right=2cm
fontsize: 12pt
numbersections: true
toc: true
toc-depth: 2
csl: ieee.csl
bibliography: references.bib
colorlinks: true
linkcolor: black
urlcolor: black
documentclass: article
header-includes: |
  \usepackage{fancyhdr}
  \usepackage{graphicx}
  \usepackage[hyphens]{url}
  \usepackage{microtype}
  \usepackage{enumitem}
  \usepackage{xcolor}
  \usepackage{lastpage}
  \usepackage{newunicodechar}
  \DeclareTextCommandDefault{\textupperdiagonalarrow}{\raisebox{0.5ex}{\scriptsize$\nearrow$}}
  \newunicodechar{⬀}{\textupperdiagonalarrow}
  \newunicodechar{⤴}{\textupperdiagonalarrow}
  \newunicodechar{≥}{\ensuremath{\geq}}
  \newunicodechar{≤}{\ensuremath{\leq}}
  \emergencystretch=3em
  \sloppy
  \pagestyle{fancy}
  \fancyhf{}
  \fancyfoot[C]{\thepage\ / \pageref{LastPage}}
  \renewcommand{\headrulewidth}{0pt}
  \graphicspath{{./assets/}{./}}
  \setlist{nosep, leftmargin=*}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{6pt}
  \usepackage{ragged2e}
  \justifying
  
  \pagestyle{fancy}
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  
  \fancyfoot[C]{\thepage}
  
  \graphicspath{{./assets/}{./}}
  \setlist{nosep, leftmargin=*}
  \setlength{\parindent}{0pt}
  \setlength{\parskip}{6pt}
  \usepackage{ragged2e}
  \justifying
  
  \pagenumbering{roman}

---

\newpage
\listoffigures

\newpage
\clearpage
\pagenumbering{arabic}
\setcounter{page}{1}

\newpage
# Introduction {-}
Test [@mi_yolo11s-uav_2026].

\newpage
# Conclusion {-}

\newpage
# References {-}