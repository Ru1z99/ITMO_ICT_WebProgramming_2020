
from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail, name='detail'),
    path('blog/', views.post_list, name='post_list'),
    path('time/', views.geeks_view),
    path('all_owners/', views.owners_list),
    path('all_cars/', views.CarList.as_view(template_name="cars.html")),
]