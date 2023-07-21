from rest_framework.routers import SimpleRouter
from GenericViewSet4 import views



router = SimpleRouter()
router.register('books4', views.GenericViewSetBook4, basename='books')
urlpatterns = router.urls
