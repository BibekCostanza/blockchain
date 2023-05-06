
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from blockie.models import contact
def home(request):
    return render(request,'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username , password = password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        x=login(request , user_obj)
        if x== login(request, user_obj): 
            return redirect('/')
        
    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request ,'index2.html')

def about(request):
    return render(request,'index3.html')

def lol(request):
    return render(request,'index4.html')



def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username = username)
        user.set_password(password)
        user.save() 
        return redirect('/home/light')
        

        
         

    return render(request , 'fight.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        something = request.POST.get('something')
        contac = contact(name=name, email=email, subject=subject, something=something)
        contac.save()
        messages.warning(request, 'success')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'index3.html')