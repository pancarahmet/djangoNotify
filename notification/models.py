from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name="Notofications")
    message=models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def __str__(self):
        return f"Şu kişi {self.user.username} için bildirim"


