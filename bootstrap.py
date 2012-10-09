from os.path import abspath, dirname, join

base_dir = abspath( dirname(__file__) )
tools_dir = join( base_dir, "tools" )
conf_dir = join( base_dir, "conf" )
data_dir = join( base_dir, "data" )
logs_dir = join( base_dir, "logs" )

import sys
sys.path.append( join(base_dir,'lib') )
sys.path.insert( 0, join(base_dir,'external') )

from pkg_resources import require
for requirement in file( 'packages.txt' ):
	require( requirement )
