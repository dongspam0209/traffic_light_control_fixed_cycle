# Fixed cycle traffic simulation about an intersection with SUMO
Guide for the simulation
- Generate cars in Normal distribution. (25% in left turn only lane, 75% in straight and turn right lane)
- the cycle of the traffic is - NS: Green(15s) -> Yellow(2s) -> NS leftonly(5s) : Green -> Yellow -> EW: Green -> Yellow -> EW leftonly : Green -> Yellow

# generator.py
generate cross.rou.xml (cars)

# util.py
contains sumo command to run the simulation.
