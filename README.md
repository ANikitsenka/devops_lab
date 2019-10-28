# Snapshots 
Simple script

## Description 
This script creates pc's status snapshots to json or text file.

## Usage
Parameters of config.ini should be placed in [common] block:
output: type of file. 'json' or 'text' are available.
interval: logging interval in minutes

Example of config.ini file:

[common]
output = text
interval = 1

### Running
Import and use as any other packages:
```python
>>> import snapshot
>>> snaphot.run()
```

### Requirements
psutil

