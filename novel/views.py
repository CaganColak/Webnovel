from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Novel, Chapter

# Ana sayfa
def index(request):
    novels = Novel.objects.all()
    return render(request, "index.html", {"novels": novels})

# Roman detay
def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    chapters = novel.chapters.order_by("-number")
    return render(request, "novel_detail.html", {
        "novel": novel,
        "chapters": chapters
    })

def chapter_detail(request, novel_id, number):
    novel = get_object_or_404(Novel, id=novel_id)
    chapter = get_object_or_404(Chapter, novel=novel, number=number)

    prev_chapter = Chapter.objects.filter(novel=novel, number__lt=chapter.number).order_by('-number').first()
    next_chapter = Chapter.objects.filter(novel=novel, number__gt=chapter.number).order_by('number').first()

    return render(request, "chapter_detail.html", {
        "novel": novel,
        "chapter": chapter,
        "prev_chapter": prev_chapter,
        "next_chapter": next_chapter,
    })
@login_required
def chapter(request, id):
    chapter = get_object_or_404(Chapter, id=id)
    return render(request, "chapter.html", {"chapter": chapter})
# Kayıt olma
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
