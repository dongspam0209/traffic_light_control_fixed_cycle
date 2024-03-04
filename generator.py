
import numpy as np
import math

class CarGenerator:
    def __init__(self, max_steps, n_cars_generated):
        self._n_cars_generated = n_cars_generated  # 한 에피소드당 생성할 차량 수
        self._max_steps = max_steps  # 최대 시뮬레이션 스텝

    def generate_car(self, seed):
        np.random.seed(seed)
        
        # car information list
        vehicles_info = []

        # car route (start_to_end)
        route_ids_straight_right = ["W_to_E", "W_to_S", "N_to_W", "N_to_S", "E_to_W", "E_to_N", "S_to_N", "S_to_E"]
        route_ids_left=["W_to_N", "N_to_E" , "E_to_S" , "S_to_W"]
        # car generation distribution : normal distribution
        # limit of car generation timing 300~3000
        mu,sigma=1800,600
        

        for i in range(self._n_cars_generated):
            car_id = f"vehicle_{i}"
            # route_id = np.random.choice(route_ids)
            straight_or_left_switch=np.random.uniform()
            if(straight_or_left_switch<0.75):
                route_id=np.random.choice(route_ids_straight_right)
            else:
                route_id=np.random.choice(route_ids_left)
            depart=np.random.normal(mu,sigma)
            depart=np.rint(depart)
            depart=np.clip(depart,300,3000)

            vehicles_info.append((depart, car_id, route_id))

        # 출발 시간에 따라 차량 정보 정렬
        vehicles_info.sort()

        # .rou.xml 파일에 차량 정보 기록
        with open("./intersection/cross.rou.xml", "w") as routes:
            print("""                
<routes>
            <vType accel="1.0" decel="4.5" id="standard_car" length="5.0" minGap="2.5" maxSpeed="25" sigma="0.5" laneChangeMode="5242898"/>
            
            <!-- route definition (the car route) -->

            <route id="W_to_N" edges="W_in N_out"/>
            <route id="W_to_E" edges="W_in E_out"/>
            <route id="W_to_S" edges="W_in S_out"/>
            <route id="N_to_W" edges="N_in W_out"/>
            <route id="N_to_E" edges="N_in E_out"/>
            <route id="N_to_S" edges="N_in S_out"/>
            <route id="E_to_W" edges="E_in W_out"/>
            <route id="E_to_N" edges="E_in N_out"/>
            <route id="E_to_S" edges="E_in S_out"/>
            <route id="S_to_W" edges="S_in W_out"/>
            <route id="S_to_N" edges="S_in N_out"/>
            <route id="S_to_E" edges="S_in E_out"/>""",file=routes)

            for depart, car_id, route_id in vehicles_info:
                print(f'    <vehicle id="{car_id}" type="standard_car" route="{route_id}" depart="{depart}" departLane="random" departSpeed="10" laneChangeMode="5242898" />' , file=routes)

            print("</routes>", file=routes)


