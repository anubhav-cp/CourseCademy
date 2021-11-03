from django.db import models



class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('Free', 'Free'),
        ('Premium', 'Premium')
    ]
    
    
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='free', max_length=20)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)


    def __str__(self) -> str:
        return self.membership_type

