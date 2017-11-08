from mapvis.osm_parser import get_default_parser
from mapvis.store import NodeSet

def extract_osm_nodes(f_name):
    # Parse the supplied OSM file
    print("Loading data...")
    parser = get_default_parser(f_name)
    node_set = NodeSet()

    for node in parser.iter_nodes():
        node_set.add(node['id'], node['lat'], node['lon'])

    return node_set

nodes = extract_osm_nodes('Ourmap.osm')
nodes.print_node_set()
