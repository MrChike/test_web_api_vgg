from django.contrib import admin
from django.urls import path, include
# from core.views import test_view -- A new method of importing views
from core import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', views.TestView.as_view(), name='test'),
]
