import serial
import time

# Replace '/dev/ttyUSB0' with your actual serial port
ser = serial.Serial('COM6', 9600)  # Adjust baud rate if necessary
time.sleep(2)  # Wait for the connection to establish

# Send data to Arduino
data_to_send = 14
ser.write(f"{data_to_send}\n".encode('utf-8'))

# Wait a bit for Arduino to process the data and send a response
time.sleep(1)

# Read the response from Arduino
while ser.in_waiting:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip() 
        print(f"Received number: {line}") # Print the echoed integer from Arduino

# Close the serial connection
ser.close()