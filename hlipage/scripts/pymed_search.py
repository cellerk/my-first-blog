
from pymed import PubMed
import json
from datetime import date
import time

from .investigators import all_PIs_dict

import csv

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="cellerk@yahoo.ca")

#mindate = "01/01/2000"
#maxdate = "02/02/2000"

# Create a GraphQL query in plain text
# Functioning query (first line)
#query = '(("2022/01/01"[Date - Create] : "2022/02/01"[Date - Create])) AND' + HLI_authorlist[1]

# Build your query
#date_range = '''("2022/01/01"[Date - Publication] : "3000"[Date - Publication])'''
#mindate = date.fromisoformat('2021-01-01')
#maxdate = date.fromisoformat('2021-12-31')

def create_citation_output(mdate: str, mxdate: str, alist):
    # Build the query based on the form input (mdate = mindate, mxdate = maxdate, alist = author list (str))
    date_range = "(" +  mdate + "[Date - Publication] : " + mxdate + "[Date - Publication])"
    print(date_range)
    # List of all properly-formatted citations 
    citation = []

    for a in alist:
#         # Create the PubMed query for the specified date_range, iterating through all_PIs
        query = date_range + " AND " + all_PIs_dict.get(a)
        print(query)
#       acc = acc+1
       # Execute the query against the API (must be done separately for each PI)
        results = pubmed.query(query, max_results=500)

        # Add a sleep of 1 second to not overload eutils
        time.sleep(1)

         # Loop over the retrieved articles
        for article in results:
         # Extract and format information from the article
            article_id = article.pubmed_id
            article_doi = article.doi
            title = article.title
            authors = article.authors
            journal_title = article.journal
            journal_pii = article.journal_issue
            if article.keywords:
                if None in article.keywords:
                    article.keywords.remove(None)
                keywords = '", "'.join(article.keywords)
            publication_date = article.publication_date

            d = publication_date.strftime("%Y %b %d;")

            # Extract the author list from the authors dictionary
            author_list = ""

            for author_entry in authors:
                if author_entry.get("lastname") is not None: # This is necessary, because sometimes there are "collective authors", ie. Care-PF
                    #author_list = author_list + author_entry.get("lastname") + ", " + author_entry.get("firstname")[0] + "., "
                    author_list = author_list + author_entry.get("lastname") + ", " 
                    if author_entry.get("initials") is not None:
                        author_list = author_list + author_entry.get("initials") + "., "
                else:
                    if author_entry.get("collective_name") is not None:
                        author_list = author_list + author_entry.get("collective_name") + "., "

            author_list = author_list[:-2] 
            
            formatted_citation = author_list + " " + title + " " + journal_title + " " + str(d) + str(journal_pii) + " doi: " + str(article_doi) + " PMID: " + str(article_id)
            citation.append(formatted_citation)
    
    # Remove duplicate citations
    citation_duplicates_removed = list(dict.fromkeys(citation))

    #with open('output.csv','w', encoding="utf-8", newline="") as result_file:
    #    wr = csv.writer(result_file, dialect='excel')

    #    for item in citation_duplicates_removed:
    #        wr.writerow([item])

    return citation_duplicates_removed

def write_citations_to_csv(citationlist):

    # Write the citations to an excel file (csv)
    with open('output.csv','w', encoding="utf-8", newline="") as result_file:
        wr = csv.writer(result_file, dialect='excel')

        for item in citationlist:
            wr.writerow([item])
    
    return result_file

# with open('output_duplicates_removed.csv','w', encoding="utf-8", newline="") as result_file:
#     wr = csv.writer(result_file, dialect='excel')

#     for item in citation_duplicates_removed:
#         wr.writerow([item])