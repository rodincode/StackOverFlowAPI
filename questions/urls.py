from django.urls import path
from . import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
	path('',views.indexview,name='index'),
	path("query",views.queryview,name="query"),
	path('api',views.QuestionsAPIView.as_view(),name="api"),
    ]


