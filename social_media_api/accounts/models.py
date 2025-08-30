from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    # asymmetric "follow" graph (Twitter-style)
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,         # one-way relation: A follows B != B follows A
        related_name="following",  # so you can query user.following.all()
        blank=True,
    )
    
    class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )


    def __str__(self):
        return self.username
