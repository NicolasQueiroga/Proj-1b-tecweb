from django.shortcuts import render, redirect
from .models import Note, Tag


def index_note(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})

def index_tag(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tags.html', {'tags': tags})

def sorted_tag(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    sorted_notes = Note.objects.filter(tag=tag)
    return render(request, 'sorted/sorted.html', {'notes': sorted_notes})


def upload_note(request):
    if request.method == 'POST':
        note = Note()
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        tag_name = request.POST.get('tag')
        tag, create = Tag.objects.get_or_create(name=tag_name)
        if create:
            tag.save()
        note.tag = tag

        note.save()
        return redirect('index')


def update_note(request, note_id):
    tag_name = request.POST.get('tag')
    tag, create = Tag.objects.get_or_create(name=tag_name)
    if create:
        tag.save()
    Note.objects.filter(pk=note_id).update(title=request.POST.get('title'), content=request.POST.get('content'), tag=tag) 
    return redirect('index')


def delete_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return redirect('index')
    note_sel.delete()
    return redirect('index')

def delete_tag(request, tag_id):
    tag_id = int(tag_id)
    try:
        tag_sel = Tag.objects.get(id=tag_id)
    except Note.DoesNotExist:
        return redirect('index')
    tag_sel.delete()
    return redirect('tags')

