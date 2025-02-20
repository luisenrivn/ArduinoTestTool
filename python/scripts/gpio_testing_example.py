import serial
import time
from setup_conf import *

# Set serial configuration
ser = serial.Serial('COM6', 9600)  # Adjust baud rate if necessary
time.sleep(2)  # Wait for the connection to establish

# Test for GPIO 
# Inputs of mixer system
# Bit        Function
#--------------------
# 0          Power
# 1          Release fluid
# 2          Low level
# 3          High level

# Outputs of mixer system
# Bit        Function
#--------------------
# 0          Fluid 1 valve
# 1          Fluid 2 valve
# 2          Mixer engine
# 3          Release fluid valve

# Crate a new test
GPIO_Test1 = GPIO_Test()

# Test 1: Power system with normal level (nor high nor low) 
# Set port to 1 --> 0001
data_to_send = 1
GPIO_Test1.set_gpio_value(ser, data_to_send)
print(f"Set port value: {data_to_send}")
time.sleep(2)
# Expected: Nothing should happen
obtained_data = GPIO_Test1.get_gpio_value(ser)
test_name = "Test 1: Power with normal level"
verify_result(test_name, 0, obtained_data)

time.sleep(3)

# Test 2: There is low level
# Set port to 5 --> 0101
data_to_send = 5
GPIO_Test1.set_gpio_value(ser, data_to_send)
time.sleep(2)
# Expected: Fluid 1 and 2 should activate 0011 - 3
obtained_data = GPIO_Test1.get_gpio_value(ser)
test_name = "Test 2: Powered with low level"
verify_result(test_name, 3, obtained_data)

time.sleep(3)

# Test 3: There is high level
# Set port to 9 --> 1001
data_to_send = 9
GPIO_Test1.set_gpio_value(ser, data_to_send)
time.sleep(2)
# Expected: Fluid 1 and 2 valves should  are shut down and mixer engine is on
# for 5 seconds  0100 - 4
obtained_data = GPIO_Test1.get_gpio_value(ser)
test_name = "Test 3: Powered with high level"
verify_result(test_name, 4, obtained_data)

print("Wait 5 seconds")
time.sleep(5)

# Test 4: There is high level
# Expected: Mixer engine should be turned off 
# activate for 5 seconds  0000 - 0
obtained_data = GPIO_Test1.get_gpio_value(ser)
test_name = "Test 4: Mixer engine is turned off"
verify_result(test_name, 0, obtained_data)

time.sleep(3)

# Test 5: There is high level
# Set port to 0 --> 0000
data_to_send = 0
GPIO_Test1.set_gpio_value(ser, data_to_send)
time.sleep(2)
# Expected: System is turn off
obtained_data = GPIO_Test1.get_gpio_value(ser)
test_name = "Test 5: Reset system"
verify_result(test_name, 0, obtained_data)

# Close the serial connection
ser.close()

save_results("GPIO_Mixer_Test_Results.txt")
