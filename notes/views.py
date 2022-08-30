from pydoc import describe
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
        title = forms.CharField() 
        description = forms.CharField(widget=forms.Textarea())



def index(request):
    if "notes" not in request.session:
        request.session["notes"] = {}
        
    return render(request, "notes/index.html", {
        "notes": request.session["notes"],
    })

def add(request):

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            request.session.modified = True
            request.session["notes"][title] = description
            

            return HttpResponseRedirect(reverse("notes:index"))

        else:
            return render(request, "notes/add.html", {
                "form": form
            })

    return render(request, "notes/add.html", {
        "form": NewTaskForm()
    })