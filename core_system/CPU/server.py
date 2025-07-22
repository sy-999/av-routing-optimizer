import os
import traci
import socket
import json
import time
import subprocess
# Variable to track the current step
current_step = 0
vehicle_numbers = 0

def run_optimal_route(start_edge, destination_edge, step):
    """
    Execute Optimal_Route.py and return the result.

    :param start_edge: Departing edge
    :param destination_edge: Destination edge
    :param step: Current simulation step
    """
    
    process = subprocess.Popen(
        ['python', 'Optimal_Route.py', start_edge, destination_edge, str(int(current_step))],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output, error = process.communicate()


    # Parse the execution result of the Python script
    output_lines = output.decode().strip().splitlines()
    if output_lines:
        optimal_route_json = output_lines[-1]  # The last line contains the optimised route in JSON format
        print(f"Final Optimal Route is : {optimal_route_json}")
        return optimal_route_json
    else:
        print("No output from Optimal_Route.py")
        print("Error Output:", error.decode())  # Print errors for debugging
        return None

# Configure and start the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(1)
print("Waiting for connection...")

while True:
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    # Receive the request from the client
    data = conn.recv(1024)
    if not data:
        break

    # Parse the request
    request = json.loads(data.decode())
    start_edge = request.get("start_edge")
    destination_edge = request.get("destination_edge")
    current_step = request.get("current_step")
    print(f"Received reques : Vehicle number V_{vehicle_numbers}, start_edge={start_edge}, destination_edge={destination_edge}, current_step={current_step}")
 
    print(f"Q-learning executed at step {int(current_step) + 100} to account for processing delay.")
    vehicle_numbers = vehicle_numbers+1

    # Calculate the optimal route
    optimal_route = run_optimal_route(start_edge, destination_edge, current_step)
    if optimal_route:
        conn.sendall(optimal_route.encode())  # Respond in JSON format
    else:
        conn.sendall(b'{"error": "No optimal route found"}')

    conn.close()
