from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings

# Create your models here.

class customUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN  = "Admin" , 'Admin'
        STAFF  = "staff" , 'staff'
        USER  = "user" , 'user'
    
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.USER)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role:
            group, _ = Group.objects.get_or_create(name=self.role)
            self.groups.set([group])
        
    
    def __str__(self):
        if self.role == self.Role.ADMIN:
            return f"Admin - {self.first_name} {self.last_name}"
        elif self.role == self.Role.STAFF:
            return f"Staff - {self.first_name} {self.last_name}"
        elif self.role == self.Role.USER:
            return f"User - {self.first_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"
    
    
class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.type

class CardState(models.Model):
    Card_State_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20)
    
    def __str__(self):
        return self.state
    
class TravelPlanState(models.Model):
    travel_plan_state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20)
    
    def __str__(self):
        return self.state
    
    
class Rout(models.Model):
    rout_no = models.CharField(max_length=100)
    rout = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.rout_no} - {self.rout}"
    
class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    rout = models.ForeignKey(Rout, on_delete=models.SET_NULL, null=True)
    fee_stage = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.rout} - {self.fee_stage} - {self.fee} - {self.destination}"

class CardCategory(models.Model):
    card_category_id = models.AutoField(primary_key=True)
    card_category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.card_category

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_category = models.ForeignKey(CardCategory, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    card_state = models.OneToOneField(CardState, on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.card_id} - {self.card_category} - {self.user} - {self.card_state} - {self.balance}"

class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=100)
    
    def __str__(self):
        return self.plan
    
class TravelPlan(models.Model):
    travel_plan_id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
    from_destination = models.OneToOneField(Destination, on_delete=models.SET_NULL, null=True, related_name='travel_from')
    to_destination = models.OneToOneField(Destination, on_delete=models.SET_NULL, null=True, related_name='travel_to')
    plan = models.OneToOneField(Plan, on_delete=models.SET_NULL, null=True)
    travel_plan_state = models.OneToOneField(TravelPlanState, on_delete=models.SET_NULL, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.card} - {self.from_destination} - {self.to_destination} - {self.plan} - {self.fee}"
    
class InterchangingPoint(models.Model):
    interchanging_point_id = models.AutoField(primary_key=True)
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.SET_NULL, null=True)
    ineterchanging_point = models.OneToOneField(Destination, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.travel_plan} {self.ineterchanging_point}"
        
class RechargHistory(models.Model):
    recharg_history_id = models.AutoField(primary_key=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
    recharged_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    recharged_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.card} - {self.recharged_amount} - {self.balance}"
        
    

    
    
