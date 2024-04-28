from django.shortcuts import render, redirect, HttpResponse
from .models import *
import random
import string
# Create your views here.


def contactupload(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        data=contacts(name=name,address=address, phone=phone, email=email)
        data.save()
        return redirect(contactdisplay)
        # return render(request, 'Task3_contact_upload.html', {'name':name, 'address': address, 'phone':phone, 'email': email})
    return render(request, 'Task5_contact_add.html')

def contactdisplay(request):
    data=contacts.objects.all()
    return render(request, 'Task5_contact_display.html', {'data': data})


def contactupdate(request, id):
    data=contacts.objects.get(id=id)
    if(request.method=='POST'):
        data.name=request.POST.get('name')
        data.address=request.POST.get('address')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.save()
        return redirect(contactdisplay)
    return render(request, 'Task5_contact_update.html',{'data':data})

def contactdelete(request, id):
    data=contacts.objects.get(id=id)
    data.delete()
    return redirect(contactdisplay)


def calculator(request):
    if(request.method == 'POST'):
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            answer = number1 + number2
        elif operation == 'subtract':
            answer = number1 - number2
        elif operation == 'multiply':
            answer = number1 * number2
        elif operation == 'divide':
            if number2 == 0:
                return HttpResponse('Please enter a valid number, Division by zero is not possible!')
            answer = number1 / number2
        else:
            return HttpResponse("Invalid operator")
        # print(answer)
        return render(request, 'Task2_calculator_answer.html', {'answer': answer})

    return render(request, 'Task2_calculator_upload.html')


def passwordgenerator(request):
    if(request.method == 'POST'):
        length = int(request.POST.get('length'))
        data = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        return render(request, 'Task3_password_display.html', {'data': data})
    else:
        return render(request, 'Task3_password_generator.html')

