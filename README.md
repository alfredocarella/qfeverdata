# bibliomaps

## Prerequisites
*   An API key from http://dev.elsevier.com
*   Python 3.x on your machine. If you still haven't installed it, you might want to get the [Anaconda distribution of Python 3.6](https://www.continuum.io/downloads) and get a lot of useful packages in one go.
*   A network connection at an institution that subscribes to Scopus and/or ScienceDirect

## Quick start
*   Download or clone this repository
*   Run `pip install -r requirements.txt` in order to ensure you have the right dependencies installed (I am 99% sure I have included all the necessary packages there).
*   Create a [config file and add your APIkey](https://github.com/ElsevierDev/elsapy/blob/master/CONFIG.md) to it.
*   Run the command `jupyter notebook` and open the file "main.ipynb" (which you can modify at will).

## Useful links
*	Last version of [main.py](https://bitbucket.org/losvetes/qfeverdata/annotate/master/main.ipynb?fileviewer=notebook-viewer%3Anbviewer). Note that the notebook *cannot* be run online. This link just displays the last version.
*	Current version of the [Article](https://www.sharelatex.com/project/5ab9fb9706d3305b5eb40cc2) (**Share**LaTeX)

## To-do
| Task          | Status        | Responsible |
| ------------- |:-------------:| :--------:|
| Write a minimum working example that saves data to .xlsx and .csv and link it here | pending | Alfredo |
| Upload a Jupyter notebook template for R code | pending | Alfredo |
| Improve generality and readability of parsing code (the code converting the raw .json into neat tables). | pending | Alfredo |
| Start adding (Python or R) notebooks with possible research questions and ways to explore/answer them (i.e. generate material) | pending | Alfredo & José |
