import asyncio

from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

# from Wactop.firebase import send_notification
from tour.models import Tour
from organizer.models import Notification
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


User = get_user_model()

@receiver(post_save,sender=Tour)
def send_organizer_notify_when_tour_is_published(sender, instance, created, **kwargs):
    recipient = User.objects.get(username=instance.organizer.user.username)
    if instance.status == 1 and not instance.activated:
        recipient = User.objects.get(username=instance.organizer.user.username)
        print(recipient, recipient.id, 'salam')
        notification = Notification.objects.create(user = instance.organizer.user , text = f'{instance.title} was Acctivated by admin')
        notifications = Notification.objects.filter(user = instance.organizer.user , is_published=True)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'room_{recipient.id}',
            {
                'type': 'send_message',
                'text': notifications.count(),
            }
        )
        # loop.run_until_complete(coroutine)
        # send_notification(user_ids=[recipient.id],
        #                   title="It's now or never: Horn Ok is back!",
        #                   message="Book now to get 50% off!",
        #                   data=data)
        # notify.send(sender, recipient=recipient, verb=f'Your <i>"{instance.title}"</i> Tour was activated by Admin <br> <a href="/tour/{instance.pk}" class="full">Go to {instance.title} Tour</a>' )
        instance.activated = True
        instance.save()
