from django.shortcuts import render_to_response
from django.template import Template, Context
from mapvis.extractor import * # change here

# Create your views here.
from django.http import HttpResponse
import datetime

def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>tjabbatjenahallej, tiden är nu %s.</body></html>" % now
    return HttpResponse(html)

def mapapp(request):
    node_set = extract_osm_nodes("Ourmap.osm")
    node_set = select_nodes_in_rectangle(node_set, 58.3984, 58.3990,
                                                   15.5733, 15.576)
    c = Context({'GMAPS_API_KEY': 'AIzaSyDRHfQSRMEJl7XA7D6SiXr2e7M4RruAJcc',
    'COORDS': node_set.get_nodes().values()},)

    return render_to_response('mapvis/mapapp.html', c)
