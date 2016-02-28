from imposm.parser import OSMParser

class Graph(object):
    LATITUDE = 0
    LONGITUTE = 1

    def __init__(self, osmfile):
        # parse input file