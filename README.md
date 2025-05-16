# UE22EC342BC2-Aashna_Ankitha-Smart_Object_Counter

PROJECT OVERVIEW

This project is a simple and low-cost solution for counting small objects using an infrared (IR) sensor and an Arduino Uno. It is useful for tasks like sorting, packaging, and inventory tracking in small-scale or educational setups.

Instead of using complex and expensive camera systems, this project detects objects based on the reflection of IR light. When an object passes in front of the sensor, the Arduino counts it and sends the data to a computer.

HOW IT WORKS

An IR sensor detects objects by sensing reflected infrared light.

The Arduino Uno reads the sensor and counts each object that passes by.

This count is sent to a computer using serial communication.

A ROS2 Python node receives the data and publishes it to a ROS2 topic.

The system can be connected to tools like rviz or rqt_plot for visualization.

WHY THIS PROJECT?

Simple and affordable hardware

Easy to build and understand

Works in real-time

Can be used for learning and small automation projects

TOOLS AND TECHNOLOGIES

Arduino Uno

IR Sensor

L298N driver motor

ROS2
