from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, default=None, null=True)
    description = models.TextField(max_length=200, default=None, null=True)
    city = models.CharField(max_length=200, default=None, null=True)
    address = models.TextField(max_length=200, default=None, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=200, default=None, null=True)
    description = models.TextField(max_length=200, default=None, null=True)
    salary = models.FloatField(default=0, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }
