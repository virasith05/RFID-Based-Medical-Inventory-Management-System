from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Medicine
from .forms import MedicineForm
from django.core.mail import send_mail
from django.conf import settings



def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save()

            # Check if the stock is below 5% of the original quantity
            if medicine.quantity < 0.05 * medicine.original_quantity:
                send_mail(
                    'Low Stock Alert',
                    f'The stock for {medicine.name} is below 5%. Please restock it soon.',
                    'medicalshop383@gmail.com',  # Your email address here
                    ['medicalshop383@gmail.com'],  # Your email address here
                    fail_silently=False,
                )

            # Redirect to the same page after adding the medicine
            return redirect('add_medicine')
    else:
        form = MedicineForm()
    
    # Fetch all medicines from the database to display them
    medicines = Medicine.objects.all()
    
    # Render the add_medicine.html template with the form and medicines
    return render(request, 'inventory/add_medicine.html', {'form': form, 'medicines': medicines})

def search_medicine(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.filter(name__icontains=query) if query else Medicine.objects.all()

    return render(request, 'inventory/search_medicine.html', {'medicines': medicines})


def home(request):
    return render(request, 'inventory/home.html')

def scan_medicine(request):
    return render(request, 'inventory/scan_medicine.html')











    

