class ExplodeSystem:
    def __init__(self, projectiles, exploders):
        self.projectiles = projectiles
        self.exploders = exploders

    def act(self):
        explode_map = {}
        has_exploded = {}
        position_deltas = [
            (1, 1),
            (1, 0),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        for exploder in self.exploders:
            if "Explode" in exploder:
                explode_map[exploder["Position"]] = exploder
                has_exploded[exploder["Position"]] = False
        
        for projectile in self.projectiles:
            to_extend = []

            if projectile["Position"] in explode_map and not has_exploded[projectile["Position"]]:
                has_exploded[projectile["Position"]] = True
                for delta in position_deltas:
                    newEntity = dict(projectile)
                    newEntity["Position"] = (projectile["Position"][0] + delta[0], projectile["Position"][1] + delta[1])
                    newEntity["Velocity"] = delta
                    
                    color = 1
                    if "Color" in newEntity:
                        color = self.rotateColor(newEntity["Color"])
                    newEntity["Color"] = color

                    to_extend.append(newEntity)

            self.projectiles.extend(to_extend)

    def rotateColor(self, color):
        newColor = color + 1
        if newColor > 5:
            newColor = 0
        return newColor
