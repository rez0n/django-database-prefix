from django.conf import settings
from django.db.models.signals import class_prepared, pre_init


def function(sender, **kwargs):

    # Get tables prefix from configuration
    prefix = getattr(settings, "DB_PREFIX", None)

    # Perform action only for managed tables
    managed = sender._meta.managed
    
    if managed:
        if prefix and not sender._meta.db_table.startswith(prefix):
            sender._meta.db_table = prefix + sender._meta.db_table


pre_init.connect(function)
class_prepared.connect(function)