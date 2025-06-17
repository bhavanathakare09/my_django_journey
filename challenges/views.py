from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenges_dict = {
    "january": "This is January",
    "february": "This is February",
    "march": "This is March",
    "april": "This is April",
    "may": "This is May",
    "june": "This is June",
    "july": "This is July",
    "august": "This is August",
    "september": "This is September",
    "october": "This is October",
    "november": "This is November",
    "december": "This is December"
}

def monthly_challenge_number(request, month):
    months = list(challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirtect_request = months[month - 1]
    redirect_path = reverse("month-challenge" , args=[redirtect_request])
    return HttpResponseRedirect(redirect_path)
    
    
   

def monthlyChallenge(request, month):
    try:
        challenge_text = challenges_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Challenge for this month does not exist.")



