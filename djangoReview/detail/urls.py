from django.urls import path
from . import views

app_name = 'detail'

urlpatterns = [
    path('<int:game_id>/',views.detail,name="detail")
]
    