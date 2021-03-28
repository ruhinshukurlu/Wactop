from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from activity.models import Activity
from organizer.models import Notification
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

User = get_user_model()

@receiver(post_save,sender=Activity)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    recipient = User.objects.get(username=instance.organizer.user.username)
    if instance.status == 1 and not instance.activated:
        recipient = User.objects.get(username=instance.organizer.user.username)
        print(recipient)
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
        # notify.send(sender, recipient=recipient, verb=f'Your <i>"{instance.title}"</i> Activity was activated by Admin <br> <a href="/activity/{instance.pk}" class="full">Go to {instance.title} Activity</a>')
        instance.activated = True
        instance.save()
