import json

from django.http import HttpResponse
from django.shortcuts import render

from ais.AI_models.Tensorflow_model import Recommend_movie
# Create your views here.
def index(request):
    return render(request, 'index.html')


def recommend_movie_start(request):
    return render(request, 'recommend_movie/start.html', {})


def recommend_movie_form1(request):
    return render(request, 'recommend_movie/form1.html', {})


def recommend_movie_form2(request):
    step1 = int(request.GET['step1'])
    data = {'step1': step1}
    return render(request, 'recommend_movie/form2.html', data)

def recommend_movie_form3(request):
    step1 = int(request.GET['step1'])
    step2 = int(request.GET['step2'])
    data = {'step1': step1, 'step2': step2}
    return render(request, 'recommend_movie/form3.html', data)

def recommend_movie_form4(request):
    step1 = int(request.GET['step1'])
    step2 = int(request.GET['step2'])
    step3 = int(request.GET['step3'])
    data = {'step1': step1, 'step2': step2, 'step3': step3}
    return render(request, 'recommend_movie/form4.html', data)

def recommend_movie_form5(request):
    step1 = int(request.GET['step1'])
    step2 = int(request.GET['step2'])
    step3 = int(request.GET['step3'])
    step4 = int(request.GET['step4'])
    data = {'step1': step1, 'step2': step2, 'step3': step3, 'step4': step4}
    return render(request, 'recommend_movie/form5.html', data)

def recommend_movie_end(request):
    step1 = request.GET['step1']
    step2 = request.GET['step2']
    step3 = request.GET['step3']
    step4 = request.GET['step4']
    step5 = request.GET['step5']
    recommend_movie = Recommend_movie()  # 모델 사용
    data = ",".join([step1, step2, step3, step4, step5])
    print('data:', data)

    index = recommend_movie.proc(data)
    print('index:', index)

    return render(request, 'recommend_movie/end.html', {'index': index})


def recommend_movie_end_ajax(request):
    step1 = request.GET['step1']
    step2 = request.GET['step2']
    step3 = request.GET['step3']
    step4 = request.GET['step4']
    step5 = request.GET['step5']
    recommend_movie = Recommend_movie()  # 모델 사용
    data = ",".join([step1, step2, step3, step4, step5])
    print('data:', data)

    index = recommend_movie.proc(data)  # 1 ~ 3 확률이 높은 index 리턴됨.
    print('index:', index)

    content = {
        'index': int(index),
    }
    # 날짜등의 변한 선언: cls=DjangoJSONEncoder
    # return HttpResponse(json.dumps(content, cls=DjangoJSONEncoder), content_type="application/json")
    return HttpResponse(json.dumps(content), content_type="application/json")