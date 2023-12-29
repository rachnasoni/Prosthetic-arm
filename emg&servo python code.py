import serial
import time

# Define the COM port where your Arduino is connected
arduino_port = 'COMX'  # Replace 'COMX' with the actual port name (e.g., 'COM3' on Windows)

# Define threshold values and corresponding servo angles
threshold1 = 300
angle1 = 0
threshold2 = 600
angle2 = 90
threshold3 = 900
angle3 = 180

# Initialize the serial connection
ser = serial.Serial(arduino_port, 9600, timeout=1)
time.sleep(2)  # Allow time for the Arduino to reset

def control_servo(emg_value):
    if emg_value < threshold1:
        servo_angle = angle1
    elif emg_value < threshold2:
        servo_angle = angle2
    elif emg_value < threshold3:
        servo_angle = angle3
    else:
        servo_angle = angle2  # Default to angle2 if above threshold3

    command = f"{servo_angle}\n"
    ser.write(command.encode())
    print(f"EMG Value: {emg_value}, Servo Angle: {servo_angle} degrees")

try:
    while True:
        emg_value = int(ser.readline().decode().strip())  # Read EMG value from Arduino
        control_servo(emg_value)
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
