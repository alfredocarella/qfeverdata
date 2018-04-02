# bibliomaps

## Prerequisites
*   An API key from http://dev.elsevier.com
*   Python 3.x on your machine. If you still haven't installed it, you might want to get the [Anaconda distribution of Python 3.6](https://www.continuum.io/downloads) and get a lot of useful packages in one go.
*   A network connection at an institution that subscribes to Scopus and/or ScienceDirect

## Quick start
*   Download or clone this repository
*   Run `pip install -r requirements.txt` in order to ensure you have the right dependencies installed (I am 99% sure I have included all the necessary packages there).
*   Create a [config file and add your APIkey](https://github.com/ElsevierDev/elsapy/blob/master/CONFIG.md) to it. I have included my own APIkey, but please avoid using it extensively or I may get in trouble.
*   Run the command `jupyter notebook` and open the file "main.ipynb" (which you can modify at will).
