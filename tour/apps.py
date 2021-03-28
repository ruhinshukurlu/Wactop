from django.apps import AppConfig


class TourConfig(AppConfig):
    name = 'tour'


    def ready(self):
        import tour.consumers
        import tour.signals