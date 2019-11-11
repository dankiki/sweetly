"""sweetly URL Configuration
"""

from django.urls import path
import sweetly.views as views

urlpatterns = [
    path('shorten/', views.Shortener.as_view({'get': 'empty',
                                              'post': 'shorten'}), name='shorten'),  # noqa: E501
    path('<short_part>/', views.Redirect.as_view({'get': 'redirect'})),
]
