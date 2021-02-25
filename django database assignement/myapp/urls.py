from django.urls import path
from.import views


urlpatterns =[
    path('',views.index , name='index'),
    path('detail1',views.detail1 , name='detail1'),
    path('detail2',views.detail2 , name='detail2'),

]
