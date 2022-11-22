from django.shortcuts import render, redirect
from random import randint


def index(request):

    return render(
        request,
        "main/index.html",
        {
            "places": {i: "booked" if randint(0, 1) else "" for i in range(1, 26)},
        }
    )
