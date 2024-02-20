from django.db import models
from django.contrib.auth import get_user_model
import pytz

utc=pytz.UTC

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="First Name", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name="Location", max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return self.user.username


class Logs(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True, related_name="logs") 
    log = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Log: {self.user.username} {self.created_at}'