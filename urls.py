from django.urls import path
from .views import *

urlpatterns=[
    path('contactupload', contactupload),
    path('contactdisplay', contactdisplay),
    path('contactupdate<int:id>', contactupdate),
    path('contactdelete<int:id>', contactdelete),
    path('calculator', calculator),
    path('passwordgenerator', passwordgenerator),

]