# Project Compilation Guide (Pandoc + LaTeX)

This project uses **Pandoc** to convert Markdown documents into a formatted PDF with bibliography support (IEEE style).

---

## Requirements

Before compiling, ensure you have the following installed:

* [Pandoc](https://pandoc.org/)
* A LaTeX distribution:

  * TeX Live (Linux)
  * MacTeX (macOS)
  * MiKTeX (Windows)

Check installation:

```bash
pandoc --version
xelatex --version
```

---

## Project Structure

```
cv-uav-internship-upv/
│── main.md
│── references.bib
│── ieee.csl
│── assets/
│── output.pdf
```

---

## Compilation Command

To generate the PDF:

```bash
pandoc main.md \
  --pdf-engine=xelatex \
  --citeproc \
  --bibliography=references.bib \
  --csl=ieee.csl \
  -o output.pdf
```

---

## Bibliography System

This project uses:

* **BibTeX file**: `references.bib`
* **IEEE citation style**: `ieee.csl`
* **Citation syntax in Markdown**:

  ```markdown
  This is a citation [@key].
  ```

Example:

```markdown
YOLO models are widely used in detection tasks [@mi_yolo11s-uav_2026].
```