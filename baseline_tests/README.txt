#  Experiment 1: Routing Algorithm Comparison (Q-Learning vs SUMO vs Fixed)

##  Simulation Environment

* Simulator: SUMO (Simulation of Urban MObility)
* Topology: 4×4 grid (16 junctions, 40 segments)
* Routing methods:

  * **Fixed Route** – statically assigned, no adaptation
  * **SUMO Default** – dynamic Dijkstra-based rerouting
  * **Q-Learning** – RL agent operating via MEC server

##  Performance Metrics

| Method       | Travel Time (s) | Route Length (m) | Time Loss (s) | CO₂ Emission (mg) | Fuel Consumption (mg) |
| ------------ | --------------- | ---------------- | ------------- | ----------------- | --------------------- |
| Fixed Route  | 108.45          | 640.57           | 61.88         | 285,814.45        | 91,388.18             |
| SUMO Default | 66.85           | 639.05           | 19.82         | 229,388.18        | 73,164.46             |
| Q-Learning   | 63.75           | 637.76           | 14.14         | 217,308.11        | 69,311.40             |

##  Interpretation

* **Q-Learning** outperformed both baseline strategies in all major metrics.
* Latency and time loss were significantly reduced, indicating superior congestion avoidance.
* Environmental impact (CO₂ and fuel) was also lowered due to more efficient pathing.

## Key Takeaways

*  \~1.7× faster than Fixed Route
*  \~4.4× lower time loss
*  \~1.3× reduction in emissions and fuel usage

##  File Reference

* Folder: `baseline_tests`
* Subdirectories contain raw data (`data/`), simulation outputs (`results/`), and source code (`src/`).
