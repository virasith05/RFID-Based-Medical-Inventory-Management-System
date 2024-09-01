import json
from channels.generic.websocket import WebsocketConsumer
from .models import Medicine
from django.core.mail import send_mail

class InventoryConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        rfid_tag = data['rfid_tag']
        try:
            medicine = Medicine.objects.get(rfid_tag=rfid_tag)
            medicine.quantity -= 1
            medicine.save()
            
            # Check if stock is below 5%
            if medicine.quantity < 0.05 * medicine.quantity:
                send_mail(
                    'Low Stock Alert',
                    f'The stock for {medicine.name} is below 5%. Please restock it soon.',
                    'medicalshop383@gmail.com',
                    ['medicalshop383@gmail.com'],
                    fail_silently=False,
                )
                
            # Send updated quantity back to WebSocket
            self.send(text_data=json.dumps({
                'status': 'success',
                'medicine_name': medicine.name,
                'new_quantity': medicine.quantity,
            }))
        except Medicine.DoesNotExist:
            self.send(text_data=json.dumps({
                'status': 'error',
                'message': 'Medicine not found.'
            }))
