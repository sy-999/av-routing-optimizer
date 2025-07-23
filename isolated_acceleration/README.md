#  Experiment 2: FPGA vs CPU Acceleration

##  Test Setup

* **CPU**: Intel Core i3
* **FPGA**: Xilinx PYNQ-Z1 (Zynq-7000 SoC)
* **Task**: 100,000 Q-value updates for reinforcement learning routing agent
* **Implementations**:

  * CPU: Python
  * FPGA: C++ with hardware-level parallelism using Programmable Logic (PL)

##  Performance Result

* CPU: 0.0767946243 seconds/ FPGA: 0.0010335 seconds
*  **FPGA achieved 74.3× faster execution** than CPU
*  Latency improvement significantly boosts feasibility for real-time decision-making in autonomous systems

##  Interpretation

The FPGA-based implementation offloads time-critical Q-table updates from the CPU to the Programmable Logic block. By leveraging hardware parallelism, the system dramatically reduces processing time, which is critical in scenarios where routing decisions must reflect current traffic conditions.

## Key Takeaways

*  Offloading to FPGA removes Python-level bottlenecks
*  Hardware acceleration makes real-time adaptation possible
*  Ideal for MEC environments requiring ultra-low latency

