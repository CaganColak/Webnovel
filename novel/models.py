from django.db import models

class Novel(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/")
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("Ongoing", "Ongoing"), ("Completed", "Completed")])
    rating = models.FloatField(default=0)
    categories = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name="chapters")
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()  # 📌 Bölüm metnini burada tutacağız
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.novel.title} - Bölüm {self.number}"

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="Webnovel Platformu")
    logo = models.ImageField(upload_to="site/", blank=True, null=True)

    class Meta:
        verbose_name = "Site Ayarı"
        verbose_name_plural = "Site Ayarları"

    def __str__(self):
        return self.site_name