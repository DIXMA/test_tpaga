from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Model strcuture for an account
    """
    number = models.IntegerField()
    client = models.ForeignKey(User, on_delete='CASCADE')
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_created=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.number
