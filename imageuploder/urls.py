
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.userlogin),
    path('logout/', views.userlogout),
    path('delete/<int:id>/', views.userdelete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
