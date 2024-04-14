

def nmap_scan(target, options=None):\
    # Build the Nmap command with user-specified options\
    nmap_command = ["nmap"]\
    if options:\
        nmap_command.extend(options.split())\
    nmap_command.append(target)\
\
    # Execute the Nmap command and capture output\
    try:\
        output = subprocess.check_output(nmap_command, stderr=subprocess.STDOUT, universal_newlines=True)\
        print(output)\
    except subprocess.CalledProcessError as e:\
        print(f"Error executing Nmap command: \{e.output\}")\
\
if __name__ == "__main__":\
    # Target IP address or hostname to scan\
    target = input("Enter the target IP address or hostname to scan: ")\
\
    # Additional options for Nmap scan (optional)\
    options = input("Enter additional options for the Nmap scan (e.g., '-sS -p 1-1000'): ")\
\
    # Perform the Nmap scan\
    nmap_scan(target, options)\
}
