class MoveSystem:
    def __init__(self, projectiles, movers):
        self.projectiles = projectiles
        self.movers = movers

    def act(self):
        move_map = {}

        for mover in self.movers:
            if "Move" in mover:
                move_map[mover["Position"]] = mover

        for projectile in self.projectiles:
            position = projectile["Position"]
            if position in move_map:
                projectile["Velocity"] = move_map[position]["Move"]
                self.rotate(move_map[position])

    def rotate(self, mover):
        if mover["Char"] == "←":
            mover["Char"] = "↖"
            mover["Move"] = (-1, -1)
        elif mover["Char"] == "↖":
            mover["Char"] = "↑"
            mover["Move"] = (-1, 0)
        elif mover["Char"] == "↑":
            mover["Char"] = "↗"
            mover["Move"] = (-1, 1)
        elif mover["Char"] == "↗":
            mover["Char"] = "→"
            mover["Move"] = (0, 1)
        elif mover["Char"] == "→":
            mover["Char"] = "↘"
            mover["Move"] = (1, 1)
        elif mover["Char"] == "↘":
            mover["Char"] = "↓"
            mover["Move"] = (1, 0)
        elif mover["Char"] == "↓":
            mover["Char"] = "↙"
            mover["Move"] = (1, -1)
        elif mover["Char"] == "↙":
            mover["Char"] = "←"
            mover["Move"] = (0, -1)

