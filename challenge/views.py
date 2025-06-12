from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


months = {
    "january": "Become a profitable trader",
    "february": "Become a successful fullstack engineer (React + Django)",
    "march": "Possibly get hired full-time as a fullstack dev",
    "april": "Maintain physical, spiritual, and personal well-being",
    "may": "Send commitment money to Yam's",
    "june": "Pay off debt to Honey (150k for laptop, Crypto Contributions, etc.)",
    "july": "Happy birthday Honey",
    "august": "Happy birthday Pa, and Michmas",
    "september": "Happy anniveersary",
    "october": None,
    "november": "Jolly good show indeed",
    "december": "Happy birthday ma",
}


def index(request):
    data = {
        "months": months,
    }
    return render(request, 'challenge/index.html', data)

def challenge_by_month_number(request, month):
    _months = list(months.keys())
    try:
        _month = _months[month-1]
        urlpath = reverse("month-challenge", args=[_month])
        return HttpResponseRedirect(urlpath)
    except:
        raise Http404()

def challenge_by_month(request, month):
    try:
        data = {
            'month': month,
            'text': months[month],
        }
        return render(request, 'challenge/challenge.html', data)
    except:
        raise Http404()
