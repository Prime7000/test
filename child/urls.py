from django.urls import path
from .views import HomePageView#,PostDetailView,AddPostView,primeview
from django.conf.urls.static import static
from .views import *

app_name = 'child'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('calculus1/', Calculus1.as_view(), name='cal1'),
    path('algebra1/', Algebra1.as_view(), name='alg1'),
    path('probablity1/', Probability1.as_view(), name='pro1'),
    path('statictics1/', Statictics1.as_view(), name='sta1'),
    path('calculus2/', Calculus2.as_view(), name='cal2'),
    path('algebra2/', Algebra2.as_view(), name='alg2'),
    path('probablity2/', Probability2.as_view(), name='pro2'),
    path('statictics2/', Statistics2.as_view(), name='sta2'),
    path('about/', About.as_view(), name='about'),

]