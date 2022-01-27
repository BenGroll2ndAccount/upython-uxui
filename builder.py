
from graphics import *
def _render(data, zoom):
    display = GraphWin("PaperDisplay", len(data[0])*zoom, len(data)*zoom)
    print(str(len(data[0])*zoom) + " x " + str(len(data)*zoom))
    for x in range(len(data[0])):
        for y in range(len(data)):
            r = Rectangle(Point(x * zoom, y * zoom), Point(x * zoom + zoom, y * zoom + zoom))
            r.setFill("black") if data[y][x] else r.setFill("white")
            r.draw(display)
    input()


_render([[0, 1], [1, 0]], 60)