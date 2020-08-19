from django.contrib import admin
from django.urls import include, path
from djangodogs import views
import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dogs/<id>/', views.dog_detail, name='dog_detail'),
]
