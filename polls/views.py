from django.shortcuts import render, redirect
from .models import Poll, Choice, QuestionType, Answer, AnswerQuestion, AnswerChoice
from .forms import TextForm, MultipleForm, SingleForm
from django.shortcuts import get_object_or_404
from .tasks import create_pdf

from django.contrib.auth.decorators import login_required

def polls_list(requset):
    polls = Poll.objects.filter(visible=True)
    auth = requset.user.is_superuser
    return render(requset, 'polls/polls_list.html', {'polls': polls, 'auth': auth})

def poll_page(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    questions = poll.get_questions()
    if request.method == 'POST':
        data = dict(request.POST)
        answer = Answer(poll=poll, user_name=data['name'][0])
        create_pdf.delay(answer.user_name)
        answerquestions = []
        for q in questions:
            answerquestions.append(AnswerQuestion(question=q, answer=answer))
            if q.type == QuestionType.TEXT:
                answerquestions[-1].text = data[f'{q.pk}']
        answerchoices = []
        for aq in answerquestions:
            answerchoices += [AnswerChoice(answerquestion=aq, choice=Choice.objects.get(pk=int(e)))
                              for e in data[f'{aq.question.pk}'] if aq.question.type != QuestionType.TEXT]
        answer.save()
        [aq.save() for aq in answerquestions]
        [ac.save() for ac in answerchoices]
        return redirect('end_page')

    df = {}
    for q in questions:
        df[q] = get_form(q)
    nameform = TextForm('Введите имя', 'name')
    return render(request, 'polls/poll_page.html', {'poll': poll, 'question_form': df.items(), 'nameform': nameform})

def get_form(question):
    if question.type == QuestionType.TEXT:
        return TextForm(question, f'{question.pk}')
    elif question.type == QuestionType.SINGLE:
        return SingleForm([(c.pk, c) for c in question.get_choices()], question, f'{question.pk}')
    return MultipleForm([(c.pk, c) for c in question.get_choices()], question, f'{question.pk}')

def end_page(request):
    return render(request, 'polls/end_page.html')

@login_required
def answer_list(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    answers = Answer.objects.filter(poll=poll)
    return render(request, 'polls/answers_list.html', {'answers': answers, 'poll': poll})

@login_required
def answer_page(request, poll_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answerquestions = answer.get_answerquestions()
    df = {}
    for aq in answerquestions:
        if len(aq.text):
            df[aq.question] = [(aq.text, True)]
        else:
            df[aq.question] = aq.get_choices()

    return render(request, 'polls/answer_page.html', {'answer': answer, 'question_answers': df.items()})
# Create your views here.
