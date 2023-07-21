from rest_framework.routers import SimpleRouter
from GenericViewSet5 import views



router = SimpleRouter()
router.register('books5', views.GenericViewSetBook5,basename='books')
urlpatterns = router.urls