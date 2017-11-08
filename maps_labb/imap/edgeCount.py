# Parser example
# Usage python parser_ex.py 

import sys
from datetime import datetime

from mapvis.osm_parser import get_default_parser

# The first argument after the python module on the commandline
#filename = sys.argv[0]

# Parse the supplied OSM file
start = datetime.now()

parser = get_default_parser('Ourmap.osm')

edges = 0
for way in parser.iter_ways():
    edges += 1

end = datetime.now()

print("The data contains", edges, "ways")
print("Parsing the date took", (end - start).total_seconds(), "seconds")
