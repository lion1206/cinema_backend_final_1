from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Создание суперпользователя по умолчанию"

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("Суперпользователь admin создан"))
        else:
            self.stdout.write(self.style.WARNING("Суперпользователь уже существует"))
