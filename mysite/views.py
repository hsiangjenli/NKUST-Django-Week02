from django.shortcuts import render, redirect
from django.http import HttpResponse
import random, datetime
from mysite import models

def index(request):
	posts = models.Post.objects.all()
	return render(request,"index.html",locals())

def lotto(request):
	numbers = [n for n in range(1,43)]
	random.shuffle(numbers)
	spec = numbers[6]
	lotto = numbers[:6]
	return render(request, "lotto.html", locals())

def date(request):
	now = datetime.datetime.now()
	return HttpResponse("<h1 style='font-family:微軟正黑體;'>現在時刻：{}</h1><hr>".format(now))

def candlestick(request):
	
	return render(request,"candlestick.html",locals())

def play(request, id):
	try:
		post = models.Post.objects.get(id = int(id))
		return render(request, "play.html", locals())
	except:
		return redirect("/")
	