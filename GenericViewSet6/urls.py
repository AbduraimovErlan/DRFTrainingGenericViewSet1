from rest_framework.routers import SimpleRouter
from GenericViewSet6 import views



router = SimpleRouter()
router.register('books6', views.GenericViewSetBook6, basename='books')
urlpatterns = router.urls