from rest_framework import routers
from .viewsets import BookViewSet,PageViewSet


#Generar rutas para API
router = routers.SimpleRouter()
router.register('books',BookViewSet)
router.register('pages',PageViewSet)

urlpatterns = router.urls