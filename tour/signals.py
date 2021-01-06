from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from notifications.signals import notify
from tour.models import Tour
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save,sender=Tour)
def send_organizer_notify_when_tour_is_published(sender, instance, created, **kwargs):
    recipient = User.objects.get(username=instance.organizer.user.username)
    if instance.status == 1 and not instance.activated:
        recipient = User.objects.get(username=instance.organizer.user.username)
        print(recipient)
        notify.send(sender, recipient=recipient, verb=f'Your <i>"{instance.title}"</i> Tour was activated by Admin <br> <a href="/tour/{instance.pk}" class="full">Go to {instance.title} Tour</a>' )
        instance.activated = True
        instance.save()