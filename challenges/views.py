from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january" : "Eat no meat for entire month",
    "february" : "Walk for 2 hours",
    "march" : "Do nothing"
}

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
        return HttpResponse(challenge_month)
    except:
        return HttpResponseNotFound("Not supported")      
    