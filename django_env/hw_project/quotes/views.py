from django.shortcuts import render
from quotes.utils import get_data_from_db
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def main(request, page=1):
    db = get_data_from_db()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    top_tags = get_top_tags()
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'top_tags': top_tags})
    
  
@login_required
def add_author(request):
    if request.method == 'POST':
        # 
        
        
        
        pass
    return render(request, 'quotes/add_author.html')


@login_required
def add_quote(request):
    if request.method == 'POST':
        # 
        pass
    return render(request, 'quotes/add_quote.html')


def quotes_by_tag(request, tag):
    db = get_data_from_db()
    quotes = db.quotes.find({"tags": tag})
    return render(request, 'quotes/tag_quotes.html', {'quotes': quotes, 'tag': tag})


def get_top_tags():
    db = get_data_from_db()
    tags = db.quotes.aggregate([
        {"$unwind": "$tags"},
        {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    return [tag['_id'] for tag in tags]



