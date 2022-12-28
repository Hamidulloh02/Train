from django.db import models


class IshHolati(models.Model):
    yuklanganvagon = models.CharField(max_length=250, null=True, blank=True)
    yuklanishunturganvagon = models.CharField(max_length=250, null=True, blank=True)
    tushurilganvagonlar = models.CharField(max_length=250, null=True, blank=True)
    tushurishunturganvagon = models.CharField(max_length=250, null=True, blank=True)
    bushvagon = models.CharField(max_length=250, null=True, blank=True)
    mdhvagon = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.yuklanishunturganvagon


class Stansiyalar(models.Model):
    nomi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nomi

class Yulak(models.Model):
    STATUS = (
        ("BO'SH", "BO`SH"),
        ("TAYYOR", "TAYYOR"),
        )
    stansiya = models.ForeignKey(Stansiyalar, on_delete=models.CASCADE, related_name='stansiya', help_text='Tirgan stansiya nomi')
    yulak = models.CharField(max_length=5, unique=True, help_text='Turgan yulak nomi')
    holati = models.CharField(choices=STATUS, max_length=15, null=True, blank=True, help_text='Yulak holatni tanlang ')
    go_to = models.ForeignKey(Stansiyalar,on_delete=models.CASCADE, null=True, blank=True, help_text='Junab ketadigan stansiya aha')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stansiya}ning {self.yulak}da {self.go_to } 'junab ketadi'"
