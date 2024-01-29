from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import backend

urlpatterns = [
    path("", views.index, name = "Home"),
    path("About/", views.about, name="About"),
    path("Contact/", views.contact_us, name = "Contact s"),
    path("Submission/", views.sub, name="Submission"),
    path('Success/',views.success,name="success"),
    path('Backend/',views.login,name="backend"),
    path('Verification/',views.article,name="Article"),
    path('search/',views.search,name="search"),
    path('login/',views.login,name="login"),
    path('backend_uid/', views.backend, name='backend')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

