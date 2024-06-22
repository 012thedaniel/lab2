from django.db import models
from django.utils import timezone


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'post by {self.person.username} ({str(self.date)})'


class Friendship(models.Model):
    STATUS_CHOICES = [(0, 'pending'), (1, 'accepted')]

    user_1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_from')
    user_2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_to')
    status = models.IntegerField(choices=STATUS_CHOICES)

    class Meta:
        unique_together = ['user_1', 'user_2']

    def __str__(self):
        if self.status == 0:
            return f"friendship request sent from {self.user_1.username} to {self.user_2.username}"
        else:
            return f"friendship between {self.user_1.username} and {self.user_2.username}"
