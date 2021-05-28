from django.http import JsonResponse
from django.http.response import HttpResponse
from db import query_lines, query_stations

def lines_view(request):
    return JsonResponse(query_lines(), safe=False, json_dumps_params={"indent":2})


def stations_view(request):
    line_id = request.GET.get("line_id", None)
    return JsonResponse(query_stations(line_id=line_id), safe=False, json_dumps_params={"indent":2})

def home_view(request):
    return HttpResponse("""
    Welcome To the Rail API.<br>
    Available Endpoints<br>
    - api/stations/<br>
    - api/lines/<br>
    """)