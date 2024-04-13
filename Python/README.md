# Python tutorial and useful resources

## Cookiecutter Data Science

Cookiecutter has a series of neat templates for different use cases (such as [Data Science](https://drivendata.github.io/cookiecutter-data-science/) or Django Projects).

Although for the Data Science the main bit is the Directory Structure, one thing that seems to pop up pretty often is the way to automatically reload the notebook when changing source code.

```python
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2
```

## Nb Mypy

[Nb Mypy](https://pypi.org/project/nb-mypy/#:~:text=Nb%20Mypy%20is%20a%20facility,information%20about%20the%20execution%20history.) is a facility to automatically run mypy on Jupyter notebook cells as they are executed, whilst retaining information about the execution history.

For an example please see this [notebook](https://gitlab.tue.nl/jupyter-projects/nb_mypy/-/blob/master/Nb_Mypy.ipynb)

The short version is:
```python
%load_ext nb_mypy
# or
%nb_mypy unknown

# Where: 
Unknown argument
 Valid arguments: ['', '-v', 'On', 'Off', 'DebugOn', 'DebugOff', 'mypy-options OPTIONS']
```
