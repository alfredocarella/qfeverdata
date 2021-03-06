qfevermaps
=====================

Jupyter notebooks for downloading and visualizing Scopus article metadata using Pandas.

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
1. [**01_bibsearch.ipynb**](https://github.com/alfredocarella/qfeverdata/blob/master/01_bibsearch.ipynb): saves a database search locally as `.json`, `.xlsx` and `.csv`.
2. [**02_data_cleanup.ipynb**](https://github.com/alfredocarella/qfeverdata/blob/master/02_data_cleanup.ipynb): code for cleaning up the downloaded data. It includes (for now) a quick and dirty colormap plot example for this data.
3. Last version of [main.py](https://github.com/alfredocarella/qfeverdata/blob/master/main.ipynb). Note that the notebook *cannot* be run online. This link just displays the last version.

## To-do
| Order | Task          | Status        | Comment |
|:------:| ------------- |:-------------:| :--------:|
| 1      | ~~Write a minimum working example that saves data to `.json`, `.xlsx` and `.csv` and link it here.~~ | **Done** | [01_bibsearch.ipynb](https://github.com/alfredocarella/qfeverdata/blob/master/01_bibsearch.ipynb) |
| 2      | Upload a Jupyter notebook template for R code. It may (or not) be as easy as following [these instructions](https://irkernel.github.io/) | pending | Alfredo + José |
| 3      | ~~Improve generality and readability of parsing code (the code converting the raw .json into neat tables).~~ | **Done** | [02_data_cleanup.ipynb](https://github.com/alfredocarella/qfeverdata/blob/master/02_data_cleanup.ipynb) |
| 4      | Start adding (Python or R) notebooks with possible research questions and ways to explore/answer them (i.e. generate material) | pending | Alfredo + José |

## Ideas to discuss
* Would it make any sense to see how a map like the one in [`02_data_cleanup.ipynb`](https://github.com/alfredocarella/qfeverdata/blob/master/02_data_cleanup.ipynb) changes after each year?
Do we have any external *"real-world"* information we could potentially correlate the changes with? (e.g. evidence of increased funding, a research program, a Q-fever outbreak, etc.)
  * It ~~*should be* relatively~~ **is quite** easy to create video-like image sequences and see if there are any meaningful changes/evolution year by year for a given topic.
