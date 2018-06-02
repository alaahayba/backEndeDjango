from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from .validation import validateUserData,getUserData


# Create your views here.

def index(request):
    return JsonResponse({"name": "Ahmed"})


def addUser(request):

    if request.method == 'POST':
        user=getUserData(request.POST)
        error=validateUserData(user)
        if(error!={}):
            return JsonResponse(error,safe=False)
        else:
            #... save user data
            user.save()
            return JsonResponse(user.first_name,safe=False )
            # return JsonResponse(dumps(user),safe=False)

        # hashed_pwd = make_password("plain_text")
        # check_password("plain_text",hashed_pwd)  # returns True

    else:
        return JsonResponse({"req": "get"})
