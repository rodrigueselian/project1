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
        return render(request, "encyclopedia/error.html", {
            "error": "notfound"
        })

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
            return render(request, "encyclopedia/error.html", {
                "error": "noresults"
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "results": result
            })
    else:
        return redirect('title', title=query)

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        entries = util.list_entries()
        title = request.POST["title"]
        for entry in entries:
            if entry == title:
                return render(request, "encyclopedia/error.html", {
                    "error": "exist"
                })
        text = request.POST["text"]
        util.save_entry(title, text)
        return redirect('title', title=title)

def edit(request, title):
    if request.method == "GET":
        text = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "text": text
        })
    else:
        text = request.POST["text"]
        util.save_entry(title, text)
        return redirect('title', title=title)    

def rand(request):
    entries = util.list_entries()
    selected = random.choice(entries)
    return redirect('title', title=selected)