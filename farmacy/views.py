from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PharmacyForm
from .models import Pharmacy


def create_pharmacy(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        contact_number = request.POST['contact_number']
        
        pharmacy = Pharmacy.objects.create(
            name=name,
            address=address,
            contact_number=contact_number
        )
        
        # Redirect to a success page or render a page with the pharmacy info and QR code
        return redirect('doctor_signup', pk=pharmacy.pk)  # Adjust this as per your URL patterns
    
    return render(request, 'pharmacy/create.html')


def Pharmacy_register(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-view")
    else:
        form = PharmacyForm()
    context={
        "form":form
    }
    return render(request,'pharmacy/index.html',context=context)

# @login_required
# def get_pre(request, pk):
#     page_data = Pharmacy.objects.all(pk=pk)
#     # get_prescription = 
    
    