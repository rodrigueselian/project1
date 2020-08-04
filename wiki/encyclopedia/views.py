from django.shortcuts import render
import markdown2
from . import util


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