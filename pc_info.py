#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
InfoGathering help your seem your machine info:)
'''
__copyright__ ="Copyright 2021, Morpho-BadUsb | YourMachineInfoGathering Tool"
__version__   ="1.0" 
__codename__  = "Morpho"
__status__    ="Junior Developer" 


import os

b = os.uname()
print(b)
print("""
	MachineOs        : {} {}
	MachineName      : {}
	Version          : {}
	Version Data	 : {}
""".format(
	b.sysname, b.machine,
	b.nodename,
	b.release,
	b.version
	))
