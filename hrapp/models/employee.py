from django.db import models
from .department import Department
from .computer import Computer
from .training_program import TrainingProgram
from .employee_computer import EmployeeComputer
from .training_program_employee import TrainingProgramEmployee


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_supervisor = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    computers = models.ManyToManyField(Computer, through=EmployeeComputer)
    training_programs = models.ManyToManyField(TrainingProgram, through=TrainingProgramEmployee)


    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
