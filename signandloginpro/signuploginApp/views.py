from django.shortcuts import render
from signuploginApp.forms import SignUpDataForm,LoginDataForm
from .models import SignUpData
from django.http.response import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from signuploginApp.tokens import account_activation_token

def sign_page(request):
    if request.method=='POST':
        sform=SignUpDataForm(request.POST)
        if sform.is_valid():
            name=request.POST.get('name','')
            age=request.POST.get('age','')
            email_id=request.POST.get('email_id','')
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            data=SignUpData(
                name=name,
                age=age,
                email_id=email_id,
                username=username,
                password=password
            )
            data.save()
            lform=LoginDataForm()
            return render(request,'login_form.html',{'lform':lform})
        else:
            return HttpResponse("invalid Data")
    else:
        sform=SignUpDataForm()
        return render(request,'sign_form.html',{'sform':sform})


def login_page(request):
    if request.method=='POST':
        lform=LoginDataForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            uname=SignUpData.objects.filter(username=username)
            pwd=SignUpData.objects.filter(password=password)

            if uname and pwd:
                return HttpResponse('correct username and password..')
            else:
                return HttpResponse('wrong username and password...')
        else:
            return HttpResponse("invalid data")
    else:
        lform=LoginDataForm()
        return render(request,'login_form.html',{'lform':lform})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')





































