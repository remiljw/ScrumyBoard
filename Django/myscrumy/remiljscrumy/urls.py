from django.urls import include,path
from remiljscrumy import views

app_name = 'remiljscrumy'


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
]



