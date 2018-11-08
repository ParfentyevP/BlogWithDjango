from django.http import HttpResponse

def hello(request):
    h = '<h1>Хахахаха это Django! ;))</h1>'
    return HttpResponse('Пишу тут что хочу могу заголовком вот так: ' + h)
