from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
def january(request):
    '''_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_'''
  
    return HttpResponse("Eat more meat")

def monthly_challenges(request,month):
    challenge_month = None
    if month == "january":
        challenge_month = " Eat in January"
    elif month == "february":
        challenge_month = "Eat in February"
    elif month == "march":
        challenge_month = "Eat in March"
    else:
        return HttpResponseNotFound("This value is not supported")                
    return HttpResponse(challenge_month)