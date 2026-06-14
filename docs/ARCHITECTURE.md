# System Architecture: Stewardship OS

Stewardship OS is a custom Home Assistant integration designed to manage residential energy as a resilient, communal mesh. 

## 1. Core Principles (The Constitution)
* **Vitality:** Energy is prioritized for life-critical loads (heating, water, medical).
* **Reciprocity:** Local energy surpluses are shared with the immediate mesh before grid export.
* **Resilience:** Nodes must maintain self-sufficiency during grid instability.

## 2. High-Level Hierarchy
The system utilizes a modular, object-oriented approach within the Home Assistant framework:

* **Coordinator (`coordinator.py`):** The "Brain." Polls sensors, evaluates the current state against the Constitution, and manages state updates.
* **Sensors (`sensor.py`):** The "Eyes." Interfaces with physical hardware (Inverters, Shelly EM, etc.) to report real-time power metrics.
* **Switches (`switch.py`):** The "Hands." Executes load-shedding or islanding commands based on the Coordinator's decisions.
* **Config Flow (`config_flow.py`):** The "Gatekeeper." Handles onboarding and node-identification.

## 3. Data Flow
1.  **Ingestion:** Sensors poll local hardware every 30 seconds.
2.  **Analysis:** The `Coordinator` evaluates data against grid conditions (price, frequency, local mesh demand).
3.  **Governance:** The `Coordinator` selects an operational mode (STABLE, CONSERVATION, ISLAND).
4.  **Action:** The system updates relevant switches and binary sensors.

## 4. Node-to-Node Communication (The Mesh)
*Future Implementation:* Nodes communicate via a local MQTT broker. 
* **Discovery:** Nodes broadcast their "Capacity-Available" status.
* **Negotiation:** If a node is in a "High-Demand" state, it requests surplus energy from the nearest "High-Capacity" node.

## 5. Security Model
* **Local-First:** No sensitive data leaves the local network. 
* **Secrets:** API keys and credentials are never stored in the code; they are managed via Home Assistant's `secrets.yaml`.
* **Air-Gapped Potential:** The system is designed to function fully even if the external Internet connection is severed.

## 6. Directory Structure
```text
/custom_components/stewardship
├── __init__.py        # Integration entry point
├── coordinator.py     # Main logic engine
├── sensor.py          # Entity definition
├── switch.py          # Load management logic
├── config_flow.py     # Setup wizard
└── manifest.json      # Dependencies and metadata
```
