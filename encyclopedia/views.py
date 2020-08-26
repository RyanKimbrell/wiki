from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def random_page(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return HttpResponseRedirect(reverse("display_entry", args=[title]))


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    success = util.save_new_page(title, content)
    if success:
        markdowner = Markdown()
        body_text = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "body": body_text
        })
    else:
        return render(request, "encyclopedia/alreadyexists.html")


def save_edit(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    util.save_entry(title, content)
    return HttpResponseRedirect(reverse("display_entry", args=[title]))


def edit_page(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/editpage.html",{
        "title": title,
        "content": entry
    })


def display_entry(request, title):
    entry = util.get_entry(title)
    if entry == None:
        return render(request, "encyclopedia/error.html")
    else:
        markdowner = Markdown()
        body_text = markdowner.convert(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "body": body_text
        })


def search(request):
    title = request.POST.get("q")
    entry = util.get_entry(title)
    if entry == None:
        return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries(),
        "search_query": title
    })
    else:
        markdowner = Markdown()
        body_text = markdowner.convert(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "body": body_text
        })


def create_new_page(request):
    return render(request, "encyclopedia/newpage.html")