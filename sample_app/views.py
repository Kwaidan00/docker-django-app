from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone

def homepage(request):
    now = timezone.now()
    html = """
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <h1>Sample Django page</h1>
            <p>Today is: {}</p>
        </body>
    </html>
    """.format(now)
    return HttpResponse(html)
