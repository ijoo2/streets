from imposm.parser import OSMParser

class Graph(object):
    LATITUDE = 0
    LONGITUTE = 1
    highways = 0

    def ways(self, ways):
        for osmid, tags, refs in ways:
            if 'highway' in tags:
                self.highways += 1