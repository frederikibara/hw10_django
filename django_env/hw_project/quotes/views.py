# from django.shortcuts import render
# from quotes.util import get_data
# from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required


# def main(request, page=1):
#     db = get_data()
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     top_tags = get_top_tags()
#     return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'top_tags': top_tags})
    
  
# @login_required
# def add_author(request):
#     if request.method == 'POST':
#         # 
        
        
        
#         pass
#     return render(request, 'quotes/add_author.html')


# @login_required
# def add_quote(request):
#     if request.method == 'POST':
#         # 
#         pass
#     return render(request, 'quotes/add_quote.html')


# def quotes_by_tag(request, tag):
#     db = get_data()
#     quotes = db.quotes.find({"tags": tag})
#     return render(request, 'quotes/tag_quotes.html', {'quotes': quotes, 'tag': tag})


# def get_top_tags():
#     db = get_data()
#     tags = db.quotes.aggregate([
#         {"$unwind": "$tags"},
#         {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 10}
#     ])
#     return [tag['_id'] for tag in tags]



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AuthorForm, QuoteForm
from .models import Author, Quote

def home(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/home.html', {'quotes': quotes})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'quotes/register.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    quotes = author.quote_set.all()
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})
