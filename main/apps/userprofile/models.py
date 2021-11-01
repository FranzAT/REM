from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from . import managers

from django.dispatch import receiver
from django.db.models.signals import post_save

# Singals
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

# Models
class Profile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name=_("user"),
        on_delete=models.CASCADE
        )

    # Attributes - Mandatory
    birth_date = models.DateField(null=True, blank=False, verbose_name=_("birthday"))

    # Attributes - Optional

    # Object Manager
    objects = managers.ProfileManager()

    # Custom Properties
    @property
    def username(self):
        return self.user.username

    # Methods

    # Meta and String
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)

    def __str__(self):
        return self.user.username
