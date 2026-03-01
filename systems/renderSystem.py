import curses

class RenderSystem:
    def __init__(self, window, projectiles, movers, exploders, portals):
        self.window = window
        self.projectiles = projectiles
        self.movers = movers
        self.exploders = exploders
        self.portals = portals

    def act(self):
        entities = self.projectiles + self.movers + self.exploders + self.portals
        for entity in entities:
            color = 1
            if "Color" in entity:
                color = entity["Color"]

            try:
                self.window.addstr(entity["Position"][0], entity["Position"][1], entity["Char"], curses.color_pair(color))
            except Exception:
                pass

            # Update position based on velocity if it exists
            if "Velocity" in entity:
                position_list = list(entity["Position"])

                position_list[0] += entity["Velocity"][0]
                if curses.LINES <= position_list[0]:
                    position_list[0] = 0
                elif position_list[0] < 0:
                    position_list[0] = curses.LINES - 1

                position_list[1] += entity["Velocity"][1]
                if curses.COLS <= position_list[1]:
                    position_list[1] = 0
                elif position_list[1] < 0:
                    position_list[1] = curses.COLS - 1

                entity["Position"] = tuple(position_list)

