from django.db import models
from django.utils import timezone

# Create your models here.

class boastroast(models.Model):
    boastroast = ((True, "boast"),(False, "roast"))
    choices = models.BooleanField(choices=boastroast, default=True)
    post_field = models.CharField(max_length=240, default="")
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=timezone.now)
    
    @property
    def votes(self):
        return self.up_votes - self.down_votes
