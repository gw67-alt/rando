import pyautogui
import serial
import time

# Configure the serial port
serial_port = 'COM4'  # Replace with your serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

# Threshold limit
threshold = 0

# Movement parameters
move_distance = 10  # Distance to move per impulse
move_delay = 0.1    # Delay between movements

def move_mouse(direction):
    # Get the current mouse position
    current_x, current_y = pyautogui.position()
    new_x, new_y = current_x, current_y



    # Move the mouse to the new position slowly
    pyautogui.moveTo(new_x, new_y, duration=move_delay)

def read_serial_data():
    direction = "right"  # Default direction

    while True:
        if ser.in_waiting > 0:
            # Read data from serial port
            line = ser.readline().decode('utf-8').strip()
            try:
                # Convert the line to a float
                value = float(line)
                # Check if the value exceeds the threshold
                if value > threshold:
                    pyautogui.click()  # Perform a left-click

                move_mouse(direction)

            except ValueError:
                print(f"Invalid data: {line}")

if __name__ == "__main__":
    try:
        read_serial_data()
    except KeyboardInterrupt:
        print("Program terminated")
    finally:
        ser.close()