#!/usr/bin/python
import csv
import sys
import requests

if len(sys.argv) < 3 :
    print("Usage: " + __file__ + " urls_list.csv result.csv")
    sys.exit(2)

file_source = open(sys.argv[1], 'r')
file_dest = open(sys.argv[2], 'w')

csv_source = csv.reader(file_source)
csv_dest = csv.writer(file_dest)
header = ['Source url', 'Expected final url', 'Final url', 'Is redirect correct', 'Redirects count']
csv_dest.writerow(header)
for url_list in csv_source:
    url_source = str(url_list[0])
    url_dest = str(url_list[1])
    req_check = requests.get(url_source)
    url_final = req_check.url
    redir_count = len(req_check.history)
    if url_final != url_dest:
        corr_redir = 'Not correct'
    else:
        corr_redir = 'Correct'
    data = [url_source, url_dest, url_final, corr_redir, redir_count]
    csv_dest.writerow(data)


