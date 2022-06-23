from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter
from api.views import AuthorsViewSet, ArticlesViewSet, Register, AuthorSearchWithESViewSet, ArticleSearchWithESViewSet


route = DefaultRouter()
route.register('authors', AuthorsViewSet, basename='authors')
route.register('articles', ArticlesViewSet, basename='articles')
route.register(r'es/author', AuthorSearchWithESViewSet, basename="es_search_author")
route.register(r'es/articles', ArticleSearchWithESViewSet, basename="es_search_article")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('api/register/', Register.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

