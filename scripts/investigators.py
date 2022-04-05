import pandas as pd

HLI_authorlist = ['''(("Dorscheid D"[Author]) OR ("Dorscheid DR"[Author]) OR ("Dorscheid, Delbert"[Author - Full]))''',
    '''(("Sin DD"[Author]) OR ("Sin, Don"[Author - Full]))''']


# Andrew Krahn
Krahn = '''("Krahn A"[Author]) OR ("Krahn AD"[Author])'''

# Andrew Sandford
Sandford = '''(("Sandford AJ"[Author]) OR ("Sandford A"[Author]) OR ("Sandford AJ"[Investigator]) OR ("Sandford A"[Investigator])) AND ((University of British Columbia[Affiliation]) OR (St Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]) OR (University of Oxford[Affiliation]) OR (Pare P[Author]) OR (He JQ[Author]) OR (Laprise C[Author]) OR (Bossé Y[Author]) OR (Sin DD[Author]) OR (Cookson W[Author]) OR (Tan WC[Author]) OR (Wright FA[Author]))'''

# Andrew Thamboo
Thamboo = '''("Thamboo A"[Author]) OR ("Thamboo AV"[Author])'''

# Bradley Quon
Quon = '''(("Quon BS"[Author]) OR ("Quon B"[Author]) OR ("Quon, Bradley"[Author - Full]) NOT Dwight-Johnson M[Author]))'''

# Bruce McManus
McManus = '''(("McManus BM"[Author]) OR ("McManus, B"[Author]) OR ("McManus, Bruce"[Author - Full]) NOT (Smith CF[Author]) NOT (Nugent JK[Author]) NOT (Rosenberg S[Author]) NOT (Carle AC[Author]) NOT (Palta M[Author]) NOT (Moody C[Author]) NOT (Rapport MJ[Author]) NOT (Poehlmann J[Author]) NOT (McCormick M[Author]) NOT (Capistran PS[Author]) NOT (Kotelchuck M[Author]) NOT (Dorman DC[Author]) NOT (Gannotti ME[Author]) NOT (Carle A[Author]))'''

# Chris Carlsten
Carlsten = '''Carlsten C[Author]'''

# Chris Ryerson
Ryerson = '''((Ryerson CJ[Author]) OR ((Ryerson C[Author])) AND interstitial) OR (Ryerson Christopher J[Author])'''

# Chun Seow
Seow = '''Seow CY[Author]'''

# David Granville
Granville = '''(("Granville D"[Author]) OR ("Granville DJ"[Author]) OR ("Granville David"[Author])) AND ((University of British Columbia[Affiliation]) OR (The Scripps Research Institute[Affiliation]) OR (James Hogg Research Centre[Affiliation]) OR (St Paul's Hospital[Affiliation]))'''

