from rest_framework.routers import SimpleRouter
from GenericViewSet2 import views



router = SimpleRouter()
router.register('books2', views.GenericViewSetBook2, basename='books')
urlpatterns = router.urls