from rest_framework import serializers
from .models import customUser, Card, PaymentType, RechargHistory, CardState, TravelPlanState, TravelMode, Rout, Destination, Plan, TravelPlan, InterchangingPoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'
     
class RechargHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RechargHistory
        fields = '__all__'

class CardStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardState
        fields = '__all__'
        
class TravelPlanStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlanState
        fields = '__all__'
        
class TravelModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelMode
        fields = '__all__'
        
class RoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'
        
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        
class TravelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlan
        fields = '__all__'
        
class InterchangingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterchangingPoint
        fields = '__all__'