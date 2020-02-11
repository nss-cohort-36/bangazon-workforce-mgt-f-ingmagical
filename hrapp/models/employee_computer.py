from django.db import models
# from .employee import Employee
# from .computer import Computer

class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """
    assigned_date = models.DateField()
    unassigned_date = models.DateField(null=True, blank=True, default=None)
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)
