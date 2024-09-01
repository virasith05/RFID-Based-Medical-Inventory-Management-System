import serial
import json
import requests

# Set up serial connection (make sure the port and baud rate match your Arduino setup)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port

while True:
    if ser.in_waiting > 0:
        rfid_tag = ser.readline().decode('utf-8').strip()
        print("Scanned RFID Tag:", rfid_tag)

        # Send data to Django WebSocket
        try:
            response = requests.post('http://127.0.0.1:8000/inventory/scan/', json={'rfid_tag': rfid_tag})
            print("Response from server:", response.text)
        except Exception as e:
            print("Error sending data to server:", e)
