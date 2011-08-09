from django.db import models
from accounts.models import Tutor, Client

class Session(models.Model):
    date = models.DateTimeField()
    tutor = models.ForeignKey(Tutor)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return self.tutor.first_name + " tutors " + self.client.first_name + " on " + str(self.date)