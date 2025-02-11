import time

def display_message(message):

    print(f"The message is: {message}")

def send_message(serial, data_to_send):
    # Send data
    serial.write(f"{data_to_send}\n".encode())
    # Wait a bit for Arduino to process the data and send a response
    time.sleep(1)

def receive_data(serial):
    # Read the response from Arduino
    while serial.in_waiting:
        if serial.in_waiting > 0:
            line = int(serial.readline().decode().rstrip())
            #print(f"Received number: {line}") # Print the echoed integer from Arduino
            break

    return line