# Coding Assignment

A python script to generate list of unexpired certificates using censys api's

## Quick Guide
This script uses censys api's to get the list of certificates and convert the certifcates to csv format

## Installation

Download the python, poetry libraries

Use the poetry package manager to install packages defined in `pyproject.toml` file

```bash
# Command
poetry install
```
## Setup the config variables

To configure your api credentials run `censys config`.

```sh
$ censys config

Censys API ID: XXX
Censys API Secret: XXX
Do you want color output? [y/n]: y

Successfully authenticated for your@email.com
```

## Usage
run the index.py files where it has main logic to find unexpired certificates and generate csv files 


- Clone the repository from the  [git](https://censys-python.readthedocs.io/en/stable/usage-v2.html)
- Move to `coding-assignment` folder
- Run the below command

```sh
python index.py
```
