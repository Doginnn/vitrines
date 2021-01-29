from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from vitrines.vitrines.views import EventoViewSet, ItemViewSet, CityViewSet, CountryViewSet, CategoryViewSet

# Routes from API
api_router = routers.DefaultRouter()
api_router.register(r'eventos', EventoViewSet)
# api_router.register(r'item', ItemViewSet)
api_router.register(r'city', CityViewSet)
api_router.register(r'country', CountryViewSet)
api_router.register(r'category', CategoryViewSet)

# Routes from REST_FRAMEWORK_NESTED
eventos_router = routers.NestedDefaultRouter(api_router, r"eventos", lookup='evento')
eventos_router.register(r"items", ItemViewSet, basename="evento-items")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(api_router.urls)),
    path('item/', include(api_router.urls)),
    path('city/', include(api_router.urls)),
    path('country/', include(api_router.urls)),
    path('category/', include(api_router.urls)),
]

# path('/', tem que me retornar o primeiro e segundo pacote criado "id 1 e id 2"),
# path('/destinos', tem que me retornar o primeiro pacote criado "id 1"),
# path('/sobre', tem que me retornar uma lista vazia "[]"),
