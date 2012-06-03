##########################################################################
#  Copyright (C) 2012 by Jactry Zeng                                     #
#                                                                        #
#  This program is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>. #
##########################################################################

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
