from imposm.parser import OSMParser
from config import config
from osmdata import Graph

class Streets(object):
    def __init__(self):
        print "Reading OpenStreetMap data from file=", config['osm_data']
        # data = Graph(config['osm_data'])

        data = Graph()
        p = OSMParser(concurrency=4, ways_callback=data.ways)
        p.parse(config['osm_data'])
        print data.highways

if __name__ == "__main__":
    Streets()
