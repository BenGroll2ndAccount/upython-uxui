from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
import graphics
from unotifier import uNOTIFY
class ROOT:
    def build(self, rootnode):
        self.wallpaper = graphics.GraphWin("Wallpaper", width=528, height = 880)
        uNOTIFY.add_listener("darkmode_enabled", self)



