#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 00:38:12 2018

@author: chun
"""

import datetime

player = 'cjx'
turn = 4
startTime = datetime.datetime.strptime("2018-02-15 00:15:31", "%Y-%m-%d %H:%M:%S")
duration = 155.28943
hint = 0

#Store data in json file
data = {'player': player,
        'turns': turn+1,
        'startTime': datetime.datetime.strftime(startTime, "%Y-%m-%d %H:%M:%S"),
        'duration': duration,
        'hints': hint}

with open('stats.txt', 'a') as file:
    file.write(json.dumps(data))
    file.write('\n')