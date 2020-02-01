from django.http import HttpResponse
from django.template import loader
from .models import Question

path = r"D:\Users\teacher\PycharmProjects\test_django\django_lesson\polls\templates\polls\index.html"


def index(request):
    template = loader.get_template("polls/index.html")
    context = {
        'items': Question.objects.order_by('-pub_date')[:5],
    }
    return HttpResponse(template.render(context, request))


