from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Input
from .forms import InputForm, InputQuery
from datetime import datetime

from .scripts import pymed_search

from django.core.cache import cache
cache.clear()

import mimetypes
import csv

# The views.py page has different functions related to the different pages possible.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#def post_new(request):
#    form = InputQuery()
#    return render(request, 'hlipage/input_form.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = InputQuery(request.POST)
        if form.is_valid():
            mindate = form.cleaned_data['min_date'].strftime("%m/%d/%Y")
            maxdate = form.cleaned_data['max_date'].strftime("%m/%d/%Y")
        
            authorlist = form.cleaned_data.get("or_choose_which_author")

            #return redirect('post_detail', pk=post.pk)
            #return HttpResponse(pymed.test_fun(mindate, maxdate, authorlist))
            citations = pymed_search.create_citation_output(mindate, maxdate, authorlist)
            cache.set('citations_list', citations, 30)

            #return HttpResponse(authorlist)
            return render(request, 'hlipage/citation_details.html', {'citations': citations, 'mindate': mindate, 'maxdate': maxdate, 'authorlist': authorlist})

    else:
        form = InputQuery()
    return render(request, 'hlipage/input_form.html', {'form': form})

def download(request):

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="output.csv"'},
    )

    citations = cache.get('citations_list')

    wr = csv.writer(response)
    for item in citations:
        wr.writerow([item])

    return response

def button(request):
    return render(request, 'hlipage/base.html')

#def output(request):
#    return HttpResponse("You have pressed my button!")
#    data = requests.get("https://regres.in/api/users")
#    print(data.text)
#    data = data.text
#    return render(request, 'home.html', {'data': data})

def output(request):

    output_data = pymed_search.date_range
    
    #output_data = "Hello world."
    website_link = "Visit our website: " + "https://www.geniusvoice.nl/"
    
    return render(request,"hlipage/base.html", {"output_data":output_data, "website_link":website_link})