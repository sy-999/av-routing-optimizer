# Latency Optimization in Autonomous Vehicle Routing using MEC, FPGA and Reinforcement Learning

This project proposes a latency-optimized routing system for autonomous vehicles using **Q-learning**, simulated with **SUMO**, and accelerated through **hardware implementation on FPGA**. The system is tested under various configurations including **CPU-only**, **Raspberry Pi**, and **FPGA-based partial acceleration**.

>  Developed as part of MSc dissertation in Advanced Microelectronic Systems Engineering at the University of Bristol.

---

##  Overview

Autonomous Vehicles (AVs) require real-time, adaptive decision-making in dynamic environments. This project investigates a modular AV routing framework with three goals:

1. Minimize latency in path planning using hardware acceleration (FPGA)
2. Apply online learning (Q-learning) to simulate dynamic urban traffic
3. Evaluate comparative performance across CPU, edge device (Raspberry Pi), and FPGA-based compute setups

---

##  Core Technologies

| Component        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| SUMO             | Traffic simulator used for modeling a custom 4x4 intersection grid           |
| TraCI            | Interface for real-time control of SUMO vehicles via Python                 |
| Q-learning       | Lightweight reinforcement learning algorithm for route planning             |
| Raspberry Pi     | Edge computing platform for CPU-based baseline testing                      |
| FPGA (PYNQ-Z1)   | Hardware acceleration of key RL function via programmable logic             |

---

##  Repository Structure
```
📁 av-routing-optimizer/
├── baseline_tests/                  # Q-learning vs Fixed vs Dijkstra comparison
│   ├── Qlearning/
│   ├── Fixed/
│   ├── Dijkstra/
│   └── README.md         ← Summary of Results – Experiment 1
├── isolated_acceleration/          # Standalone CPU vs FPGA benchmark
│   ├── CPU/
│   ├── FPGA/
│   └── README.md         ← Summary of Results – Experiment 3
├── core_system/                    # MEC architecture combining Raspberry Pi, CPU, FPGA
│   ├── CPU/
│   ├── FPGA/
│   └── RaspberryPi/
├── matlab_tools/                   # Scripts for result visualization
└── README.md            ← Overview of the main repository and links to result summaries

```


---

##  Simulation Workflow

### 1. Traffic Environment
- A custom 4x4 grid network (16 junctions) was designed and modeled in SUMO using .net.xml.
- Background traffic is defined statically in .rou.xml but designed to change over time, simulating dynamic congestion patterns across different time intervals.
- This time-varying flow introduces non-uniform and evolving traffic bottlenecks, providing a more realistic environment for testing the RL agent’s adaptability.
  
### 2. RL Vehicle Behavior
- A reinforcement learning-controlled vehicle is dynamically inserted during simulation runtime via **TraCI**.
- The vehicle starts with no route and selects its path based on a learned Q-table.

### 3. Learning & Routing
- The vehicle updates its Q-values in each episode based on:
  - State: current junction
  - Action: selection of next outgoing edge
  - Reward: penalizing delay and congestion, encouraging fast, efficient travel

### 4. Real-Time TraCI Control
- At every simulation step, the chosen action is reflected in the simulation via TraCI.
- The learning loop runs concurrently with vehicle control.

---

##  Evaluation & Results

Three configurations were tested:

### 1. **CPU-only (Local PC)**
- Q-learning runs entirely in Python
- Fastest processing but not scalable to edge scenarios

### 2. **Raspberry Pi + CPU (Edge Split)**
-SUMO simulation runs on the Raspberry Pi, while the Q-learning algorithm runs on an external CPU.
-The CPU computes the path and returns it, which is then applied to the vehicle.

### 3. **CPU vs FPGA Comparison**
- A single **RL function (Q-value update logic)** was implemented both in CPU (Python) and in FPGA (PYNQ-Z1)
- Due to the complexity of implementing arithmetic operations (many inputs/outputs) in PL within deadline constraints, **a full MEC architecture was not realized**
- Partial acceleration confirmed potential, but also highlighted integration challenges (PL-PS interface and synchronization bottlenecks)

---

## Performances and Results

### 1.**CPU-only (Local PC)** : Q-learning vs Fixed vs Dijkstra(SUMO Default)

| Method       | Travel Time (s) | Route Length (m) | Time Loss (s) | CO₂ Emission (mg) | Fuel Consumption (mg) |
| ------------ | --------------- | ---------------- | ------------- | ----------------- | --------------------- |
| Fixed Route  | 108.45          | 640.57           | 61.88         | 285,814.45        | 91,388.18             |
| SUMO Default | 66.85           | 639.05           | 19.82         | 229,388.18        | 73,164.46             |
| Q-Learning   | 63.75           | 637.76           | 14.14         | 217,308.11        | 69,311.40             |

- Folder: `baseline_tests`
- Subdirectories contain raw data (`data/`), simulation outputs (`results/`), and source code (`src/`).
- ✅ Q-learning outperformed both Fixed and SUMO Default methods, achieving the shortest travel time, lowest time loss, and reduced CO₂ and fuel consumption.


### 2.**Raspberry Pi + CPU (Edge Split): CPU-only vs Raspberry Pi + CPU (Q-learning Comparison)**


| Setup                   | Travel Time (s) | Route Length (m) | Time Loss (s) |
| ----------------------- | --------------- | ---------------- | ------------- |
| **CPU-only (Local PC)** | 63.75           | 637.76           | 14.14         |
| **Raspberry Pi + CPU**  | 68.45           | 638.62           | 19.03         |


- Folder: `core_system`
- ✅ The Raspberry Pi setup adds slight delay due to communication latency with the external CPU, simulating a realistic MEC offloading scenario.



### 3. **CPU vs FPGA Comparison  – Q-value Update Performance**


| Metric                           |       CPU (Python)	  |   FPGA (C++ / PL)   |
| ------------------------------ | ----------------------- | --------------------- |
| **Execution Time (100K ops)**  |      0.0768 sec      |	  0.0010 sec     |
| **Speedup	**	 |             –              |       ×74.3 faster     |   

* Folder: `isolated_acceleration` 
✅ FPGA dramatically accelerates Q-table updates via hardware parallelism, Suitable for real-time decision-making in latency-critical AV routing.



---

##  Limitations

- MEC framework remains **partially implemented** due to time/resource constraints in FPGA design
- Q-learning is scalable for small environments, but not ideal for high-dimensional traffic networks
- Current evaluation does not include multi-agent interactions or V2X communication

---

##  Future Work

- **Complete FPGA-based Q-learning core**:
  - Finish arithmetic design in PL and Optimize PL-PS interfacing for full Q-table management
  - Integrate into full MEC pipeline with real-time inference loop
- **Upgrade learning agent**:
  - Replace Q-learning with **Deep Q-Networks (DQN)** or more scalable ML models

---

📚 Reference
Sooyeon Kim (2024). Latency Optimization in Autonomous Vehicle Routing Using MEC, FPGA, and Reinforcement Learning. MSc Dissertation, University of Bristol.

📩 Contact
Sooyeon Kim
sienna_6562@gmail.com



