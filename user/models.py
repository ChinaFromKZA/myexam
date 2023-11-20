from django.db import models
from django.contrib.auth.models import AbstractUser


class Myuser(AbstractUser):
    nickname = models.CharField(
        max_length=50,
        verbose_name='Никнейм',
        blank=True,
        null=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_groups',
        blank=True,
        verbose_name='Groups',
        help_text='The groups this user belongs to.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_user_permissions',
        blank=True,
        verbose_name='User permissions',
        help_text='Specific permissions for this user.',
    )
