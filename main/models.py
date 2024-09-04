from django.db import models

# nama model yang kamu definisikan.
class MoodEntry(models.Model): # kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5