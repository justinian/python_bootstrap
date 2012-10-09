#!/usr/bin/python

import os
import sys
sys.path.append( 'lib' )
sys.path.insert( 0, 'external' )

os.environ['PYTHONPATH'] = 'external'

from setuptools.command import easy_install
for requirement in file('packages.txt'):
	if requirement.strip().startswith('#'): continue 
	easy_install.main( ['--install-dir=external', requirement] )
