from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum

def index1(request):
    return HttpResponse('<u>Hello</u>')

def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    # 1-linux 입력
    Curriculum.objects.create(name='linux')
    # 2-python 입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js 입력
    Curriculum(name='python').save()
    # 4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    # curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

    curriculum = Curriculum.objects.all()
    return render(
        request,
        'firstapp/show.html', 
        {'score': 100, 'data': curriculum})

def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)

def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')

def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')

import json
def req_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    return JsonResponse(data)