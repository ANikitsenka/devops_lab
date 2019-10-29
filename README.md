# homework5
Simple scripts.

## Description 
htask5.py: This script collects python info and saves it to info.json and info.yaml.
test_task3.py and task3.py - try to understand and use unittest.
## Usage
Example of output htask5.py:

JSON:
{
    "Python version:": "3.6.8",
    "Virtual environment:": "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv",
    "Python executable:": "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/bin/python",
    "PIP version:": "19.0.3",
    "PYTHONPATH:": "/home/andrei/Documents/DevOps_Lab/10_python/homework5",
    "Installed packs:": [
        "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3.6/site-packages",
        "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/local/lib/python3.6/dist-packages",
        "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3/dist-packages",
        "/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3.6/dist-packages",
        "/usr/lib/python3.6/site-packages",
        "/usr/local/lib/python3.6/dist-packages",
        "/usr/lib/python3/dist-packages",
        "/usr/lib/python3.6/dist-packages"
    ],
    "Packs_versions": {
        "setuptools": "40.8.0",
        "pip": "19.0.3"
    }
}

YAML:
'Installed packs:': [/home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3.6/site-packages,
  /home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/local/lib/python3.6/dist-packages,
  /home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3/dist-packages,
  /home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/lib/python3.6/dist-packages,
  /usr/lib/python3.6/site-packages, /usr/local/lib/python3.6/dist-packages, /usr/lib/python3/dist-packages,
  /usr/lib/python3.6/dist-packages]
'PIP version:': 19.0.3
'PYTHONPATH:': /home/andrei/Documents/DevOps_Lab/10_python/homework5
Packs_versions: {pip: 19.0.3, setuptools: 40.8.0}
'Python executable:': /home/andrei/Documents/DevOps_Lab/10_python/homework5/venv/bin/python
'Python version:': 3.6.8
'Virtual environment:': /home/andrei/Documents/DevOps_Lab/10_python/homework5/venv

### Running
htask5.py

task3.py and test_task3.py:
nosetests
nosetests --with-coverage

### Requirements
import os
import sys
import pip
import site
import json
import yaml
from pip._internal.utils.misc import get_installed_distributions



