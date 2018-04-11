# qfevermaps

## Prerequisites
*   An API key from http://dev.elsevier.com
*   Python 3.x on your machine. If you still haven't installed it, you might want to get the [Anaconda distribution of Python 3.6](https://www.continuum.io/downloads) and get a lot of useful packages in one go.
*   A network connection at an institution that subscribes to Scopus and/or ScienceDirect

## Quick start
*   Download or clone this repository
*   Run `pip install -r requirements.txt` in order to ensure you have the right dependencies installed (I am 99% sure I have included all the necessary packages there).
*   Create a [config file and add your APIkey](https://github.com/ElsevierDev/elsapy/blob/master/CONFIG.md) to it.
*   Run the command `jupyter notebook` and open the file `main.ipynb` (or any of the files with that extension).

## Useful links
1. Last version of [main.py](https://bitbucket.org/losvetes/qfeverdata/annotate/master/main.ipynb?fileviewer=notebook-viewer%3Anbviewer). Note that the notebook *cannot* be run online. This link just displays the last version.
2. Current version of the [Article](https://www.sharelatex.com/project/5ab9fb9706d3305b5eb40cc2) (**Share**LaTeX)
3. [**bibsearch.ipynb**](https://bitbucket.org/losvetes/qfeverdata/annotate/master/bibsearch.ipynb?fileviewer=notebook-viewer%3Anbviewer): saves a database search locally as `.json`, `.xlsx` and `.csv`.
4. [**data_cleanup.ipynb**](https://bitbucket.org/losvetes/qfeverdata/annotate/master/data_cleanup.ipynb?fileviewer=notebook-viewer%3Anbviewer): code for cleaning up the downloaded data. It includes (for now) a quick and dirty colormap plot example for this data.

## To-do
| Order | Task          | Status        | Comment |
|:------:| ------------- |:-------------:| :--------:|
| 1      | ~~Write a minimum working example that saves data to `.json`, `.xlsx` and `.csv` and link it here.~~ | **Done** | [bibsearch.ipynb](https://bitbucket.org/losvetes/qfeverdata/annotate/master/bibsearch.ipynb?fileviewer=notebook-viewer%3Anbviewer) |
| 2      | Upload a Jupyter notebook template for R code. It may (or not) be as easy as following [these instructions](https://irkernel.github.io/) | pending | Alfredo + José |
| 3      | Improve generality and readability of parsing code (the code converting the raw .json into neat tables). | **In progress...** | [data_cleanup.ipynb](https://bitbucket.org/losvetes/qfeverdata/annotate/master/data_cleanup.ipynb?fileviewer=notebook-viewer%3Anbviewer) |
| 4      | Start adding (Python or R) notebooks with possible research questions and ways to explore/answer them (i.e. generate material) | pending | Alfredo + José |
