from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):  # HttpRequest
    # t = render_to_string()
    # return HttpResponse(t)
    data = {
        'title': 'Main page with heatmap',
        'header': 'Main page header with heatmap'
    }
    return render(request, 'heatmap/index.html', context=data)


def info(request, test_id):  # HttpRequest
    return HttpResponse(f"Heatmap page - {test_id}")
