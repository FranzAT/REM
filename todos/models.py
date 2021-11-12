# todos/models.py
# https://wsvincent.com/django-rest-framework-react-tutorial/

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from . import managers


class Todo(models.Model):
    # Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="task",
        verbose_name=_("user")
        )
    # Attributes - Mandatory
    title = models.CharField(max_length=200)
    description = models.TextField()

    # Attributes - Optional
    # Object Manager
    objects = managers.TodoManager()

    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        """A string representation of the model."""
        return self.title
