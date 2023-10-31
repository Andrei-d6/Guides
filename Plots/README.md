# Making better scientific plots

This guide is inspired by the **[SciencePlots](https://github.com/garrettj403/SciencePlots/)** package which offers *Matplotlib styles for scientific figures*. <br>

This repo contains a set of Matplotlib styles for better formatting of figures for research papers, academic articles, presentations, theses or any formal scientific document.

<div align="center">
    <img src="examples/figures/trial.jpg" alt="Example plot" width="70%"/>
</div>


## Using the Styles

The main style intended for use is called `"science"`. In order to set is as the style for the plots, this should be added to the python script/notebook:

```python
import matplotlib.pyplot as plt

# When running from a Jupyter notebook, don't forget to add this
%matplotlib inline

# Assuming "science.mlpstyle" is in the current directory
plt.style.use('science.mlpstyle')


# Otherwise here is a quick and dirty example for making it work
# with an arbitrary path
from pathlib import Path
path_styles = Path('../styles')


def styles(paths):
    paths = [paths] if not isinstance(paths, list) else paths
    return [path_styles/f"{path}.mlpstyle" for path in paths]


with plt.style.context(styles(['science'])):
    # The plotting stuff goes here
    pass
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

## Styles Differences

```yaml
# Minimal is science with the following differences:
xtick.minor.visible:    False
xtick.top:              False

ytick.minor.visible:    False
ytick.right:            False

axes.spines.right:      False
axes.spines.top:        False


# Clasic is science with the following differences:
xtick.minor.visible:    False
xtick.top:              False

ytick.minor.visible:    False
ytick.right:            False
```

## Matplotlib specifics


### Matplotlib defaults

The default matplotlib configuration can be found [here](https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file).

### Setting the fonts

Most of the fonts are generally set to a certain size via `font.size`, for a more granular approach, please consider the following settings:

```yaml
axes.labelsize:         12
legend.fontsize:        12
legend.title_fontsize:  12
axes.titlesize:         14
xtick.labelsize:        12
ytick.labelsize:        12
```

### Ten simple rules for better figures

On the subject of making better plots, the following [paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833) provides a comprehensive breakdown on some of the most important aspects to consider when creating scientific visualizations. <br>

Also, a nice guide and repo from the previous paper (including the nice sine and cosine plot) on using matplotlib can be found [here](https://github.com/rougier/matplotlib-tutorial/tree/master).

### Anatomy of a figure

Taken from [here](https://matplotlib.org/stable/users/explain/quick_start.html), the following image displays various elements of a matplotlib figure.

<div align="center">
    <img src="examples/figures/plot_anatomy.png" alt="Example plot" width="55%"/>
</div>

### Tutorials

On the subject of having an example/tutorial on how to plot something nicely, please consider the following resources:

- [Matplotlib Tutorial (2022): For Physicists, Engineers, and Mathematicians](https://www.youtube.com/watch?v=cTJBJH8hacc)
- 


## Examples

<https://www.youtube.com/watch?v=cTJBJH8hacc&t=1593s>
