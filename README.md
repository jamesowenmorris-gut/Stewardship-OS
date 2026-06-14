# Stewardship OS

**An autonomous, decentralized energy operating system.**

**Stewardship OS** is the foundational software for the **Project Convergence** initiative. It transforms residential energy infrastructure into a resilient, self-balancing, and communal mesh. By running Stewardship OS, your home becomes a "Node"—capable of autonomous load-balancing, grid-islanding, and local energy sharing.

## The Mission
To transition the national grid from an extraction-based commodity model to a resilience-based communal mesh. We believe that energy is a fundamental right, and the infrastructure to manage it should be open, local, and sovereign.

## The Constitution
The Stewardship OS logic is governed by three immutable pillars:
1.  **VITALITY:** Life-critical systems (heating, medical, water preservation) always take priority.
2.  **RECIPROCITY:** Energy is a shared, local resource. Surplus power is offered to immediate neighbors before being pushed to the national grid.
3.  **RESILIENCE:** When the national grid fails, the Mesh decouples, forms its own frequency, and maintains local stability.

## Getting Started
Stewardship OS is built as a custom integration for [Home Assistant](https://www.home-assistant.io/).

### Prerequisites
* A running Home Assistant instance (latest version recommended).
* [HACS (Home Assistant Community Store)](https://hacs.xyz/) installed.

### Installation
1.  Open **HACS** in your Home Assistant sidebar.
2.  Click the three dots in the top right and select **Custom Repositories**.
3.  Paste the URL of this repository and select **Integration** as the category.
4.  Restart Home Assistant.
5.  Navigate to **Settings > Integrations > Add Integration** and search for "Stewardship OS."

## Architecture Overview
Stewardship OS uses a local-first, peer-to-peer communication model. It consists of:
* **The Coordinator:** Manages the logic engine (Constitution enforcement).
* **The Sensors:** Interfaces with local inverters, batteries, and grid meters.
* **The Mesh Protocol:** Enables nodes to communicate capacity availability to neighbors.

*For a detailed technical deep-dive, see [ARCHITECTURE.md](/docs/ARCHITECTURE.md).*

## Roadmap
We are currently in **Phase 1: Pilot**.
* **Status:** Active data sanitization (Exo-Correlation) and Alpha-Node recruitment.
* **Goal:** Establish 5 functional, autonomous Nodes in the Cardiff-Bristol corridor.

## Contributing
This project is licensed under **AGPLv3**. We welcome code contributions, logic improvements, and hardware integrations. 
* **Before contributing:** Please review the [CONSTITUTION.md](/docs/CONSTITUTION.md) to ensure your changes align with the project's core principles.
* **Submitting:** Open a Pull Request with a clear description of the impact on mesh stability.

---
*Built for the future of energy sovereignty.*
