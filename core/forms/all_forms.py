from portfolio.models import *
from django.forms import ModelForm 


class ExperienceForm(ModelForm):
    class Meta:
        model  = Experience
        fields = '__all__'

class AboutForm(ModelForm):
    class Meta:
        model  = About
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model  = Education
        fields = '__all__'

class InterestsForm(ModelForm):
    class Meta:
        model  = Interests
        fields = '__all__'