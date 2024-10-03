import serial.tools.list_ports

# Get a list of available serial ports
ports = serial.tools.list_ports.comports()

# Print the list of ports
for port in ports:
    print(f"Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
