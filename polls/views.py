from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', {})

def submit_image(request):
	import pdb; pdb.set_trace()
	return render(request, 'polls/index.html', {})