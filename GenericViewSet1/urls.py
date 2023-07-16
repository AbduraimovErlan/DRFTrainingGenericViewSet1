from rest_framework.routers import SimpleRouter
from GenericViewSet1 import views

router = SimpleRouter()
router.register('books1', views.GenericViewSetBook1, basename='books')
urlpatterns = router.urls