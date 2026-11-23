from django.db import models
class MusicRelease(models.Model):
 title=models.CharField(max_length=180)
 description=models.TextField(blank=True)
 release_date=models.DateField(null=True,blank=True)
 artwork=models.ImageField(upload_to="releases/",blank=True)
 is_featured=models.BooleanField(default=False)
 is_published=models.BooleanField(default=True)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["-is_featured","-release_date","-created_at"]
 def __str__(self): return self.title
