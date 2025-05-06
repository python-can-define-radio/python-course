# Jupyter/Jupytext Proof of Concept

#### Scripts below to copy .ipynb file (Jupyter Journal) to a .py file (Jupytext), and sync them so the .py files can be uploaded to Github for version control

Convert .ipynb notebook to .py file, and sync the .py file with the notebook
```
jupytext --set-formats py,ipynb EXAMPLE_FILE.ipynb
jupytext --sync EXAMPLE_FILE.ipynb
```

