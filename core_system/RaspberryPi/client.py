import os
import traci
import socket
import json
import time
import threading
import queue

optimal_route_queue = queue.Queue()  # 서버에서 받은 최적 경로를 저장할 큐
count = 0
request_in_progress = False  # 현재 최적 경로 요청이 진행 중인지 여부를 나타내는 플래그
current_step = 0  # 현재 시뮬레이션 스텝

def request_optimal_route(start_edge, destination_edge, step):
    """서버에 최적 경로를 요청하는 함수"""
    global request_in_progress  # 플래그를 업데이트하기 위해 전역으로 설정
    try:
        print("1. Attempting to connect to server...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('172.20.10.2', 8080))  # 서버 IP와 포트에 연결
        client_socket.settimeout(5)  # 타임아웃 설정
        print("2. Connected to server.")

        # 서버에 요청 전송
        request = json.dumps({"start_edge": start_edge, "destination_edge": destination_edge, "current_step": step})
        client_socket.sendall(request.encode())
        print("3. Request sent to server.")

        response = None
        while response is None:
            try:
                data = client_socket.recv(1024)

                if not data:
                    print("4. No data received, waiting...")
                    time.sleep(1)
                    continue  # 데이터가 없으면 루프를 계속해서 반복
                
                # 정상적으로 데이터를 받은 경우 처리
                print("5. Data received")
                try:              
                    response = json.loads(data.decode())
                    print("6. Response received from server.")
                    optimal_route_queue.put(response)  # 큐에 최적 경로 추가                
                except json.JSONDecodeError:
                    print("Error decoding JSON response from server.")                  
                    response = None
            except socket.timeout:
                print("7. No response from server, retrying...")
                time.sleep(1)
            except Exception as e:
                print(f"Error receiving data: {e}")
                break  # 오류 발생 시 루프 종료

        client_socket.close()
    
    except Exception as e:
        print(f"Connection failed: {e}. Retrying in 5 seconds...")
        time.sleep(5)  # 재시도하기 전 대기
    
    # 요청 완료 후 플래그를 해제
    request_in_progress = False

def initiate_route_request(start_edge, destination_edge, step):
    """새로운 최적 경로 요청을 위한 쓰레드 시작"""
    global request_in_progress
    if not request_in_progress:  # 요청이 진행 중이 아닐 때만 새 요청 시작
        request_in_progress = True
        request_thread = threading.Thread(target=request_optimal_route, args=(start_edge, destination_edge, int(step)))
        request_thread.start()

# 시뮬레이션 초기 설정  "--vehroute-output","vehicle_routes_q.xml", "--emission-output", "vehicle_emission_q.xml", 
try:
    print("Starting SUMO simulation...")
    traci.start(["sumo-gui", "-c", "osm.sumocfg","--tripinfo-output", "tripinfo-output_q.xml", "--no-warnings", "--no-step-log"])

    # 시뮬레이션 실행
    while True:
        traci.simulationStep()
        
        # 최적 경로가 준비되면 큐에서 꺼내어 차량 추가
        if not optimal_route_queue.empty():           
            optimal_route = optimal_route_queue.get()
            vehicle_id = f"V_{count}"
            traci.route.add(f"optimal_route_{count}", optimal_route)  # 각 경로 ID가 고유하도록 수정
            traci.vehicle.add(vehicle_id, routeID=f"optimal_route_{count}")
            print(f"Vehicle {vehicle_id} added with optimal route: {optimal_route}")                    
            count += 1

        # 조건에 따라 새로운 최적 경로 요청
        if count < 21 and optimal_route_queue.empty():  # 요청이 없을 때에만 새로운 요청을 시작
            start_edge = "E0"
            destination_edge = "E19"
            step = traci.simulation.getTime()
            initiate_route_request(start_edge, destination_edge, step)  # 비동기 요청을 시작
        if count==21:
            traci.close()
            
except Exception as e:
    print(f"Error in SUMO simulation: {e}")



