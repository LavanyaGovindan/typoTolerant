# Create your views here.
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Company
from difflib import get_close_matches

patterns = ['guvi geek network', 'maximl labs', 'ynos venture', 'swapeco','agnikul cosmos','impensus electronics','doodhbhandaar',
            'rekindle automationcs private limited','ather energy private limited','bigphi technologies']

def closeMatches(patterns, word):
    return get_close_matches(word, patterns)

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Company
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        word = closeMatches(patterns, query)
        print(word[0])
        return Company.objects.filter(
            Q(name__icontains=word[0])
        )
