
# Styles for Better Scientific Figures

This directory contains Matplotlib style files designed to enhance the appearance of scientific figures.

*Note: To enable LaTeX rendering in your figures, ensure LaTeX is installed on your system. For an easy installation, you can download [MiKTeX](https://miktex.org/download).*


## Serif-Style Font Configuration

or figures with a general serif-style font, use the following settings:

```text
## ***************************************************************************
## * FONT                                                                    *
## ***************************************************************************
font.family:            serif
font.serif:             STIXGeneral
mathtext.fontset:       stix

font.size:              10
```

<br>

## LaTeX-Style Font Configuration

To achieve a LaTeX-like appearance in your figures, ensure the following font settings are applied (for LaTeX typeface, pure black colors are recommended):

```text
## ***************************************************************************
## * FONT                                                                    *
## ***************************************************************************
font.serif:             cmr10, Computer Modern Serif, DejaVu Serif
font.family:            serif
axes.formatter.use_mathtext: True
mathtext.fontset:       cm

text.usetex:            True
text.latex.preamble:    \usepackage{amsmath} \usepackage{amssymb}



## ***************************************************************************
## * COLORS                                                                  *
## ***************************************************************************
text.color:             k      # 0.2
xtick.color:            k      # 0.2
ytick.color:            k      # 0.2
axes.labelcolor:        k      # 0.2
axes.edgecolor:         k      # 0.2
legend.edgecolor:       k      # 0.2
```