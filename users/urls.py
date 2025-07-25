from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from .views import SecureLoginView, SecureLogoutView, UserRoleView, CustomRegisterView, NotificationPreferencesView, NotificationViewSet, PasswordResetRequestView, PasswordResetConfirmView
from rest_framework.routers import DefaultRouter

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        from django.middleware.csrf import get_token
        token = get_token(request)
        return JsonResponse({'csrfToken': token})

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('login/', SecureLoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/role/', UserRoleView.as_view(), name='user_role'),
    path('registration/', CustomRegisterView.as_view(), name='registration'),
    path('csrf/', GetCSRFToken.as_view(), name='csrf'),
    path('notification-preferences/', NotificationPreferencesView.as_view(), name='notification-preferences'),
    path('password/forgot/', PasswordResetRequestView.as_view(), name='password_forgot'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include(router.urls)),
]
