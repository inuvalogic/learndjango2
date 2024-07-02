from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    enable = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "webapp_category"

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published")
    hits_view = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = "webapp_blog"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "webapp_comment"
