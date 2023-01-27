from django.urls import include, path
from rest_framework import routers

from .views import (AdminUserViewSet, CategoryViewSet, CommentViewSet,
                    GenreViewSet, MeDetailsViewSet, ReviewViewSet,
                    SignUpAPIView, TitlesViewSet, TokenAPIView)

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('users', AdminUserViewSet, basename='AdminUser')
router_v1.register('categories', CategoryViewSet, basename='Category')
router_v1.register('genres', GenreViewSet, basename='Genre')
router_v1.register('titles', TitlesViewSet, basename='Title')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/users/me/', MeDetailsViewSet.as_view()),
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignUpAPIView.as_view()),
    path('v1/auth/token/', TokenAPIView.as_view()),
]
