from .models import *

def bildirimGonder(user,message):
    if isinstance(user,User):
        Notification.objects.create(user=user,message=message)
    else:
        raise ValueError("Geçerli bir user bulanamadı")
