from django.db import models
from django.conf import settings


user = settings.AUTH_USER_MODEL


class Experience(models.Model):
    user        = models.ForeignKey(user, on_delete=models.CASCADE)
    job_title   = models.CharField(max_length=255)
    company     = models.CharField(max_length=255)
    start_date  = models.DateField()
    end_date    = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f'{self.job_title} at {self.company}'
    

class Education(models.Model):
    user          = models.ForeignKey(user, on_delete=models.CASCADE)
    school        = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    gpa           = models.FloatField()
    start_date    = models.DateField()
    end_date      = models.DateField()

    class Meta:
        verbose_name_plural = "Educations"

    def __str__(self):
        return f'{self.degree} at {self.school}'
    

class Interests(models.Model):
    user     = models.ForeignKey(user, on_delete=models.CASCADE)
    interest = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Interests"

    def __str__(self):
        return self.interest
    

class About(models.Model):
    user      = models.ForeignKey(user, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email     = models.EmailField()
    contact   = models.CharField(max_length=13)    
    city      = models.CharField(max_length=255)
    country   = models.CharField(max_length=255)
    about_me  = models.TextField()

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return f'{self.full_name} from {self.city}, {self.country}'