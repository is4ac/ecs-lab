# ECS Lab

This is an experiment to implement an Entity Component System (ECS) architecture using Python and `curses`. Please don't mind the poor system design choices, etc, as I am mostly figuring things out as I go and this is meant to be a proof-of-concept.

If things go well, I hope to turn this into a game eventually.

## To develop and run

Just run `main.py` as you typically would.

**NOTE**: Because the `curses` library is not supported by Windows, if you are a Windows user, first install `windows-curses` before running. E.g. `pip install windows-curses`. Alternatively, go use Linux or MacOS 😉.

## Current entity / tile types

**Projectiles**: These are the basic entities that move around the screen. They can be represented using any character.

**Movers**: These are arrows that redirect the projectiles to move in a different direction when they run into them.

**Exploders**: When a projectile hits an exploder, it causes a copy of the projectile to "explode" out in all 8 directions (and change colors).

**Portals**: When a projectile runs into a portal, it teleports to the connected portal while maintaining the same velocity.

And hopefully many more to come!
