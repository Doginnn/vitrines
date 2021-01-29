from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from vitrines.vitrines.views import EventoViewSet, ItemViewSet, CityViewSet, CountryViewSet, CategoryViewSet

# End Points from API
api_router = routers.DefaultRouter()
api_router.register(r'eventos', EventoViewSet)
api_router.register(r'city', CityViewSet)
api_router.register(r'country', CountryViewSet)
api_router.register(r'category', CategoryViewSet)

# End Points solicitados pela SBTur
api_router.register(r'vitrines', ItemViewSet)

# End Points from REST_FRAMEWORK_NESTED
eventos_router = routers.NestedDefaultRouter(api_router, r"eventos", lookup='evento')
eventos_router.register(r"items", ItemViewSet, basename="evento-items")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(api_router.urls)),
    path('vitrines/', include(api_router.urls)),
    path('eventos', include(api_router.urls)),
    path('city/', include(api_router.urls)),
    path('country/', include(api_router.urls)),
    path('category/', include(api_router.urls)),
]
