from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


def index(request):
    template = loader.get_template('pradeepan_portfolio/index.html')
    context = {
        'latest_question_list': "",
    }
    # A shortcut: render()
    # return render(request, 'polls/index.html', context)
    return HttpResponse(template.render(context, request))
