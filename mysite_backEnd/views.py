from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from .validation import validateUserData,getUserData
from django.conf import settings
import os, jwt ,json


# Create your views here.

def index(request):
    return JsonResponse({"name": "Ahmed"})


def addUser(request):

    if request.method == 'POST':
        user=getUserData(request.POST)
        avatar=request.FILES.get('picture')
        error=validateUserData(user,avatar)
        if(error!={}):
            return JsonResponse(error,safe=False)
        else:
            hashed_pwd = make_password(user.password)
            user.password=hashed_pwd
            try:
                user.save()
            except:
                return JsonResponse({"error": "database error ,user exist,duplicate phone number or email"})


            userData={"first_name":user.first_name,"last_name":user.last_name,
            "countryCode":str(user.countryCode),"phone_number":user.phone_number,
            "gender":user.gender,"birthDate":user.birthDate, "email":user.email}
            return JsonResponse(userData,safe=False)

    else:
        return JsonResponse({"req": "get"})

###..........................................................................................###
def authToken(request):
    if(request.method=='POST'):
        phone_number='phone_number' in request.POST and request.POST['phone_number']
        password='password' in request.POST and request.POST['password']
        error={}
        if not phone_number:
            error.update({"phone_number":"blank"})

        if not password:
            error.update({"password":"blank"});

        if error == {} :
            try:
                user=User.objects.get(phone_number=phone_number)
                matched=check_password(password,user.password)  # returns True
                if matched :
                    #.. return token
                    user_data={"user_name":user.first_name,"user_email":user.email}
                    encoded = jwt.encode(user_data, 'secret', algorithm='HS256')
                    return JsonResponse({"phone_number":phone_number,"authorized":matched,"token":encoded.decode("utf-8") })
                else:
                    return JsonResponse({"authorization":"is not authorized"})

            except User.DoesNotExist:
                user = None
                return JsonResponse({"error":"no user exist with that phone"})

        else :
            return JsonResponse(error,safe=False);

####......................... get user profile by verfying token ...............................####

def accessProfile(request):
        if(request.method=='POST'):
            phone_number='phone_number' in request.POST and request.POST['phone_number']
            authToken='authToken' in request.POST and request.POST['authToken']
            error={}
            if not phone_number:
                error.update({"phone_number":"blank"})

            if not authToken:
                error.update({"authToken":"blank"});

            if error == {} :
                decoded=jwt.decode(authToken, 'secret', algorithms=['HS256'])
                return JsonResponse(decoded,safe=False);#payload data

            else :
                return JsonResponse(error,safe=False);
