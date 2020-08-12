from django.apps import AppConfig


class BloodappConfig(AppConfig):
    name = 'bloodapp'

    def ready(self):
    	import bloodapp.signals