from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        from plain_permissions.signal_handlers import sync_permissions

        sync_permissions(sender=None)
