from django.db import models
from django.db import connections
# Create your models here.

class GetUserFile(models.Model):
    File_Name = models.CharField(max_length=100)
    File = models.CharField(max_length=300)
    Folder_Location = models.CharField(max_length=100)

    class Meta:
        db_table = "KGtheCoder01"

class tickets_notifications(models.Model):
    Subject = models.CharField(max_length=255)
    Message = models.CharField(max_length=100000)
    ticket_or_notification = models.CharField(max_length=25)
    Viewed = models.BooleanField()

    class Meta:
            db_table = "KGtheCoder01_tickets_and_notifications"
