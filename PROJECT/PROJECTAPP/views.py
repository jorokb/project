from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from PROJECT.views import PdfMixin
from PROJECT.local import generate_pdf, render_to_pdf_response, pdf_decorator

def test_view(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/lpc.html', file_object=resp)
    return result


def index(request):
    return render(request, "PROJECTAPP/hi.html")

def lpc(request):
    return render(request, "PROJECTAPP/lpc.html")

def lpn(request):
    return render(request, "PROJECTAPP/lpn.html")

def lpn2(request):
    return render(request, "PROJECTAPP/lpn2.html")

def lpp(request):
    return render(request, "PROJECTAPP/lpp.html")

def pst(request):
    return render(request, "PROJECTAPP/pst.html")

def pst2(request):
    return render(request, "PROJECTAPP/pst2.html")
