from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from . import sdk
from .models import User
from decouple import config
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from astrologerapplogic.task import Sending_Emails

#userID = 'USERID'
#apiKey = 'APIKEY'
userID = config("userID")
apiKey = config("apiKey")

# Create your views here.
def test(request):
    print(request)
    return JsonResponse({"message":"success"}, status=200)


def getReport(response):
    if response.method == "POST":
        form = ReportForm(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            phonecode = form.cleaned_data["phonecode"]
            gender = form.cleaned_data["gender"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            place = form.cleaned_data["place"]
            lat = form.cleaned_data["lat"]
            lon = form.cleaned_data["lon"]
            zone = form.cleaned_data["tzone"]
            language = form.cleaned_data["language"]
            phoneno = phonecode+str(phone)

            #save to db
            obj = User(name=name, email=email, phone=phoneno, gender=gender, date=date, time=time, place=place, lat=lat, lon=lon, tzone=zone)
            obj.save()

            #call api
            tzone = getTzone(zone)
            print(name,email,phone,gender,date,time,place,lat,lon,tzone,language, sep='\n')
            if tzone:
                resource = 'basic_horoscope_pdf'
                vedicRishi = sdk.VRClient(userID, apiKey)
                reportData = vedicRishi.reportCall(resource, name, gender, date.day, date.month, date.year, time.hour, time.minute, lat, lon, tzone, place, language)
                data = reportData.json()
                print(data)
                if data['status']:
                    Sending_Emails(email)
                    return JsonResponse({'status':True ,'message':data['pdf_url']}) #pdf_url
                else:
                    return JsonResponse({'status':False,'message':data['msg']})
        else:
            return JsonResponse({'status':False,'message':'Invalid data'})
    else:
        form = ReportForm()
    return JsonResponse({"form":form})


def getPlace(response):
    place = response.POST.get('place')
    # print(place)
    if place:
        resource = 'geo_details'
        astro = sdk.JsonClient(userID, apiKey)
        data = astro.placeCall(resource, place)
        res = data.json()
        if res:
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse({'status':False}, status=500)

def getTzone(zone):
    resource = 'timezone'
    astro = sdk.JsonClient(userID, apiKey)
    data = astro.zoneCall(resource, zone)
    res = data.json()
    return res["timezone"]

def sendMail(data,name,email):
    message = render_to_string("backend/email.html", {"name": name})
    # pdf = data['msg'] #pdf_url
    
    mail = EmailMessage(
        subject="Welcome to NHMC",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
        reply_to=[settings.EMAIL_HOST_USER],
    )
    mail.content_subtype = "html"
    mail.send()