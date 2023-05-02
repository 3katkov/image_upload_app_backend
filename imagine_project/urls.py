from django.urls import path, include
from django.contrib import admin
from imagine_api import views
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()

router.register(r'user_profiles', views.UserProfileViewSet) # requirment 4

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('plans/', views.PlanList.as_view(), name='plan_create'), 
    # path('images/<int:pk>/temporary_link/', views.TemporaryLinkView.as_view(), name='a') # requirment 4
    path('upload-and-view-images/', views.ImageUploadView.as_view(), name='plan_create'),  # requirment 2
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

