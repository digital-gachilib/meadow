from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView
import login.views as login_views
import books.views as book_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("books/", book_views.ListBooks.as_view(), name='books'),
    path('login/', login_views.LoginView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
