#!/usr/bin/python

import os
import sys
from os.path import join

ext_dir = join( 'external', os.name )
try:
	os.mkdir(ext_dir)
except OSError:
	pass

sys.path.append( 'lib' )
sys.path.insert( 0, ext_dir )

os.environ['PYTHONPATH'] = ext_dir

from setuptools.command import easy_install
for requirement in file('packages.txt'):
	if requirement.strip().startswith('#'): continue 
	easy_install.main( ['--install-dir='+ext_dir, requirement] )
