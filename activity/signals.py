from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from notifications.signals import notify
from activity.models import Activity
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save,sender=Activity)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    recipient = User.objects.get(username=instance.organizer.user.username)
    if instance.status == 1:
        recipient = User.objects.get(username=instance.organizer.user.username)
        print(recipient)
        notify.send(sender, recipient=recipient, verb=f'Your <i>"{instance.title}"</i> Activity was activated by Admin <br> <a href="/activity/{instance.pk}" class="full">Go to {instance.title} Activity</a>')
