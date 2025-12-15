from django.shortcuts import render, get_object_or_404
from .models import Note
from django.core.paginator import Paginator

def notes_list(request):
    notes = Note.objects.all()
    return render(request, "Notatnik/notes_list.html", {"notes": notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "Notatnik/note_detail.html", {"note": note})

def notes_list_view(request):
    all_notes = Note.objects.all()
    paginator = Paginator(all_notes, 3) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    return render(request, 'notes_list.html', {'page_obj': page_obj})