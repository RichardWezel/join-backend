from django.apps import AppConfig
from django.db.utils import OperationalError

class JoinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join'

    def ready(self):
        from .models import TaskStatus
        try:
            if not TaskStatus.objects.exists():
                TaskStatus.objects.create(status=False)
        except OperationalError:
            # Datenbanktabellen sind noch nicht erstellt
            pass