from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['full-text']
    wordlist = fulltext.split()
    numofwords = len(wordlist)

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': numofwords, 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
