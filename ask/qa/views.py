# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,  Http404

from django.views.decorators.http import require_GET

from django.core.paginator import Paginator 

from qa.models import Question, Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, num ):
	q = get_object_or_404(Question, id=num)
	
	return render(request, 'question.html', { 'titel': 'Question', })

@require_GET	
def popular(request):
	questions = Question.objects.order_by('-rating').all()
	paginator, page = paginate(request, questions)

	return render(request, 'page1.html', {'questions': page.object_list, 'paginator': paginator,  'page': page,  })

@require_GET
def main(request):
	questions = Question.objects.order_by('-id').all()
	paginator, page = paginate(request, questions)
	
	return render(request, 'page1.html', {'questions': page.object_list, 'paginator': paginator, 'page': page, } )

def paginate(request, qs):
	limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
		
	paginator = Paginator(qs, limit)
	
	page = paginator.page(page)
	
	return paginator, page






