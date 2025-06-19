from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.

challenges_dict = {
    "january": "this is January",
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
    "december": None
}

def index(request):
    months = list(challenges_dict.keys())
    # list_items = ""
    # for month in months:
    #     month_path = reverse("month-challenge", args =[month])
    #     list_items += f"<li><a href = \"{month_path}\">{months}</a></li>"
    # responce_data = f"<ul>{list_items}</ul>"   
    # return HttpResponse(responce_data)
    return render(request, "challenges/index.html", {
        "months": months,
    })
def monthly_challenge_number(request, month):
    months = list(challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirtect_request = months[month - 1]
    redirect_path = reverse("month-challenge" , args=[redirtect_request])
    return HttpResponseRedirect(redirect_path)
    
def monthlyChallenge(request, month):
    try:
        month_lower = month.lower()
        challenge_text = challenges_dict[month_lower]
        index_path = reverse("index")
        return render(request, "challenges/challenges.html",{
            "text": challenge_text,
            "month_name": month,
            "index_path": index_path
        })
        # responce_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound("<h1>Challenge for this month does not exist.</h1>")