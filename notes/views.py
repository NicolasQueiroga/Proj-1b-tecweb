from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteCreate
from django.http import HttpResponse


def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})


def upload(request):
    upload = NoteCreate()
    if request.method == 'POST':
        upload = NoteCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload <a href = "{{ url : 'index'}}">here</a>""")


def update_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return redirect('index')
    note_form = NoteCreate(request.POST or None, instance=note_sel)
    if note_form.is_valid():
        note_form.save()
        return redirect('index')
    return render(request, 'notes/index.html', {'upload_form': note_form})


def delete_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return redirect('index')
    note_sel.delete()
    return redirect('index')
