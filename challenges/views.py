from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january" : "Eat no meat for entire month",
    "february" : "Walk for 2 hours",
    "march" : "Do nothing",
    "april" : None
}

def index(request):
    #list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",{
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data =f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

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
        return render(request,"challenges/challenge.html", {
            "month_name": month,
            "text":challenge_month
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        return Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)      
    