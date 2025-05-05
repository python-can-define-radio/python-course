# Jupyter/Jupytext Proof of Concept

#### Scripts below to copy .ipynb file (Jupyter Journal) to a .py file (Jupytext), and sync them so the .py files can be uploaded to Github for version control

Convert .ipynb notebook to .py file
```
jupytext --set-formats py,ipynb --execute EXAMPLE_FILE.ipynb
```

Sync the .py file with the notebook
```
jupytext sync EXAMPLE_FILE.ipynb
```

