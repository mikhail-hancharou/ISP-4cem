from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    personality = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    pseudonym = models.CharField(max_length=30, unique=True)
    time_sing_up = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pseudonym}'

    #def get_absolute_url(self):
    #    return reverse('post_detail', args=[str(self.id)])
