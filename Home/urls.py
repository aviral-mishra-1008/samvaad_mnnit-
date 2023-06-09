from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('Backend_Uid/',views.backend, name="u_id")
] 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


