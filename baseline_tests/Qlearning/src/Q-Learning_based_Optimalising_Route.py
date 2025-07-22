# ##  Q-learning Summary

# - **State**: Vehicle’s current location (junction ID)
# - **Action**: Selection of next road segment
# - **Reward**: Negative of delay + route efficiency heuristics
# - **Exploration**: ε-greedy strategy
# - **Learning**: On-policy, tabular update loop (Q-table)



import traci
import numpy as np
import random
import os
import sys
import json
from sumolib.net import readNet
import matplotlib.pyplot as plt  # For visualizing the Q-table
import networkx as nx

# Q-learning parameters
alpha = 0.1       # Learning rate
gamma = 0.9       # Discount factor
epsilon = 0.2     # Exploration rate
episode = 1       # Number of episodes

destination_edge = 'E19'  # Destination edge in the network
start_edge = 'E0'         # Starting edge in the network

# DuaRouter path and network configurations
duarouter_path = r'"C:\Program Files (x86)\Eclipse\Sumo\bin\duarouter"'  # Path to the DuaRouter executable
network_file = "osm.net.xml"  # Path to the network file
demand_file = "osm.demand.xml"  # Path to the demand file
output_route_file = "generated_routes.rou.xml"  # Output route file

# Initialize Q-table as an empty dictionary
q_table = {}

# Start SUMO simulation
def start_simulation():
    traci.start(["sumo", "-c", "osm.sumocfg", "--no-warnings", "--no-step-log"])

# Reward function for Q-learning
def get_reward(current_edge, next_edge, waiting_time):
    # If the next edge is the destination, reward the agent positively
    if next_edge == destination_edge:
        return 1  
    # If the next edge is congested, assign a large penalty
    elif traci.edge.getLastStepVehicleNumber(next_edge) > 0:
        return -100  
    else:
        # Calculate a penalty proportional to the waiting time
        waiting_time_penalty = waiting_time
        return -10 * waiting_time  

# Load the SUMO network file
net = readNet(network_file)

# Generate routes using cached data or create new ones with DuaRouter
def generate_routes_cached():
    os.system(f"{duarouter_path} -n {network_file} --additional-files {demand_file} -o {output_route_file}")

# Update Q-table using the Q-learning formula
def update_q_table(current_edge, action, reward, next_edge):
    if current_edge not in q_table:
        q_table[current_edge] = []
    while len(q_table[current_edge]) <= action:
        q_table[current_edge].append(0)
    q_table[current_edge][action] += alpha * (reward + gamma * max(q_table.get(next_edge, [0])) - q_table[current_edge][action])

# Get a random next edge from the current edge
def get_random_next_edge(current_edge):
    lane_count = traci.edge.getLaneNumber(current_edge)  # Number of lanes on the current edge
    next_edges = []

    # Retrieve outgoing links for each lane of the current edge
    for lane_index in range(lane_count):
        lane_id = f"{current_edge}_{lane_index}"  # Lane ID format: 'edgeID_laneIndex'
        outgoing_links = traci.lane.getLinks(lane_id)
        
        # Add the target edge IDs of the outgoing links to the list
        for link in outgoing_links:
            next_edge = traci.lane.getEdgeID(link[0])  
            next_edges.append(next_edge)
    
    # Remove duplicates and choose a random next edge
    next_edges = list(set(next_edges))
    if next_edges:
        return random.choice(next_edges)
    return None  # No outgoing edges available

# Calculate the optimal route using the Q-table
def get_optimal_route(start_edge):
    current_edge = start_edge
    optimal_route = [current_edge]

    while current_edge != destination_edge:
        if current_edge not in q_table or not q_table[current_edge]:
            break

        # Find the next edge with the highest Q-value
        lane_count = traci.edge.getLaneNumber(current_edge)
        best_next_edge = None
        best_q_value = float('-inf')

        for lane_index in range(lane_count):
            lane_id = f"{current_edge}_{lane_index}"
            outgoing_links = traci.lane.getLinks(lane_id)

            for link in outgoing_links:
                next_edge = traci.lane.getEdgeID(link[0])
                if next_edge in q_table:
                    q_value = q_table[next_edge][0]
                    if q_value > best_q_value:
                        best_q_value = q_value
                        best_next_edge = next_edge

        if best_next_edge is None:
            break

        optimal_route.append(best_next_edge)
        current_edge = best_next_edge

    if optimal_route[-1] != destination_edge:
        optimal_route.append(destination_edge)
    
    return optimal_route

# Main function for executing Q-learning and simulation
def main():
    # Initialize SUMO simulation
    current_step = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    start_simulation()
    for _ in range(current_step):
        traci.simulationStep()

    global epsilon  # Allow modification of epsilon during training

    for episode in range(100):
        generate_routes_cached()

        # Add a new vehicle for this episode
        vehicle_id = f"vehicle_{episode}"
        traci.vehicle.add(vehicle_id, "r_0")
        traci.vehicle.setRoute(vehicle_id, ["E0"])  # Start route from "E0"
        
        current_edge = "E0"
        route_taken = [current_edge]

        while current_edge != destination_edge:
            traci.simulationStep()
            lane_count = traci.edge.getLaneNumber(current_edge)

            # Exploration vs exploitation decision
            if random.uniform(0, 1) < epsilon:
                next_edge = get_random_next_edge(current_edge)
                action = 0  
            else:
                action = np.argmax(q_table.get(current_edge, [0] * lane_count))
                next_edge = get_random_next_edge(current_edge) if lane_count > 0 else None

            if next_edge is None:  # No valid next edge
                break
            waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
            reward = get_reward(current_edge, next_edge, waiting_time)
            update_q_table(current_edge, action, reward, next_edge)

            route_taken.append(next_edge)
            current_edge = next_edge

        if vehicle_id in traci.vehicle.getIDList():
            traci.vehicle.remove(vehicle_id)

        epsilon = max(0.1, epsilon * 0.99)

    optimal_route = get_optimal_route(start_edge)
    print(json.dumps(optimal_route))
    traci.close()  # Close SUMO connection

if __name__ == "__main__":
    if len(sys.argv) > 2: # For socket programming
        start_edge = sys.argv[1]
        destination_edge = sys.argv[2]
        current_step = int(float(sys.argv[3])) if len(sys.argv) > 3 else 0
        current_step = current_step + 500
        print(f"Starting simulation from step {current_step}")
    main()
