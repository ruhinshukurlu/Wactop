from django.apps import AppConfig


class TrainingConfig(AppConfig):
    name = 'training'



    def ready(self):
        import training.signals