# Decheng Yang
DCYang = '''(("Yang DC"[Author]) OR ("Yang D"[Author]) OR ("Yang, Decheng"[Author - Full])) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (St. Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Delbert Dorscheid
Dorscheid = '''("Dorscheid D"[Author]) OR ("Dorscheid DR"[Author]) OR ("Dorscheid, Delbert"[Author - Full])'''

# Denise Daley
Daley = '''(("Daley DD"[Author]) OR ("Daley D"[Author]) OR ("Daley, Denise"[Author - Full]) OR ("Daley D"[Investigator])) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (St. Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Don Sin
Sin = '''(("Sin DD"[Author]) OR ("Sin, Don"[Author - Full])) OR ("Sin, Don D"[Investigator])) OR (Sin, Don [Investigator]))'''

# Gordon Francis
Francis = '''(("Francis GA"[Author]) OR ("Francis, Gordon"[Author - Full])) AND ((University of British Columbia[Affiliation]) OR (University of Alberta[Affiliation]) OR (St. Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]) OR (University of Washington[Affiliation]) OR (Wiegman A[Author]) OR (Ur E[Author]) OR (Heinecke JW[Author]) OR (Leiter LA[Author]) OR (Garver WS[Author]) OR ("The Canadian journal of cardiology"[Journal]) OR (Couture P[Author]) OR (Auwerx J[Author]) OR (Taher TH[Author]) OR (Richards WR[Author])) NOT (Kappos L[Author])'''

# Graeme Koelwyn
Koelwyn = '''("Koelwyn G"[Author]) OR ("Koelwyn GJ"[Author])'''

# Honglin Luo
Luo = '''(("Luo H"[Author]) AND ("Centre for Heart Lung Innovation"[Affiliation] OR "St. Paul's Hospital"[Affiliation] OR "James Hogg Research Centre"[Affiliation]) NOT ("university of georgia"[Affiliation] OR "the chinese university of hong kong"[Affiliation]))'''

# James Hogg
Hogg = '''(("Hogg JC"[Author]) OR ("Hogg JC"[Investigator])) AND ("Centre for Heart Lung Innovation"[Affiliation] OR "St. Paul's Hospital"[Affiliation] OR "James Hogg Research Centre"[Affiliation])'''

# James Russell
Russell = '''((Russell JA[Author]) AND (Russell J[Author])) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (University of British Columbia[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Janice Leung
Leung = '''((Leung JM[Author]) OR (Leung Janice[Author]) OR (Leung J[Author])) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (University of British Columbia[Affiliation]))'''

# John Boyd
Boyd = '''(("Boyd JH"[Author]) OR ("Boyd J"[Author]) OR ("Boyd, John"[Author - Full])) AND ((St. Paul’s Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation])) NOT (Jade Boyd[Author])'''

# Jonathon Leipsic
Leipsic = '''(Leipsic J[Author] or Leipsic JA[Author])'''

# Jordan Guenette
Guenette = '''(("Guenette JA"[Author]))'''

# Keith Walley
Walley = '''(("Walley KR"[Author]) OR ("Walley K"[Author]) OR ("Walley, Keith"[Author - Full]))'''

# Kelly McNagny
McNagny = '''(("McNagny KM"[Author]) OR ("McNagny, Kelly"[Author - Full]) OR ("McNagny K"[Author]))'''

# Liam Brunham
Brunham = '''(("Brunham LR"[Author]) OR ("Brunham L"[Author]) OR ("Brunham, Liam"[Author - Full]))'''

# Mari DeMarco
DeMarco = '''("DeMarco ML"[Author]) OR ("DeMarco, Mari"[Author - Full])'''

# Michael Allard
Allard = '''(("Allard MF"[Author]) OR ("Allard M"[Author]) OR ("Allard, Michael"[Author - Full])) AND ((University of British Columbia[Affiliation]) OR (St. Paul’s Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Pascal Bernatchez
Bernatchez = '''("Bernatchez P"[Author]) OR ("Bernatchez PN"[Author])'''

# Pat Camp
Camp = '''(("Camp PG"[Author]) OR ("Camp P"[Author] and pulmonary[All fields]) OR ("Camp, Pat"[Author - Full]) OR ("Camp, Patricia"[Author - Full])) AND ((University of British Columbia[Affiliation]) OR (Centre for Heart Lung Innovation[Affiliation]) OR (St. Paul’s Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# S.F. Paul Man
Man = '''("Man SFP"[Author])'''

# Peter Pare
Pare = '''("Pare PD"[Author])'''

# Raymond Ng
Ng = '''(("Ng RT"[Author]) OR ("Ng R"[Author])) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (St. Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Scott Tebbutt
Tebbutt = '''(Tebbutt SJ[Author])'''

# Stephanie Sellers
Sellers = '''(Sellers S[Author] OR Sellers SL[Author]) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (St. Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Stephan van Eeden
vanEeden = '''("van Eeden SF"[Author]) OR ("van Eeden S"[Author]) OR ("van Eeden, Stephan"[Author - Full]) AND ((Centre for Heart Lung Innovation[Affiliation]) OR (St Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Tillie Hackett
Hackett = '''(Hackett TL[Author])'''

# Wan-Cheng Tan
Tan = '''(("Tan WC"[Author]) OR ("Tan W" [Author]) OR ("WC Tan"[Author])) AND ((Centre for Heart Lung Innovation[Affiliation] OR (St Paul's Hospital[Affiliation]) OR (James Hogg Research Centre[Affiliation]))'''

# Ying Wang
Wang = '''(33792344
32541024
32282248
31988506
31116606
30786740
29440201
25463481
24608441
24735886
24115032
23471235
22941940
22024251
22116097
21646389
21545834
20164120
20181797
)'''

# Zachary Laksman
Laksman = '''("Laksman, Zachary"[Author - Full]) OR ("Laksman Z"[Author]) OR ("Laksman ZW"[Author]) OR ("Laksman ZWM"[Author])'''

all_PIs = [Krahn, Sandford, Thamboo, Quon, McManus, Carlsten, Ryerson, Seow, Granville, DCYang, Dorscheid, Daley, Sin, Francis, Koelwyn, Luo, Hogg, Russell, Leung, Boyd, Leipsic, Guenette, Walley, McNagny, Brunham, DeMarco, Allard, Bernatchez, Camp, Man, Pare, Ng, Tebbutt, Sellers, vanEeden, Hackett, Tan, Wang, Laksman]
all_PIs_listofstr = ['Krahn', 'Sandford', 'Thamboo', 'Quon', 'McManus', 'Carlsten', 'Ryerson', 'Seow', 'Granville', 'DCYang', 'Dorscheid', 'Daley', 'Sin', 'Francis', 'Koelwyn', 'Luo', 'Hogg', 'Russell', 'Leung', 'Boyd', 'Leipsic', 'Guenette', 'Walley', 'McNagny', 'Brunham', 'DeMarco', 'Allard', 'Bernatchez', 'Camp', 'Man', 'Pare', 'Ng', 'Tebbutt', 'Sellers', 'vanEeden', 'Hackett', 'Tan', 'Wang', 'Laksman']

all_PIs_table = [('Krahn', Krahn),
                ('Sandford', Sandford), 
                ('Thamboo', Thamboo),
                ('Quon', Quon),
                ('McManus', McManus), 
                ('Carlsten', Carlsten),
                ('Ryerson', Ryerson),
                ('Seow', Seow),
                ('Granville', Granville),
                ('DCYang', DCYang),
                ('Dorscheid', Dorscheid),
                ('Daley', Daley),
                ('Sin', Sin), 
                ('Francis', Francis),
                ('Koelwyn', Koelwyn),
                ('Luo', Luo),
                ('Hogg', Hogg),
                ('Russell', Russell),
                ('Leung', Leung),
                ('Boyd', Boyd),
                ('Leipsic', Leipsic),
                ('Guenette', Guenette),
                ('Walley', Walley),
                ('McNagny', McNagny),
                ('Brunham', Brunham),
                ('DeMarco', DeMarco),
                ('Allard', Allard), 
                ('Bernatchez', Bernatchez),
                ('Camp', Camp), 
                ('Man', Man), 
                ('Pare', Pare),
                ('Ng', Ng), 
                ('Tebbutt', Tebbutt), 
                ('Sellers', Sellers),
                ('vanEeden', vanEeden),
                ('Hackett', Hackett),
                ('Tan', Tan), 
                ('Wang', Wang),
                ('Laksman', Laksman)]

all_PIs_DfObj = pd.Series(all_PIs, index = all_PIs_listofstr)