from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from api.views import TickerViewSet, UserViewSet

router = DefaultRouter()
router.register(r'watchlist', TickerViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token)

]
