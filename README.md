# DLI Scraper

Python3 scraper for the free language courses available on livelingua.com

This is really practical, not necessarily well organized or generic. There are 2 steps to getting the data:

1. Pulling metadata for each course (main.py, takes very little disk space)
2. Downloading the pdf and mp3 files themselves (downloader.py, takes several gb of disk space)

## Installing required packages

(I use a virtual environment, which is autoignored by the .gitignore if you name it venv)
```
python3 -m pip install -r requirements.txt
```

## Downloading metadata

```
python3 main.py
```

## Downloading files

```
python3 downloader.py
```
