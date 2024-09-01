# RFID-Based-Medical-Inventory-Management-System

#Overview

The RFID-Based Medical Inventory Management System is a Django-based web application designed to improve inventory management in a medical shop. By integrating RFID technology with a web interface, this system automates the tracking of medicine stock levels, ensuring efficient operations and preventing stockouts.

#Features

1)RFID Tagging for Inventory Management: Each medicine is tagged with an RFID tag upon arrival. The RFID tag number, medicine name, location (rack number), original quantity, and current quantity are recorded in a database through a web interface.

2)Automated Stock Update via RFID Scanning: An RC522 RF IC Card Sensor Module placed at the billing counter scans the RFID tags of medicines during billing. The system automatically updates the inventory database by reducing the quantity of the scanned medicines.

3)Real-Time Inventory Tracking: The Django web application provides real-time updates on inventory status. As medicines are scanned, the current quantities are adjusted in the system, reflecting accurate stock levels at all times.

4)Low Stock Alerts: The system monitors medicine quantities continuously. When the quantity of any medicine falls below 5% of its original stock, it sends an automated email notification to the shopkeeper, ensuring timely restocking.

5)Search Functionality: The web application includes a search feature, allowing the shopkeeper to quickly find the location and details of any medicine by name, facilitating efficient retrieval and management.

6)User-Friendly Interface: Displays all medicines in a table format, showing both original and current quantities. This ensures easy navigation and management for the shop staff.

#Technical Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Hardware: Arduino Uno R3, RC522 RF IC Card Sensor Module

Database: SQLite (default for Django)

#How It Works

Setup: New medicines are tagged with RFID tags, and their details are manually entered into the system using the web application.

Billing: At the billing counter, medicines are scanned using the RFID reader. The system automatically detects the RFID tags and updates the inventory.

Real-Time Monitoring: The web application provides real-time inventory levels and sends alerts when stock is low, ensuring no medicine runs out unexpectedly.

#Benefits

Efficiency: Automates the process of inventory tracking and reduces manual errors.

Accuracy: Provides accurate, real-time stock levels, reducing the risk of running out of critical medicines.

Convenience: Enhances operational efficiency with a simple search and automatic stock update features.
