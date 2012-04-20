#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os

path = os.path.expanduser('~') + '/.config/.Lindict.cfg'

def read_config():
    if os.path.exists(path):

        config = ConfigParser.ConfigParser()

        with open(path, 'rw') as config_file:
            config.readfp(config_file)
            return config.get('close_state', 'key')


def write_config(close_state):
    cfgfile = open(path, 'w')
    cfgfile.close()
    config = ConfigParser.ConfigParser()
    with open(path, 'rw') as config_file:
        config.readfp(config_file)
        config.add_section('close_state')
        config.set('close_state', 'key', close_state)
        config.write(open(path, 'r+'))
