import rclpy
from std_msgs.msg import Int32
import serial

def listener():
    rclpy.init()
    node = rclpy.create_node('object_count_listener')
    publisher = node.create_publisher(Int32, 'object_count', 10)

    # Open the serial port where Arduino is connected (replace with your serial port)
    serial_port = '/dev/ttyUSB0'  # Replace with your Arduino's serial port
    baud_rate = 9600  # Same baud rate as in Arduino code
    ser = serial.Serial(serial_port, baud_rate)

    while rclpy.ok():
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data.startswith("Object Count:"):
                # Extract the object count from the serial data
                try:
                    count = int(data.split(":")[1].strip())
                    msg = Int32()
                    msg.data = count
                    publisher.publish(msg)  # Publish the object count to ROS 2
                except ValueError:
                    pass  # If data isn't a valid number, just skip

        rclpy.spin_once(node)

    ser.close()

if __name__ == '__main__':
    listener()
