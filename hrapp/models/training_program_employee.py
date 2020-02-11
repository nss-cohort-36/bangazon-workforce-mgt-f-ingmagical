from django.db import models


class TrainingProgramEmployee(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)
