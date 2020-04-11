from django.db import models


class Job(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=300)
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{ self.company_name } {self.job_title }'

