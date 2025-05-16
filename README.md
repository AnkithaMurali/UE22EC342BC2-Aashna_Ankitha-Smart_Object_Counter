# UE22EC342BC2-Aashna_Ankitha-Smart_Object_Counter

📌 INTRODUCTION
This project is a low-cost, beginner-friendly system for detecting and counting small objects using an Infrared (IR) sensor and an Arduino Uno. It’s designed for applications like sorting, packaging, and inventory tracking, especially in educational or small-scale automation environments.

⚙️ HOW IT WORKS
An IR sensor emits and detects reflected infrared light when an object passes by.
The Arduino Uno reads the sensor signal and keeps count of the objects.
The count is sent via serial communication to a computer.
A ROS2 Python node receives the data and publishes it to a ROS2 topic.
This enables real-time monitoring and visualization using ROS tools.

🧠 WHY USE THIS SYSTEM?
Simple and cost-effective alternative to camera-based systems
Easy to build and understand for beginners
Real-time data processing with ROS2
Modular and scalable for robotics integration

🛠️ TECHNOLOGIES USED
Arduino Uno
Infrared (IR) Sensor
L298N Motor Driver
ROS2 (Robot Operating System 2)


🎯 IDEAL FOR 
Robotics and automation students
STEM learning environments
Quick prototyping for object detection/counting
Lightweight industrial automation demos
