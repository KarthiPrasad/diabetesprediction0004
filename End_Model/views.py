from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    # return HttpResponse("This is my end-to-end model..")
    return render(request,"home.html")


def result(request):
   
    NB = joblib.load('Finalized_model.sav')

    l = []

    l.append(request.GET['Pregnencies'])
    l.append(request.GET['Glucose'])
    l.append(request.GET['BloodPressure'])
    l.append(request.GET['SkinThickness'])
    l.append(request.GET['Insulin'])
    l.append(request.GET['BMI'])
    l.append(request.GET['DiabetesPedigreeFunction'])
    l.append(request.GET['Age'])

    print(l)

    ans = NB.predict([l])

    return render(request,'result.html',{'ans':ans,'l':l})

