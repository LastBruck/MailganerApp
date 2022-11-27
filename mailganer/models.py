from django.db import models

class Email(models.Model):
    name = models.CharField("ФИО", max_length=50)
    mail_to = models.CharField("eMail", max_length=50, default='SOME STRING')
    date_of_birth = models.CharField("День рождения", max_length=10, default='SOME STRING')
    track = models.CharField("Трэкер", max_length=3, default='SOME STRING')

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "eMail адрес"
        verbose_name_plural = "eMail адреса"