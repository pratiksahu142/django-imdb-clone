from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    StreamPlatformVS,
)

router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    # path("list/", movie_list, name="movie-list"),
    # path("<int:pk>", movie_details, name="movie-details"),
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="watchlist-detail"),
    # Below 2 routes can be done using router
    # path("stream/", StreamPlatformAV.as_view(), name="stream-platform"),
    # path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream-detail"),
    # Using router
    path("", include(router.urls)),
    path("stream/<int:pk>/review-create", ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
