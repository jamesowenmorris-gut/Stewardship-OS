# Installing Stewardship OS

Welcome to the **Stewardship OS Pilot Program**. By installing this software, your home is becoming a Node in a resilient, decentralized energy mesh. 

This guide will walk you through the installation process. If you encounter any issues, please check the [Troubleshooting section](#troubleshooting) or reach out to the project coordinator.

## Prerequisites
Before starting, ensure you have the following:
* **A running Home Assistant instance:** (Version 2024.1 or newer recommended).
* **HACS (Home Assistant Community Store):** If you don't have it, [install HACS first](https://hacs.xyz/docs/setup/download/).

---

## Installation Steps

### 1. Add Stewardship OS to HACS
Stewardship OS is currently in its Pilot phase and is installed via HACS as a "Custom Repository."

1. Open your **Home Assistant** dashboard.
2. Click on **HACS** in the sidebar.
3. Click the **three dots** in the top right corner.
4. Select **Custom repositories**.
5. In the **Repository** field, paste this URL:
   `https://github.com/[YOUR_GITHUB_USERNAME]/stewardship-os`
6. In the **Category** dropdown, select **Integration**.
7. Click **Add**.

### 2. Download the Integration
1. Once the repository is added, a new card for "Stewardship OS" should appear in your HACS list (or you can search for it).
2. Click **Download**.
3. A confirmation dialog will appear. Click **Download** again.

### 3. Restart Home Assistant
For the system to recognize the new code, you must restart your Home Assistant instance:
1. Go to **Settings** > **System**.
2. Click the **Power icon** (top right) and select **Restart Home Assistant**.

### 4. Configure the Node
After the restart, we need to activate the "Brain" of the OS:
1. Go to **Settings** > **Devices & Services**.
2. Click **+ Add Integration** (bottom right).
3. Search for **Stewardship OS**.
4. Follow the on-screen prompts to register your Node.

---

## Verification
Once installed, a new entity named **"Stewardship Node State"** will be created. 
* If the state shows `STABLE`, your node is connected and the Constitution is active.
* If the state is `UNAVAILABLE`, please check your sensor connections.

## Troubleshooting
* **"Integration not found":** Ensure you clicked the "Restart" button after installing in HACS. Browsing the UI isn't enough; the core engine must be reloaded.
* **Permissions:** Ensure your Home Assistant user has administrative rights to add integrations.

---
*Built for the future of energy sovereignty. If you have questions about the Constitution or Mesh connectivity, please refer to the [ARCHITECTURE.md](/docs/ARCHITECTURE.md).*
