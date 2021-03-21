from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


def enterPoint(req: HttpRequest):
    return redirect("products:featured_products")
    
