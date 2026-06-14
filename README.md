# Stewardship OS

**Decentralized Energy Governance for Home Assistant.**

Stewardship OS transforms your home into a resilient, autonomous energy node. It is a Home Assistant integration designed to prioritize life-critical loads, enable energy reciprocity with your neighbors, and maintain grid independence during instability.

---

## The Constitution
Stewardship OS is built on three immutable principles:
1. **Vitality:** Energy is prioritized for life-critical loads (heating, water, medical).
2. **Reciprocity:** Local energy surpluses are shared with the immediate mesh before grid export.
3. **Resilience:** Nodes must maintain self-sufficiency during grid instability.

---

## Current Status: Pilot Phase
We are currently in the **Alpha Pilot Phase (2026)**, focusing on 5 households in the Cardiff/Bristol region. 
*   **Goal:** To establish the first local "Mesh" of energy-aware nodes.
*   **Status:** [Active Development]

---

## Features
*   **The Brain (`coordinator.py`):** An intelligent polling engine that evaluates energy usage against the Constitution.
*   **The Eyes (`sensor.py`):** Real-time monitoring of solar generation, battery levels, and grid status.
*   **The Hands (`switch.py`):** Automated load-shedding to preserve power for critical circuits.
*   **Mesh Ready:** Built with future-proof MQTT architecture for node-to-node communication.

---

## Installation

### Prerequisites
*   A running [Home Assistant](https://www.home-assistant.io/) instance.
*   [HACS](https://hacs.xyz/) (Home Assistant Community Store) installed.

### Steps
1.  Open HACS in Home Assistant.
2.  Click the three dots in the top right corner and select **Custom repositories**.
3.  Add the URL: `https://github.com/jamesowenmorris-gut/Stewardship-OS`
4.  Select **Integration** as the category and click **Add**.
5.  Click **Download** and restart Home Assistant.
6.  Configure via **Settings > Devices & Services > Add Integration > Stewardship OS**.

---

## Contributing
We welcome contributors who are passionate about energy sovereignty and decentralized systems. Please read our [CONTRIBUTING.md](docs/CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the AGPLv3 License - see the [LICENSE](LICENSE) file for details.
