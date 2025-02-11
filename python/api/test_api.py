from serial_com import *
import os
# Test type
# 1 GPIO Test
# 2 Analog inputs and outputes test
results = []

# Get the directory of the current script 
current_dir = os.path.dirname(__file__) 

results_folder_path = os.path.abspath(os.path.join(current_dir, '..', r'results'))

# Generic test functions
def verify_result(test_name, expected, actual):
    if expected != actual:
        result = f"{test_name}, Result: Fail, Expected: {expected}, Actual: {actual}\n"
        print(result)
    else:
        result = f"{test_name}, Result: Pass, Expected: {expected}, Actual: {actual}\n"
        print(result)

    results.append(result)

def save_results(name):
        final_path = os.path.join(results_folder_path, name)
        with open(final_path,"w") as file:
             for result in results:
                 file.write(result)

# 4 GPIO pins can be tested
class GPIO_Test:

    test_code = 1

    # Subcodes
    # 1 Set port value
    # 2 Get current port value

    def set_gpio_value(self, serial, value):
        
        # Set test code
        send_message(serial, 1)
        # Send value
        send_message(serial, value)

    def get_gpio_value(self, serial):
        
        # Set test code
        send_message(serial, 2)
        # Send value
        data = receive_data(serial)

        return data





