from django.shortcuts import render, redirect
import markdown2
from . import util
import logging
import random

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
    search = util.get_entry(query)
    if search == None:
        result = []
        entries = util.list_entries()
        for entry in entries:
            if query.lower() in entry.lower():
                result.append(entry)
        if result == []:
            return render(request, "encyclopedia/error.html")
        else:
            return render(request, "encyclopedia/search.html", {
                "results": result
            })
    else:
        return redirect('title', title=query)

def rand(request):
    entries = util.list_entries()
    selected = random.choice(entries)
    return redirect('title', title=selected)