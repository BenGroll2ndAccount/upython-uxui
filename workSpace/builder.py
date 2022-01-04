import json
import framework as fw
import tree

class Builder():
    def __init__(self, size_h, size_w, resolution, dead_clusters):
        self.h = size_h
        self.w = size_w
        self.resolution = resolution
        self.dead_clusters = dead_clusters
    
    def render(self, output = False):
        grid = [] # --> grid setup
        for i in range(0, self.h):
            grid.append([0 for i in range(self.w)])

        #--> Print and return grid
        if output:
            for i in grid:
                print(i)
        return grid

build = Builder(10, 20, 2, [11])
build.render(True)



