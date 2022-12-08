# Firewall-Bypass
I use this tool to pypass most firewalls.
The working principle is simple. There are two scripts to run on one server and one client machine.
Client and server can communicate any data through these two scripts.
What I do usually is to bind remote SSH port into my local port using these scripts and then use SSH tunnel and VPN.



Use:
```bash
# 1. set desired parameters inside client.py and server.py (port number you want to tunnel etc.)
# 2. run the scripts on server and client
# on server
python3 server.py
# on client
python3 client.py
```

This is going to add some html headers to the traffic which will allow you to bypass the firewall.
Since the firewall thinks we are sending html packets but not some encrypted packets (which are blocked by default), it allows all connections.

Tried with SSH tunnel and VPN and both worked.
