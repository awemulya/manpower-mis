from django.db import models


STATUS = [
    ('On Hold', 'On Hold'),
    ('Completed', 'Completed')
]

class CountryCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CountryCategory, related_name='country', on_delete = models.PROTECT)

    def __str__(self):
        return self.name

class PassportInfo(models.Model):
    name = models.CharField(max_length=255)
    passport_no = models.IntegerField()
    reference = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='passportinfo', on_delete=models.PROTECT)
    pp_photo = models.FileField(upload_to='photos')
    qualification_certificate = models.FileField(upload_to='qualification_certificate')
    working_certificate = models.FileField(upload_to = 'working_certificate')
    passport = models.FileField(upload_to='passport')
    cost = models.IntegerField()
    entry_date = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS)

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['-entry_date']