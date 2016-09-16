# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView
from django.utils import translation
from .models import *
import datetime

def set_lang(request, lang_code):
    if not lang_code in ['en', 'es']:
        raise Http404

    next = request.GET.get('next', '/')
    if not next:
        next = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(next)

    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response

class IndexView(ListView):
    template_name = "index.html"
    model = Revistas
    paginate_by = 1

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Revistas.objects.filter(ididioma='en').order_by('-numero')
        else:
            queryset = Revistas.objects.filter(ididioma='es').order_by('-numero')
        return queryset

class DetailArticuloView(DetailView):
    model = Articulos

    def get_context_data(self, **kwargs):
        context = super(DetailArticuloView, self).get_context_data(**kwargs)
        revista = Revistas.objects.get(id=self.object.revista_id)
        context['ultima_revista'] = revista
        context['articulos'] = Articulos.objects.filter(revista_id=revista).exclude(id=self.object.id)
        return context


def busqueda(request, template='revista/busqueda_avanzada.html'):


    return render(request, template, locals())


def busqueda_google(request, template='revista/google_search.html'):
    return render(request, template, locals())


def archivos_revista(request, template='revista/archivos.html', yearr=None):
    cur_language = translation.get_language()
    if cur_language == 'en':
        years = []
        for en in Revistas.objects.filter(ididioma='en').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year = list(sorted(set(years)))
        idioma = 'en'
    else:
        years = []
        for en in Revistas.objects.filter(ididioma='es').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year = list(sorted(set(years)))
        idioma = 'es'

    if yearr is None:
            now = datetime.datetime.now()
            query = Revistas.objects.filter(ididioma=idioma,ano=now.year).order_by('-mes')
    else:
            query = Revistas.objects.filter(ano=yearr,ididioma=idioma).order_by('-numero')

    return render(request, template, locals())
