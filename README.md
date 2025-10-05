# Redis WebUI

![Redis WebUI Screenshot](/images/screenshot.png)  
*A sleek, Bootstrap-powered web interface for monitoring and managing your Redis instances.*

---

## Overview

Redis WebUI is a lightweight, open-source web interface to **inspect, monitor, and interact with Redis databases**. It’s designed for convenience, security, and usability:

- Modern Bootstrap 5 design
- Responsive cards, tables, and progress bars
- Key pagination for large databases
- Session-based credential storage (never persisted to disk)
- CPU, memory, uptime, and command stats at a glance

Perfect for **local development** or securely connecting to remote Redis servers.

### Don't want to host? This one's done for you: [redis.mileshilliard.com](https://redis.mileshilliard.com) 

Alternative (more memorable) domain name:
[redis.sntx.dev](https://redis.sntx.dev) 

---

## Features

- **Memory Usage**: Visual progress bar and human-readable stats
- **CPU & Commands**: Track CPU time and total commands processed
- **Uptime & Clients**: See how long your Redis instance has been running and active connections
- **Database Stats**: Keys, expiration counts, average TTL per DB
- **Paginated Keys List**: Avoid loading thousands of keys at once
- **Connect / Switch Servers**: Easily log out or connect to a different Redis instance
- **SSL/TLS Support**: Optional encryption for remote connections
- **Open Source & Transparent**: Inspect the code and know exactly what happens with your credentials

---

## Screenshot

![Dashboard Screenshot](/images/dashboard.png)

---

## Running it locally

### Prerequisites

- Python 3.9+
- Redis server to connect to
- `pip` package manager

### Installation

1. Clone this repository:

```bash
git clone https://github.com/syntaxerror019/redis-webui.git
cd redis-webui
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
python index.py
```

4. Open your browser at:

```
http://127.0.0.1:5000
```