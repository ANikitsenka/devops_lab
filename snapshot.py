#!/usr/bin/env python

import configparser
import datetime
import psutil
import time
import json

log = {}
s = 'SNAPSHOT'


class Logger:

    @staticmethod
    def timestamp():
        timestamp = datetime.datetime.now()
        return str(timestamp)

    @staticmethod
    def cpu():
        cpu_usage = psutil.cpu_percent(interval=1)
        return str(cpu_usage)

    @staticmethod
    def swap():
        swap_usage = psutil.swap_memory().percent
        return str(swap_usage)

    @staticmethod
    def v_mem():
        v_memory = psutil.virtual_memory()[2]
        return str(v_memory)

    @staticmethod
    def disk():
        disk_usage = psutil.disk_usage('/').percent
        return str(disk_usage)

    @staticmethod
    def net():
        net_recv = psutil.net_io_counters().bytes_recv / 1024
        return str(net_recv)


config = configparser.ConfigParser()
config.read('config.ini')
config_dict = dict(config.items('common'))


def json_log(j):
    log.clear()
    ss = s + ' ' + str(j)
    log[ss] = [{'Time': Logger.timestamp()}]
    log[ss].append({'CPU, %': Logger.cpu(), 'SWAP, %': Logger.swap(), 'Memory': Logger.v_mem(),
                    'Disk': Logger.disk(), 'Received, k/bytes': Logger.net()})
    with open('log.json', 'a+') as outfile:
        json.dump(log, outfile, indent=4)


def text_log(k):
    file = open('log.txt', 'a+')
    file.write(
        'SNAPSHOT N' + str(k) + ': ' + Logger.timestamp() + '; ' + 'CPU usage: ' + Logger.cpu() +
        '%; SWAP usage: ' + Logger.swap() + '%; Memory: ' + Logger.v_mem() + '; Disk usage: '
        + Logger.disk() + '%; Received k/bytes: ' + Logger.net() + '\r\n')


def execute():
    #    log = {}
    i = 1
    #    s = 'SNAPSHOT'
    if config_dict['output'] == 'json':
        while True:
            json_log(i)
            i += 1
            time.sleep(float(config_dict['interval']) * 60)
    elif config_dict['output'] == 'text':
        while True:
            text_log(i)
            i += 1
            time.sleep(float(config_dict['interval']) * 60)
    else:
        print('Available output parameters: "json" and "text"')


if __name__ == "__main__":
    execute()
