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
#nodes.print_node_set()


def select_nodes_in_rectangle(nodes, min_lat, max_lat, min_lng, max_lng):
    # actual min and max latitude and longitude of coordinates
    #if needed change <= to <
    nodes_in_rectangle = NodeSet()
    for k, node in nodes.get_nodes().items():
        if(min_lat <= node.lat and node.lat <= max_lat and
           min_lng <= node.lng and node.lng <= max_lng):
            nodes_in_rectangle.add(k, node.lat, node.lng)

    return nodes_in_rectangle
in_rec = select_nodes_in_rectangle(nodes, 58.3984, 58.3990, 15.5733, 15.576)
in_rec.print_node_set()
