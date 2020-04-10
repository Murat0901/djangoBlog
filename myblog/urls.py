from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.BlogList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
