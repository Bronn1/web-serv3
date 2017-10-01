# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models


class QuestionManager(models.Manager):

	def new():
		return Question.objects.order_by('added_at')

	def popular():
		return Question.objects.order_by('rating')


class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(default= 0, max_length = 255)
	text = models.TextField(default = "")
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, null = True, 
				on_delete = models.DO_NOTHING)
	likes = models.ManyToManyField(User, related_name = 'question_like_user')
	
	def __unicode__(self):
		return self.titel

	def get_url(self):
		return "/question/%d/" %self.id


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question, null = True,  on_delete = models.SET_NULL)
	author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
	
	def __unicode__(self):
		return self.text


