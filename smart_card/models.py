from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class customUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superAdmin = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def __str__(self):
        if self.is_user:
            return f"user - {self.first_name} {self.last_name}"
        elif self.is_staff:
            return f"staff - {self.first_name} {self.last_name}"
        elif self.is_admin:
            return f"admin - {self.first_name} {self.last_name}"
        elif self.is_superAdmin:
            return f"superAdmin - {self.first_name} {self.last_name}"
        
class Payment_Type(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return {self.type}
    
class Recharg_History(models.Model):
    recharg_history_id = models.AutoField(primary_key=True)
    payment_type_id = models.ForeignKey(Payment_Type, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    recharged_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    recharged_at = models.DecimalField(max_digits=10, decimal_places=2)
        
    
    
