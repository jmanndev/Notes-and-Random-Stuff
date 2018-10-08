from lxml import html
import urllib
import requests

URL = "http://goalkicker.com/"

response = requests.get(URL)
sourceCode = response.content
htmlElem = html.document_fromstring(sourceCode)

books = htmlElem.cssselect('[class="bookContainer grow"]')

for book in books:
    urlSuffix = book[0].get('href')
    response = requests.get(URL + urlSuffix)
    sourceCode = response.content
    htmlElem = html.document_fromstring(sourceCode)
    download = htmlElem.cssselect('[id="footer"]')
    pdfTitle = download[0][0].get('onclick')[15:-1]
    
    link = URL + urlSuffix + pdfTitle
    downloadDir = pdfTitle  
    urllib.request.urlretrieve(link, downloadDir) #download the pdf
    print(pdfTitle)
    
    
