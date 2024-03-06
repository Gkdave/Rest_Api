from django.http import HttpResponse,JsonResponse


def home(request):
    print('home page requested')
    friends=['ankit','ravi','uttam']
    return JsonResponse(friends,safe=False)