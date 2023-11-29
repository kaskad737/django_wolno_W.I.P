from django.shortcuts import render
from django.http import HttpResponse

def index(request): # HttpRequest
    return HttpResponse("Heatmap page")

def info(request, test_id): # HttpRequest
    return HttpResponse(f"Heatmap page - {test_id}")