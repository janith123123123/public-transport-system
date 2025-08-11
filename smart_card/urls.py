from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentTypeViewSet, RechargHistoryViewSet, CardStateViewSet, TravelPlanStateViewSet, TravelModeViewSet, RoutViewSet, DestinationViewSet, CardViewSet, PlanViewSet, TravelPlanViewSet, InterchangingPointViewSet

router = DefaultRouter()

router.register('users',UserViewSet)
router.register('payment-types', PaymentTypeViewSet)
router.register('recharges', RechargHistoryViewSet)
router.register('card-states', CardStateViewSet)
router.register('travel-plan-states',TravelPlanStateViewSet)
router.register('tavel-modes', TravelModeViewSet)
router.register('routs', RoutViewSet)
router.register('destinations', DestinationViewSet)
router.register('cards', CardViewSet)
router.register('plans', PlanViewSet)
router.register('travel-plans', TravelPlanViewSet)
router.register('interchanging-points',InterchangingPointViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]