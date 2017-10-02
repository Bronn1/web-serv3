# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,  Http404

from django.core.paginator import Paginator 

from qa.models import Question, Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, num ):
	q = get_object_or_404(Question, id=num)
	
	return render(request, 'question.html', { 'titel': 'Popular', })
	
def popular(request):
	pass

def main(request):
	pass
