from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from PROJECT.views import PdfMixin
from PROJECT.local import generate_pdf, render_to_pdf_response, pdf_decorator

def test_view(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/pst2.html', file_object=resp)
    return result


def index(request):
    return render(request, "PROJECTAPP/hi.html")

def lpc(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/lpc.html', file_object=resp)
    return result

def lpn(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/lpn.html', file_object=resp)
    return result

def lpn2(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/lpn2.html', file_object=resp)
    return result

def lpp(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/lpp.html', file_object=resp)
    return result

def pst(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/pst.html', file_object=resp)
    return result

def pst2(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('PROJECTAPP/pst2.html', file_object=resp)
    return result
