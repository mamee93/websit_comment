from django.urls import path
from .views import all_topic,topic_details

app_name = 'topic_comment'
urlpatterns = [
    path('',all_topic,name='all_topic'),
    path('<int:id>/',topic_details,name='topic_details'),
    #path('<int:id>/edit',topic_edit,name='topic_edit'),

]