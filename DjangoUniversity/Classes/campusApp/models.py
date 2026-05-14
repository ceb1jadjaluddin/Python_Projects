from django.db import models

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, blank=True, default="")
    state = models.CharField(max_length=60, blank=True, default="")
    campus_id = models.CharField(max_length=60, blank=True, default="")

    objects = models.Manager()

    def __str__(self):
        return self.campus_name

    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"