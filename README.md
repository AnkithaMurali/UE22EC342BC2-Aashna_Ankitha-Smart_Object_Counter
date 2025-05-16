# UE22EC342BC2-Aashna_Ankitha-Smart_Object_Counter

### PROJECT OVERVIEW

This project is a simple and low-cost solution for counting small objects using an infrared (IR) sensor and an Arduino Uno. It is useful for tasks like sorting, packaging, and inventory tracking in small-scale or educational setups.

Instead of using complex and expensive camera systems, this project detects objects based on the reflection of IR light. When an object passes in front of the sensor, the Arduino counts it and sends the data to a computer.

### HOW IT WORKS

An IR sensor detects objects by sensing reflected infrared light. If an object is detected, the sensor value is high. 

The Arduino Uno reads the sensor and counts each object that passes by.

This count is sent to a computer using serial communication (pySerial).

A ROS2 Python node receives the data and publishes it to a ROS2 topic.

The system can be connected to tools like rviz or rqt_plot for visualization.

### WHY THIS PROJECT?
1. - Simple and affordable hardware
2. - Easy to build and understand
3. - Works in real-time
4.   - Can be used for learning and small automation projects

### TOOLS AND TECHNOLOGIES
1. - Arduino Uno
2. - IR Sensor
3. - L298N driver motor
4. - ROS2

### Contributors:
1. Aashna Ali (PES1UG22EC002)
2. Ankitha M (PES1UG22EC038)
