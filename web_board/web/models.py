from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(
        Board,
        related_name='topics',
        on_delete=models.CharField
    )
    starter = models.ForeignKey(
        UserModel,
        related_name='topics',
        on_delete=models.CASCADE
    )
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic,
        related_name='posts',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    created_by = models.ForeignKey(
        UserModel,
        related_name='posts',
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        UserModel,
        related_name='+', # we don’t need this reverse relationship, so it will ignore it
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.message