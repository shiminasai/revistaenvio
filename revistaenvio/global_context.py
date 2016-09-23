# -*- coding: utf-8 -*-
from django.utils import translation
from revista.models import Revistas

def years_archive(request):
    cur_language = translation.get_language()
    if cur_language == 'en':
        years = []
        for en in Revistas.objects.filter(ididioma='en').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year = list(sorted(set(years)))
        all_year.append(('Choose one year','Choose one year'))
        
    else:
        years = []
        for en in Revistas.objects.filter(ididioma='es').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year = list(sorted(set(years)))
        all_year.append(('Escoja un año','Escoja un año'))

    return {'all_year':all_year}