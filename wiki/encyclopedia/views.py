from django.shortcuts import render
import markdown2
from . import util
import logging

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getpage(request, title):
    try:
        page = util.get_entry(title)
        text = markdown2.markdown(page)
        return render(request, "encyclopedia/title.html", {
            "page": title,
            "text": text            
        })
    except TypeError:
        return render(request, "encyclopedia/error.html")

def search(request):
    query = request.POST["q"]
    entries = util.list_entries()

    for entry in entries:
        if query.lower() in entry.lower():
            page = util.get_entry(entry)
            text = markdown2.markdown(page)
            
            return render(request, "encyclopedia/title.html", {
                "page": entry,
                "text": text
            })
        
    return render(request, "encyclopedia/error.html")