from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Data
from django.utils import timezone
from .forms import Queryform
import requests
from .serializers import QuestionsSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import UserMinThrottle,UserDayThrottle

class QuestionsAPIView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = QuestionsSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes= [IsAuthenticated]
    throttle_classes = [AnonRateThrottle,UserMinThrottle,UserDayThrottle]

def indexview(request):
    return render(request,"questions/index.html")

def queryview(request):
    questions_txt = []
    quota = 0
    if request.method == 'POST':
            form = Queryform(request.POST)
            if form.is_valid():
                    form.save()
                    print(Data.objects.all())
                    scope = "https://api.stackexchange.com/2.2/search/advanced"
            
                    params = {
                        "page": request.POST['page'],
                        "pagesize": request.POST['pagesize'],
                        "fromdate": request.POST["fromdate"],
                        "todate": request.POST['todate'],
                        "order": request.POST['order'],
                        "sort": request.POST['sort'],
                        "min": request.POST['min'],
                        "max": request.POST['max'],
                        "q": request.POST['q'],
                        "accepted": request.POST.get('accepted', False),
                        "answers": request.POST['answers'],
                        "body": request.POST['body'],
                        "closed": request.POST.get('closed', False),
                        "migrated": request.POST.get('migrated', False),
                        "notice": request.POST.get('notice', False),
                        "nottagged": request.POST['nottagged'],
                        "tagged": request.POST['tagged'],
                        "title": request.POST['title'],
                        "user": request.POST['user'],
                        "url": request.POST['url'],
                        "views": request.POST['views'],
                        "wiki": request.POST.get('wiki', False),
                        "site": "stackoverflow"
                    }
                    
                    response = requests.get(scope,params=params)
                    print(response.json())
                    questions = response.json()['items']
                    print(response.url)
                    #print(questions)
                    
                    # Print the title of the question
                    for index, question in enumerate(questions):
                        pretty = "{}. {}\n".format(index + 1, question["title"])
                        print(pretty)
                        questions_txt.append(pretty)
                        # Print remaining quota
                    quota = "\nYou have {} requests left today.".format(response.json()["quota_remaining"])
                    print("\nYou have {} requests left today.".format(response.json()["quota_remaining"]))

    # if a GET (or any other method) we'll create a blank form 
    else:
        form = Queryform()

    context = {'form':form,'question':questions_txt,'quota':quota}
    return render(request, 'questions/query.html', context)

def Gameview(request):
    if request.method == 'POST':
           # create a form instance and populate it with data from the request:
            form = Queryform(request.POST)
            # check whether it's valid:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('Soham')

    # if a GET (or any other method) we'll create a blank form 
    else:
        form2 = Feedbackform()

    return render(request,"questions/Game.html",{'form2': form2})

    




