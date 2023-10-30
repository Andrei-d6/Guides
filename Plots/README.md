# Making better scientific plots

This guide is inspired by the **[SciencePlots](https://github.com/garrettj403/SciencePlots/)** package which offers *Matplotlib styles for scientific figures*. <br>

This repo contains a set of Matplotlib styles for better formatting of figures for research papers, academic articles, presentations, theses or any formal scientific document.


# TODO: ADD FIGURE HERE

## Matplotlib defaults

The default matplotlib configuration can be found [here](https://matplotlib.org/stable/users/explain/customizing.html)

## Using the Styles

The main style intended for use is called `"science"`. In order to set is as the style for the plots, this should be added to the python script/notebook:

```python
import matplotlib.pyplot as plt

# Assuming "science.mlpstyle" is in the current directory
plt.style.use('science.mlpstyle')


# Otherwise add the corresponding path
import sys
sys.path.append('../styles')
```

Also, multiple style can be used together (the order is important as the next styles might override some of the settings set by the previous ones).

```python
plt.style.use(['science.mlpstyle', 'latex.mlpstyle'])
```

For this example, the `latex` style will override the font family and size from the `science` style. <br>

To use a style only temporarily, you can use a context manager:

```python
with plt.style.context(['science.mlpstyle']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

## Ten simple rules for better figures

On the subject of making better plots, the following [paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833) provides a comprehensive breakdown on some of the most important aspects to consider when creating scientific visualizations. <br>

Also, a nice guide and repo from the previous paper (including the nice sine and cosine plot) on using matplotlib can be found [here](https://github.com/rougier/matplotlib-tutorial/tree/master).

## Examples
