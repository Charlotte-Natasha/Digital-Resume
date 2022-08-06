from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):

    name = models.CharField(max_length=35, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'  

class Contact(models.Model):
    class Meta:
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}' 

class Testimonial(models.Model):
    class Meta:
        ordering = ['name']   

    thumbnail = models.ImageField(blank=True, null=True, upload_to='thumbnail') 
    name = models.CharField(max_length=200, blank=True, null=True) 
    role = models.CharField(max_length=300, blank=True, null=True) 
    quote = models.CharField(max_length=500, blank=True, null=True) 
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.name    

class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        ordering = ['name']   

    image = models.ImageField(blank=True, null=True, upload_to='media') 
    url = models.URLField(blank=True, null=True) 
    name = models.CharField(max_length=200, blank=True, null=True)  
    is_image = models.BooleanField(default=True)  

    def save(self, *args, **kwargs):
        if self.url: 
            self.is_image = False

        super(Media, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name 

class Portfolio(models.Model):
    class Meta:
        ordering = ['name']
    
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.id: 
            self.slug = slugify(self.name)

        super(Portfolio, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"  

class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True) 
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True) 
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True) 
    image = models.ImageField(blank=True, null=True, upload_to='blog')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True) 

    def save(self, *args, **kwargs):
        if self.id: 
            self.slug = slugify(self.name)

        super(Blog, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class Certificate(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name