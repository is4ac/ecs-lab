import curses
import time
import locale
from systems.renderSystem import RenderSystem
from systems.moveSystem import MoveSystem
from systems.explodeSystem import ExplodeSystem
from systems.portalSystem import PortalSystem

projectiles = [
    { "Position": (8, 7), "Char": "+", "Velocity": (0, 1), "Color": 3 },
    { "Position": (8, 6), "Char": "+", "Velocity": (0, 1), "Color": 2 },
    { "Position": (8, 5), "Char": "+", "Velocity": (0, 1), "Color": 1 },
    { "Position": (8, 4), "Char": "+", "Velocity": (0, 1), "Color": 5 },
    { "Position": (8, 3), "Char": "+", "Velocity": (0, 1), "Color": 4 },
    { "Position": (8, 2), "Char": "+", "Velocity": (0, 1), "Color": 3 },
    { "Position": (8, 1), "Char": "+", "Velocity": (0, 1), "Color": 2 },
    { "Position": (8, 0), "Char": "+", "Velocity": (0, 1), "Color": 1 }
]
movers = [
    { "Position": (8, 30), "Char": "↑", "Move": (-1, 0), "Color": 3 },
    { "Position": (30, 30), "Char": "→", "Move": (0, 1), "Color": 3 },
    { "Position": (30, 70), "Char": "↓", "Move": (1, 0), "Color": 3 },
    { "Position": (8, 70), "Char": "←", "Move": (0, -1), "Color": 3 }
]
exploders = [
    { "Position": (8, 15), "Char": "*", "Explode": "", "Color": 5 },
]
portals = [
    { "Position": (8, 25), "Char": "o", "Color": 4, "Portal": 1 },
    { "Position": (35, 85), "Char": "o", "Color": 4, "Portal": 0 }
]

FPS = 60

def main(stdscr):
    locale.setlocale(locale.LC_ALL, "")

    # Set up curses
    curses.curs_set(0) # hide cursor
    stdscr.nodelay(True) # Non-blocking getch()/getkey()
    stdscr.scrollok(True)

    # colors
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_MAGENTA)

    stdscr.bkgd(" ", curses.color_pair(1))

    # Initialize systems
    renderSystem = RenderSystem(stdscr, projectiles, movers, exploders, portals)
    moveSystem = MoveSystem(projectiles, movers)
    explodeSystem = ExplodeSystem(projectiles, exploders)
    portalSystem = PortalSystem(projectiles, portals)

    while True:
        # handle input
        try:
            key = stdscr.getkey()
            if key == "q" or key == "Q":
                stdscr.clear()
                break
        except Exception:
            key = None

        # animation and systems logic
        stdscr.erase()

        renderSystem.act()
        moveSystem.act()
        explodeSystem.act()
        portalSystem.act()

        stdscr.refresh()

        time.sleep(FPS/1000) # control animation speed


if __name__ == "__main__":
    # Main systems loop
    print("Starting up systems...")
    curses.wrapper(main)

