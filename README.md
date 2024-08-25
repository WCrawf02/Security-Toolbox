# Network Analysis 👁️🕵🏾‍♂️

### Tools Used 
1. Nmap👁️
   - **Purpose**: Network scanning and enumeration tool
   - **Explanation**: Used to identify open ports, services, and potential vulnerabilities on the target (victim) machine. Nmap provides a detailed map of the network, aiding in vulnerability assessment.
   - **Example script used in this project**:
      - Command: nmap -sV [target_ip]
      - Outcome: Scanned for open ports and service versions on the victim machine.
2. Wireshark🦈
   - **Purpose**: Network protocol analyzer
   - **Explanation**: Used to capture and analyze netwrok traffic between machines. Wireshark is crucial for detecting and analyzing potential malicious             activity in the network traffic.
3. SSH (Secure Shell)🌰
   - **Purpose**: Secure remote access to machines.
   - **Explanation**: Configured SSH on the victim (Ubuntu) machine to enable remote shell access from the attacker (Kali Linux) machine. This allowed me          secure control over the victim machine's commandl line interface from another device.
   - **Command Used**: ssh username@[victim_ip]
4. VirtualBox🛜
   - **Purpose**: Virtualization software for running machines.
   - **Explanation**: Created virtual machines for both Ubuntu and Kali Linux. Used to create and run virtual enviironments for both my victim and attacker          machines.  I was ableto set up isolated environments to conduct safe penetration testing and vulnerability analysis.
5. Kali Linux📲
   - **Purpose**: Penetration testing and security auditing platform.
   - **Explanation**: Performed attacks like network scanning, traffic analysis, and remote shell setup from the Kali Linux Machine.
6. Ubuntu
   - **Purpose**: Operating system for the victim machine.
   - **Explanation**: Used as the target (victim) machine for testing vulnerabilities and monitoring network traffic. 
