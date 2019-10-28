# prequest utility
Simple script.

## Description 
This script works with GitHub restAPI.
Parse some info and statistics (see "Usage" below").

## Usage
usage: prequest.py [-h] -u U [-repolist] [-userdisk] [-f] [-fu FU] [-fr FR]
                   [-pr] [-prt] [-pru PRU] [-prr PRR] [-v]

optional arguments:
  -h, --help  show this help message and exit
  -u U        user for authorization.
  -repolist   Repos' list of current account.
  -userdisk   Disk and creation info of current account.
  -f          Fork info (IDs + users). Require users' and repos' name (-fu and
              -fr).
  -fu FU      Username for "Fork info"
  -fr FR      Repo name for "Fork info"
  -pr         PR info (IDs + users). Require users' and repos' name (-pru and
              -prr).
  -prt        PR info (Users + time). Require users' and repos' name (-pru and
              -prr).
  -pru PRU    Username for "PR info"
  -prr PRR    Repo name for "PR info"
  -v          show program's version number and exit


Examples:
python prequest.py -u ANikitsenka -f -fu alenaPy -fr devops_lab
python prequest.py -u ANikitsenka -repolist
python prequest.py -u ANikitsenka -userdisk
python prequest.py -u ANikitsenka -pr -pru alenaPy -prr devops_lab
python prequest.py -u ANikitsenka -prt -pru alenaPy -prr devops_lab

### Running
python prequest.py -u ANikitsenka -userdisk

### Requirements
argparse
requests
getpass


