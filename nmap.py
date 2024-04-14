{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import subprocess\
\
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