import datetime
from django import forms
from .models import Session

today = datetime.date.today()


class SessionForm(forms.ModelForm):
    """
    Form to log a training session
    """
    class Meta:
        """
        Form fields
        """
        model = Session
        fields = [
            "title",
            "details",
            "time_logged",
            "wind_conditions",
            "rating",
            "date",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "details": forms.Textarea(
                attrs={"class": "form-control", "rows": 5}
            ),
            "date": forms.DateInput(
                attrs={"class": "form-control", "type": "date", "max": today}
            )
        }

