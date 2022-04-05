from pymed import PubMed
import json
import pandas as pd
from datetime import date

from HLI_investigators import HLI_authorlist, all_PIs, all_PIs_DfObj

import sys
import csv

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="cellerk@yahoo.ca")

from django.shortcuts import render

def button(request):

    return render(request,'geniusvoice.html')

def output(request):
    
    output_data = "Hello world."
    website_link = "Visit our website: " + "https://www.geniusvoice.nl/"
    
    return render(request,"geniusvoice.html",{"output_data":output_data, "website_link":website_link})
