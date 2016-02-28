from imposm.parser import OSMParser
from config import config
from osmdata import Graph

class Streets(object):
    def __init__(self):
        print "Reading OpenStreetMap data"
        data = Graph(config['osm_data'])

if __name__ == "__main__":
    Streets()
