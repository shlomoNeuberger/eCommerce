from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


def enterPoint(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect("products:featured_products")
    else:
        return redirect("login:login")
