from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class CommentStatus(models.TextChoices):
    CREATED = 'CREATED'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    DELETED = 'DELETED'


class AbstractComment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True,
                               related_name='parent_%(class)ss')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    comment_body = models.TextField()

    status = models.CharField(max_length=15, choices=CommentStatus.choices, default=CommentStatus.CREATED)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']
        abstract = True


class AbstractRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rate

    class Meta:
        abstract = True
