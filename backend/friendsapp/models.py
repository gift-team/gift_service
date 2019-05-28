from django.db import models
from django.conf import settings
from django.utils import timezone


AUTH_USER_MODEL = settings.AUTH_USER_MODEL


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendship_request_sent')
    to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendship_request_received')
    created = models.DateTimeField(default=timezone.now)

    message = models.CharField(max_length=500, default=f'Пользователь хочет добавить вас в друзья!')

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "%s" % self.from_user_id

    def accept(self):
        relation1 = Friends.objects.create(
            from_user=self.from_user,
            to_user=self.to_user
        )

        relation2 = Friends.objects.create(
            from_user=self.to_user,
            to_user=self.from_user
        )

        self.delete()

        FriendshipRequest.objects.filter(
            from_user=self.to_user,
            to_user=self.from_user
        ).delete()


class Friends(models.Model):
    from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friends')
    to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friends_with')
    created = models.DateTimeField(default=timezone.now)
