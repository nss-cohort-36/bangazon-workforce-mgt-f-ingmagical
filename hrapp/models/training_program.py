from django.db import models
# from .employee import Employee
# from .training_program_employee import TrainingProgramEmployee

class TrainingProgram(models.Model):

    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    employees = models.ManyToManyField("Employee", through='TrainingProgramEmployee')

    class Meta:
        verbose_name = ("TrainingProgram")
        verbose_name_plural = ("TrainingPrograms")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("TrainingProgram_detail", kwargs={"pk": self.pk})
