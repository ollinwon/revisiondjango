from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ContactForm, RegisterForm,ImageForm
from django.contrib.auth.hashers import make_password, check_password
from .serializer import RegisterSerializer


def delete(request):
    return HttpResponse(f"Hello World!")

# def delete(request):
#     name=request.GET.get('name')
#     email=request.GET.get('email')
#     return HttpResponse(f"Hello World!{name} and {email}") 

def hellohtml(request):
    return render(request,'myfirst.html')



def insertuser(request):
    # data=ContactForm(Name="Ashraf",Email="ashraf@gmail.com",Message="HI Hello")
    # data.save()

    data=ContactForm.objects.create(Name="Ashraf",Email="ashraf@gmail.com",Message="HI Hello")
    return HttpResponse(data)


def displayuser(request):
   data = ContactForm.objects.all()
   return HttpResponse(data)
    # # return render(request, 'contact_list.html', {'contacts': contacts})

def filtereddata(request):
    data=ContactForm.objects.filter(created_at="2024-08-24 12:25:41.530909+00:00")
    return HttpResponse(data)



def ordereddata(request):
    data=ContactForm.objects.all().order_by('created_at')
    return HttpResponse(data)



def updatesingle(request):
    data=ContactForm.objects.get(id=1)
    data.Name="new Name"
    data.save()
    return HttpResponse(data)

def updatemultiple(request):
    ContactForm.objects.filter(Age=30).update(Message="Hello")


def deletecriteria(request):
    ContactForm.objects.get(id=2).delete()
    return HttpResponse("deleted")

def deletemultiple(request):
    ContactForm.objects.filter(Age=30).delete()

def deleteall(request):
    ContactForm.objects.all().delete()



@csrf_exempt
def insertpostdata(request):
    if request.method=='POST':
        name=request.POST.get('fname')
        email=request.POST.get('femail')
        message=request.POST.get('fmessage')

        user=ContactForm.objects.create(Name=name,Email=email,Message=message)
        return HttpResponse(user)
        
    else:
        return HttpResponse("Error")
    




@csrf_exempt
def register(request):
    if request.method=='POST':
        name=request.POST.get('fname')
        email=request.POST.get('femail')
        username=request.POST.get('fusername')
        password=request.POST.get('fpassword')
        

        user=RegisterForm.objects.create(Name=name,Email=email,Username=username,Password=password)
        # return HttpResponse(data)
        serializer=RegisterSerializer(user)
        return JsonResponse({'status':'Success','data':serializer.data})
    else:
        return HttpResponse("No Data")
    
@csrf_exempt
def hashregister(request):
    if request.method == 'POST':
        name=request.POST.get('fname')
        email=request.POST.get('femail')
        username = request.POST.get('fusername')
        password = request.POST.get('fpassword')

       
        if RegisterForm.objects.filter(Username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user=RegisterForm.objects.create(Name=name,Email=email,Username=username,Password=make_password(password))
        serializer = RegisterSerializer(user)
        return JsonResponse({'message': 'User registered successfully','data':serializer.data}, status=201)

    


@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST.get('fusername')
        password=request.POST.get('fpassword')
        exists = RegisterForm.objects.filter(Username=username,Password=password).exists()
        return HttpResponse(exists)

@csrf_exempt   
def hashlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    
        try:
            user = RegisterForm.objects.get(username=username)
        except RegisterForm.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

        if  check_password(password, user.password):
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        

    return JsonResponse({'error': 'Only POST method is allowed'},status=405)


@csrf_exempt
def upload_image(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        image=request.FILES.get('Image')
        ImageForm.objects.create(name=name,image=image)
        return JsonResponse({'message': 'Upload successfull'}, status=200)
