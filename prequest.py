import argparse
import requests
import getpass


parser = argparse.ArgumentParser()
parser.add_argument('-u', nargs=1,
                    help="user for authorization.", required=True)
parser.add_argument('-repolist', action="store_true",
                    help="Repos' list of current account.")
parser.add_argument('-userdisk', action="store_true",
                    help="Disk and creation info of current account.")
parser.add_argument('-f',
                    action="store_true",
                    help="Fork info (IDs + users). Require users' and repos' name (-fu and -fr).")
parser.add_argument('-fu', help='Username for "Fork info"')
parser.add_argument('-fr', help='Repo name for "Fork info"')
parser.add_argument('-pr',
                    action="store_true",
                    help="PR info (IDs + users). Require users' and repos' name (-pru and -prr).")
parser.add_argument('-prt',
                    action="store_true",
                    help="PR info (Users + time). Require users' and repos' name (-pru and -prr).")
parser.add_argument('-pru', help='Username for "PR info"')
parser.add_argument('-prr', help='Repo name for "PR info"')
parser.add_argument('-v', action="version", version="beta_version 0.1")
args = parser.parse_args()

password = getpass.getpass()
url = "https://api.github.com"

if args.f:
    data = (requests.get(url + '/repos/' + args.fu + '/' + args.fr + '/forks',
                         auth=(args.u[0], password))).json()
    for item in data:
        dictionary = {item.get('owner').get('login'): item.get('owner').get('id')}
        for i in dictionary:
            print(dictionary[i]),
            print(i)
elif args.repolist:
    data = (requests.get('https://api.github.com/user/repos', auth=(args.u[0], password))).json()
    print('Repos list:')
    for item in data:
        dictionary = [item.get('full_name')]
        for i in dictionary:
            print(i)
elif args.userdisk:
    data = (requests.get('https://api.github.com/user', auth=(args.u[0], password))).json()
    print('Disk_usage = ' + str(data['disk_usage']))
    print('Created at: ' + data['created_at'])
elif args.pr:
    data = (requests.get(url + '/repos/' + args.pru + '/' + args.prr + '/pulls',
                         auth=(args.u[0], password))).json()
    for item in data:
        dictionary = {item.get('title'): item.get('id')}
        for i in dictionary:
            print(dictionary[i]),
            print(i)
elif args.prt:
    data = (requests.get(url + '/repos/' + args.pru + '/' + args.prr + '/pulls',
                         auth=(args.u[0], password))).json()
    for item in data:
        dictionary = {item.get('title'): item.get('created_at')}
        for i in dictionary:
            print(i)
            print(dictionary[i])
else:
    print("Something wrong! Please enter 'prequest.py -h' for help."
          " Also README.md stores examples of using.")
