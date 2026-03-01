class PortalSystem:
    def __init__(self, projectiles, portals):
        self.projectiles = projectiles
        self.portals = portals

    def act(self):
        portalMap = {}
        for portal in self.portals:
            portalMap[portal["Position"]] = portal

        for projectile in self.projectiles:
            if projectile["Position"] in portalMap:
                portalFrom = portalMap[projectile["Position"]]
                portalTo = self.portals[portalFrom["Portal"]]
                projectile["Position"] = portalTo["Position"]

