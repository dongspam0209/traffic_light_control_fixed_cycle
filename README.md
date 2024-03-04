# Fixed cycle traffic simulation about an intersection with SUMO
Guide for the simulation
- Generate cars in Normal distribution. (25% in left turn only lane, 75% in straight and turn right lane)
- the cycle of the traffic is - NS: Green(15s) -> Yellow(2s) -> NS leftonly(5s) : Green -> Yellow -> EW: Green -> Yellow -> EW leftonly : Green -> Yellow


![image](https://github.com/dongspam0209/traffic_light_control_fixed_cycle/assets/98256216/ce78e9ff-f0f4-4d77-8967-7bc1c8565509) ![image](https://github.com/dongspam0209/traffic_light_control_fixed_cycle/assets/98256216/3865441a-f6c4-4c66-9f9a-1d8ccf270268) ![image](https://github.com/dongspam0209/traffic_light_control_fixed_cycle/assets/98256216/3043a18d-cae2-4efc-a6c8-afc3a635711a) ![image](https://github.com/dongspam0209/traffic_light_control_fixed_cycle/assets/98256216/ae0b68cf-bb56-4d4e-8157-1391e878ed8e) ![image](https://github.com/dongspam0209/traffic_light_control_fixed_cycle/assets/98256216/b4ea1970-15ce-491b-99e0-3c7817331d16)





# generator.py
generate cross.rou.xml (cars)

# util.py
contains sumo command to run the simulation.
