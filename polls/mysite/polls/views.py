from django.shortcuts import render, redirect
from .models import Question,Choice, NameForm
from django.views.generic import ListView, DetailView
# Create your views here.
def index(request) :
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

# class IndexView(ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        pass #"Question does not exist" #TODO: SEARCH
    return render(request, 'polls/detail.html', {'question': question})

class DetailView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = Question.objects.get(pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : p,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return redirect('polls:results', question_id =p.id)


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
