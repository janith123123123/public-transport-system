from django.shortcuts import render
from rest_framework import viewsets
from .models import customUser, PaymentType, RechargHistory, CardState, TravelPlanState, CardCategory, Rout, Destination, Card, Plan, TravelPlan, InterchangingPoint
from .serializers import UserSerializer, PaymentTypeSerializer, RechargHistorySerializer, CardStateSerializer, TravelPlanStateSerializer, CardCategorySerializer, RoutSerializer, DestinationSerializer, CardSerializer, PlanSerializer, TravelPlanSerializer, InterchangingPointSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = customUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
    
class RechargHistoryViewSet(viewsets.ModelViewSet):
    queryset = RechargHistory.objects.all()
    serializer_class = RechargHistorySerializer
    permission_classes = [IsAuthenticated]
    
class CardStateViewSet(viewsets.ModelViewSet):
    queryset = CardState.objects.all()
    serializer_class = CardStateSerializer
    permission_classes = [IsAuthenticated]
    
class TravelPlanStateViewSet(viewsets.ModelViewSet):
    queryset = TravelPlanState.objects.all()
    serializer_class = TravelPlanStateSerializer
    permission_classes = [IsAuthenticated]
    
class CardCategoryViewSet(viewsets.ModelViewSet):
    queryset = CardCategory.objects.all()
    serializer_class = CardCategorySerializer
    permission_classes = [IsAuthenticated]
    
class RoutViewSet(viewsets.ModelViewSet):
    queryset = Rout.objects.all()
    serializer_class = RoutSerializer
    permission_classes = [IsAuthenticated]
    
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)
    
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    
class TravelPlanViewSet(viewsets.ModelViewSet):
    queryset = TravelPlan.objects.all()
    serializer_class = TravelPlanSerializer
    permission_classes = [IsAuthenticated]
    
class InterchangingPointViewSet(viewsets.ModelViewSet):
    queryset = InterchangingPoint.objects.all()
    serializer_class =InterchangingPointSerializer
    permission_classes = [IsAuthenticated]


