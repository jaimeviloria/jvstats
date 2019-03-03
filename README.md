# getstats, a commandline tool for retrieving stats

## Requirements
* make
* python3
* virtualenv

## Installation

`sudo make install`
Installs getstats

## Quickstart using Virtualenv

1. `make test`
This creates virtualenv in the Makefile directory

2. `source virtualenv/bin/activate`

## Quickstart using Docker

## Usage: 

Example
`
>>> from getstats import Delays
>>> d = Delays()
>>> d.delays
[]
>>> d.addDelay(100)
[100]
>>> d.medians
[-1]
>>> d.sliding_window
[100]
>>> d.addDelay(102)
[100, 102]
>>> d.medians
[-1, 101]
>>> d.sliding_window
[100, 102]
>>> d.addDelay([101,110,120])
[100, 102, 101, 110, 120]
>>> d.sliding_window
[101, 110, 120]
>>> d.medians
[-1, 101, 101, 102, 110]
>>> d.delays=[100,102]
>>> d.medians
[-1, 101]
`

### Testing

`make test`
creates the virtualenv and python binaries necessary for testing as well as running the unittests

