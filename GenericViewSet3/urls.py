from GenericViewSet3 import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('books3', views.GenericViewSetBook3, basename='books')
urlpatterns = router.urls