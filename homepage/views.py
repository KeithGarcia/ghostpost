from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import boastroast
from homepage.forms import AddPostForm

def index(request):
    posts = boastroast.objects.all().order_by("-time_posted")
    return render(request, "index.html", {"posts": posts})

def addpost(request):
    if request.method =="POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            boastroast.objects.create(
                choices=data.get('choices'), 
                post_field=data.get('post_field'),
                )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, "addpost.html", {"form": form})

def roasts(request):
    roasts = boastroast.objects.filter(choices=False).order_by("-time_posted")
    return render(request, "roasts.html", {"roasts": roasts})

def boasts(request):
    boasts = boastroast.objects.filter(choices=True).order_by("-time_posted")
    return render(request, "boasts.html", {"boasts": boasts})

def upvotes(request, up_votes_id):
    upvotes = boastroast.objects.filter(id=up_votes_id).first()
    upvotes.up_votes +=1
    upvotes.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def downvotes(request, down_votes_id):
    downvotes = boastroast.objects.filter(id=down_votes_id).first()
    downvotes.down_votes +=1
    downvotes.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def sortvotes(request):
    sortvotes = sorted(boastroast.objects.all(), key=lambda t:t.votes, reverse=True)
    return render(request, "sortvotes.html", {"sortvotes": sortvotes})