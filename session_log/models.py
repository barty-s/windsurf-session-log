from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from autoslug import AutoSlugField


RATING_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
TIME_LOGGED_CHOICES = ((1, "1"), (2, "2"), (3, "3"),
                       (4, "4"), (5, "5"), (6, "6"))
WIND_CHOICES = (("very light", "very light"), ("light", "light"),
                ("moderate", "moderate"),
                ("strong", "strong"), ("very strong", "very strong"),
                ("dangerous", "dangerous"))


def validate_date(date):
    """
    Check of the date is in the future
    """
    if date > timezone.now().date():
        raise ValidationError("Date cannot be in the future")


class Session(models.Model):
    """
    Database model for a training session
    """
    date = models.DateField(validators=[validate_date])
    title = models.CharField(max_length=100,
                             null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='date')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="session_logs")
    updated_on = models.DateTimeField(auto_now=True)
    details = models.TextField(null=False, blank=False)
    time_logged = models.IntegerField(choices=TIME_LOGGED_CHOICES, default=1)
    wind_conditions = models.CharField(choices=WIND_CHOICES,
                                       default="light", max_length=15)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    class Meta:
        """
        Set the order of sessions by most recent session logged
        """
        ordering = ["-date"]
        unique_together = ("author", "date")

    def save(self, *args, **kwargs):
        """
        Generates a unique slug based on the title and timestamp
        """
        if not self.slug:
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title
