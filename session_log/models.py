from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

RATING_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
TIME_LOGGED_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"))
WIND_CHOICES = ((1, "very light"), (2, "light"), (3, "moderate"), 
                (4, "strong"), (5, "very strong"), (6, "dangerous"))

class Session(models.Model):
    """
    Database model for a training session
    """
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="session_logs")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=False, blank=False)
    time_loggged = models.IntegerField(choices=TIME_LOGGED_CHOICES, default=1)
    wind_conditions = models.IntegerField(choices=WIND_CHOICES, default=1)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)


    class Meta:
        """
        Set the order of sessions by most recent session logged
        """
        ordering = ["-created_on"]


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
