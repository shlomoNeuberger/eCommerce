from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect


def enterPoint(req: HttpRequest):
    if req.user.is_authenticated:
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        return redirect("login:login")
