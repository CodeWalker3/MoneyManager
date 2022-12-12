from django.db import models

# Create your models here.
class CategoryIncome(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=255,
        blank=False, null=False
    )
    creation_user = models.ForeignKey(
        'auth.User', 
        related_name='%(class)s_requests_created',
        blank=True, null=True,
        default=None,
        on_delete=models.SET_NULL
    )
    def __str__(self):
        return self.name