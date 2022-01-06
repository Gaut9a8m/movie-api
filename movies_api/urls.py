"""movies_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .auth import CustomAuthToken
from hollywood import views
from rest_framework_swagger.views import get_swagger_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# from rest_framework.schemas import get_schema_view

schema_view = get_swagger_view(title='Movie API')

router = DefaultRouter()

router.register('hollywood_api', views.HollywoodViewSet, basename='hollywood')
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    # path("hollywood/",views.HollywoodAPILC.as_view()),
    # path("hollywood/<int:pk>",views.HollywoodAPIRUD.as_view()),
    # path("hollywood/", views.HollywooodApi.as_view(), name="hollywoodmovies"),
    # path("hollywood/<int:id>", views.HollywooodApi.as_view(), name="hollywoodmovie"),
    # path("allmovies/<int:id>", views.movie_data.as_view(), name="movies"),
    # path('callback/', views.index, name='leelelelelelele?'),
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('movieapi/',include(router.urls)),
    path('gettoken/',CustomAuthToken.as_view())

]
