from django.shortcuts import render,redirect  
from django.contrib import messages  
from django.core.paginator import Paginator  
from django.http import HttpResponseNotFound  
from faunadb import query as q  
import pytz  
from faunadb.objects import Ref  
from faunadb.client import FaunaClient  
import hashlib  
import datetime  




client = FaunaClient(secret="SECRET_KEY")  
indexes = client.query(q.paginate(q.indexes()))

from django.conf import settings  
from django.conf.urls.static import static  
from django.urls import path, include  
from . import views  
app_name = "App"  

urlpatterns = [  
 path("", views.login, name="login"),  
 path("login", views.login, name="login"),  
 path("dashboard", views.dashboard, name="dashboard"),  
 path("quiz", views.quiz, name="quiz"),  
 path("register", views.register, name="register"),  
 path("create-quiz", views.create_quiz, name="create-quiz"),  
 path("create-questions", views.create_question, name="create-question"),  
 path("answer-quiz/<slug>", views.answer_quiz, name="answer-quiz"),  
]
