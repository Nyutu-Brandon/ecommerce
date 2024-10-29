from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect
from django_daraja.mpesa.core import MpesaClient

from customers.forms import CustomerForm,CustomerRegisterForm
from customers.models import Customer
from customers.serializers import CustomerSerializer
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    data = Customer.objects.all()
    context = {'data':data}
    return render(request, 'index.html',context)
def about(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = CustomerRegisterForm()
    return render(request, 'about.html',{'form':form})
def gallery(request):
    return render(request, 'gallery.html')
def contact(request):
    return render(request, 'contact.html')
def signup(request):
    return render(request, 'signup.html')
def edit(request,id):
    customer = get_object_or_404(Customer,id=id)
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'Error!!Please check the details')
    else:
        form = CustomerRegisterForm(instance=customer)
    return render(request, 'edit.html', {'form':form,'customer':customer})
def delete(request,id):
    customer = get_object_or_404(Customer,id=id)
    try:
        customer.delete()
        messages.success(request, 'Customer has been deleted successfully')
    except Exception as e:
        messages.error(request, 'Error!!Customer not deleted')
    return redirect('index')

def customerapi(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer,many=True)
    return JsonResponse(serializer.data,safe=False)

def darajaapi(request):
    cl = MpesaClient()
    phone_number = '0716808429'
    amount = 1
    account_reference = 'eCommerce'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)
