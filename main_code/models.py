from django.db import models

class TypingResult(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES)
    asal_sekolah = models.CharField(max_length=150)
    skor = models.PositiveIntegerField()
    screenshot = models.ImageField(upload_to='screenshots/')
    tanggal_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} - {self.skor} WPM"
