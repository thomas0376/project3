# these modules need installing


# these are built in modules
import platform
import sys


# these are user defined modules



###########################################################################
# Should code run on a python version =! 3.12.6 then alt execution
###########################################################################

if platform.python_version() == '3.12.6':
    print( f"\nHello, I'm Python Version: {platform.python_version()}" )
    print( f"\nThis is where I live: {sys.executable}" )
    print( f"\nI'm happy to keep executing this code !!\n")
else:
    print( f"\nHello, I'm Python Version: {platform.python_version()}" )
    print( f"\nYou should be using Python Version: 3.12.6")
    print( f"\nCode will stop executing now !!")
    sys.exit()


