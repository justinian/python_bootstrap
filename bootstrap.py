import os
import sys
from os.path import abspath, dirname, join

base_dir = abspath( dirname(__file__) )
tools_dir = join( base_dir, "tools" )
conf_dir = join( base_dir, "conf" )
data_dir = join( base_dir, "data" )
logs_dir = join( base_dir, "logs" )

ext_dir = join( base_dir, 'external', os.name )
sys.path.insert( 0, join(base_dir,'lib') )
sys.path.insert( 0, ext_dir )

from pkg_resources import require, DistributionNotFound
for requirement in file( 'packages.txt' ):
	try:
		require( requirement )
	except DistributionNotFound:
		print "Required package '%s' not found. Please run install_external.py." % (requirement.strip(),)
		sys.exit(1)
