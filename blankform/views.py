__author__ = 'taksenov'
# coding=utf-8

# imports
from django.core.context_processors import csrf
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.template import Context, RequestContext
from blankform.models import clientsanswers, clientsession, question, answer
from django.http import HttpResponseRedirect

from django.contrib.messages.tests.urls import ContactForm



# Вывод меню для выбора среди всех оцифрованных документов
def blankForm(request):

    all_questions = connection.cursor()
    all_questions.execute ("""
        SELECT q.*
        FROM   blankform_question q
        ;
    """)
    result_all_questions = all_questions.fetchall()

    all_answers = connection.cursor()
    all_answers.execute ("""
        SELECT * FROM   blankform_answer;
    """)
    result_all_answers = all_answers.fetchall()
    request.session._get_or_create_session_key()
    my_session = request.session.session_key

    if my_session in clientsession.objects.all().values_list('clientsession', flat=True):
        error_bool = True
        error_text = 'Вы уже участвовали в оценке качества обслуживания нашего учреждения. Мы очень благодарны вам за ранее оставленный отзыв. Если вы хотите оставить новый отзыв, то попробуйте сделать это в следующий раз.'
    else:
        error_bool = False
        error_text = ''

    # Внимание! Если хочешь не иметь проблем с CSRF
    # то везде используй RequestContext!
    templ = get_template('blankform.html')
    html = templ.render(
                        RequestContext(request,
                                       {
                                       'result_all_answers':  result_all_answers,
                                       'result_all_questions': result_all_questions,
                                       'my_session': my_session,
                                       'user': request.user,
                                       'error_bool': error_bool,
                                       'error_text': error_text
                                       }
                                       )
                       )
    return HttpResponse(html)

# Вывод результатов отправки отзыва и заполнение БД
def comment(request):
    if not request.method == 'POST':
        raise Http404

    errors = []
    error = ''
    my_session = request.session.session_key

    all_questions = connection.cursor()
    all_questions.execute ("""
        SELECT q.*
        FROM   blankform_question q
        ;
    """)
    result_all_questions = all_questions.fetchall()

    all_answers = connection.cursor()
    all_answers.execute ("""
        SELECT * FROM   blankform_answer;
    """)
    result_all_answers = all_answers.fetchall()

    if request.method == 'POST':
        if not request.POST.get('answer1', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer2', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer3', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer4', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer5', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer6', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer7', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer8', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer9', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer10', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer11', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('answer12', ''):
            errors.append('Произошла ошибка! Необходимо ответить на все вопросы анкеты.')
            error = 'Произошла ошибка! Необходимо ответить на все вопросы анкеты.'
        if not request.POST.get('customcomment', ''):
            customcomment_text = ''
        else:
            customcomment_text = request.POST['customcomment']
        if not errors:

            clientsession__data = clientsession(
                clientsession = my_session,
                customcomment = customcomment_text
                )
            clientsession__data.save()

            for question_var in result_all_questions:
                answer__text = request.POST['answer' + str(question_var[0]) ]
                question_id_var = question.objects.get(pk=question_var[0])
                if u'Удовлетворен' in answer__text:
                    answer__id_var = answer.objects.get(pk=1)
                elif u'Частично удовлетворен' in answer__text:
                    answer__id_var = answer.objects.get(pk=2)
                elif u'Не удовлетворен' in answer__text:
                    answer__id_var = answer.objects.get(pk=3)
                clientsanswers__data = clientsanswers(
                    client_id = clientsession__data,
                    question_id = question_id_var,
                    answer_id = answer__id_var
                    )
                clientsanswers__data.save()

            templ = get_template('commentform.html')
            html = templ.render(RequestContext(
                                         request,
                                         {
                                         'user': request.user,
                                         }))
            return HttpResponse(html)


        templ = get_template('blankform.html')
        html = templ.render(
                            RequestContext(request,
                                           {
                                           'result_all_answers':  result_all_answers,
                                           'result_all_questions': result_all_questions,
                                           'my_session': my_session,
                                           'user': request.user,
                                           'errors': errors,
                                           'error': error,
                                           }
                                           )
                           )
        return HttpResponse(html)

















