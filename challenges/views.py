from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january" : "Eat no meat for entire month",
    "february" : "Walk for 2 hours",
    "march" : "Do nothing"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data =f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# Create your views here.
def january(request):
    '''_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_'''
  
    return HttpResponse("Eat more meat")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[forward_month])
    return HttpResponseRedirect(redirect_path)




def monthly_challenge(request,month):
    try:
        challenge_month = monthly_challenges[month]
        return render(request,"challenges/challenge.html")
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Not supported")      
    