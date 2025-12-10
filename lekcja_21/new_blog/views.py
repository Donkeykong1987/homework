from django.shortcuts import render
from .models import Entry, Blog, Author
from django.db.models import Count

def entry_list_view(request):
    
    all_entries = Entry.objects.select_related('blog').prefetch_related('authors').filter(rating__gt=7).order_by('-rating')

    context = {
        'entries': all_entries,
    }
    
    return render(request, 'new_blog/entry_list.html', context)

def search_list_view(request):
    query = request.GET.get('q', '')

    if query:

        search = Entry.objects.filter(headline__icontains=query).order_by('-rating')
    else:
            
        search = Entry.objects.all().order_by('-rating')
        
    context = {
        'search': search,
        'query' : query,
    }
    
    return render(request, 'new_blog/search.html', context)



def authors_list_view(request):
    all_authors = Author.objects.all()

    context = {
        'authors' : all_authors
        }

    return render(request, 'new_blog/authors_list.html', context)

def blog_detail_view(request, blog_id):
    """Widok szczegółów bloga z jego wpisami"""
    try:
        blog = Blog.objects.get(id=blog_id)
        blog_entries = Entry.objects.filter(blog=blog).prefetch_related('authors').order_by('-pub_date')
        
        context = {
            'blog': blog,
            'entries': blog_entries,
            'total_comments' : total_comments,
        }
        return render(request, 'new_blog/blog_detail.html', context)

    except Blog.DoesNotExist:
        # W prawdziwej aplikacji użylibyśmy Http404 lub get_object_or_404
        context = {'error': 'Blog nie został znaleziony'}
        return render(request, 'new_blog/error.html', context)

def author_detail_views(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        author_details = Entry.objects.filter(authors=author).prefetch_related('blog').order_by('-pub_date') 

        context = {
            'author' : author,
            'entries' : author_details
        }
        return render(request, 'new_blog/author_detail.html', context)
    
    except:
        context = {'error': 'Autor nie został znaleziony'}
        return render(request, 'new_blog/error.html', context)
    
def authors_sorted(request):
    authors_sorted = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries')

    context = {
        'authors_sorted' : authors_sorted
    }
    return render(request, 'new_blog/authors_sorted.html', context)
# Create your views here.
