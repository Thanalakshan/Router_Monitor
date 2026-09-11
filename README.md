# Huawei B312-926 Router Live Dashboard

A lightweight, client-side web dashboard for monitoring real-time download/upload speeds and session-based data usage for the **Huawei B312-926 4G LTE Router** directly from Microsoft Edge.

---

## Features

* **Real-time Speed Monitoring:** Displays live upload and download speeds updated every 2 seconds.
* **Session Usage Tracker:** Measures exact data consumed (in MB/GB) starting from the moment the tab is opened.
* **Jitter-Free Edge Tab Title:** Smooth 1-second clock timer showing tab open duration alongside upload and download speeds (`00:00:00 - 0 KB/s : 0 KB/s`).
* **Zero Overhead:** Runs entirely in the browser without Node.js, administrative privileges, or local server setups.

---

## Prerequisites & Setup

Due to browser Cross-Origin Resource Sharing (CORS) security policies, direct API calls to your router gateway (`192.168.8.1`) from local files require a browser extension to bypass origin blocks.

### Step 1: Install & Enable "Allow CORS" Extension

1. Open Microsoft Edge and navigate to the extension page:
   * [Allow CORS: Access-Control-Allow-Origin Extension](https://microsoftedge.microsoft.com/addons/detail/bhjepjpgngghppolkjdhckmnfphffdag)
2. Click **Get** to install the extension in Edge.
3. Once installed, click the **Allow CORS** extension icon in your browser toolbar to toggle it **ON** (the icon will light up when active).

---

## Auto-Launch Dashboard with Microsoft Edge

You can configure Microsoft Edge to automatically open your `router.html` dashboard in the background whenever the browser starts up, while directing you straight to a clean New Tab for regular browsing.

### Step 2: Configure Edge Startup Settings

1. Save `router.html` to a permanent location on your PC (e.g., `C:\Users\YourName\Documents\router.html`).
2. Open **Microsoft Edge**.
3. Click the three dots (`...`) in the top-right corner and select **Settings**.
4. In the left navigation menu, click **Start, home, and new tabs**.
5. Under the **When Edge starts** section, select **Open these pages:**.
6. Click **Add a new page** and enter the file path to your dashboard:
   ```text
   file:///C:/Users/YourName/Documents/router.html