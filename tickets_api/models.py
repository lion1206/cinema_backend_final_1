from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=20, unique=True)  # номер билета
    movie_title = models.CharField(max_length=255)               # название сеанса
    start_time = models.DateTimeField()                          # время начала
    seat_number = models.CharField(max_length=10)                # место
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"{self.ticket_number} — {self.movie_title} ({self.user.username})"
