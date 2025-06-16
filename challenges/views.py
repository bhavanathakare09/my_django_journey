from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthlyChallenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is January"
    elif month == "february":
        challenge_text = "This is February"
    elif month == "march":
        challenge_text = "This is March"
    elif month == "april":
        challenge_text = "This is April"
    elif month == "may":
        challenge_text = "This is May"
    elif month == "june":
        challenge_text = "This is June"
    elif month == "july":
        challenge_text = "This is July"
    elif month == "august":
        challenge_text = "This is August"
    elif month == "september":
        challenge_text = "This is September"
    elif month == "october":
        challenge_text = "This is October"
    elif month == "november":
        challenge_text = "This is November"
    elif month == "december":
        challenge_text = "This is December"
    else:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse("" + challenge_text)



