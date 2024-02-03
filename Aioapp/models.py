from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, phone_number, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username must be set")
        user = self.model(
            username = username,
            full_name = full_name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, full_name, phone_number, password, **extra_fields):
        user = self.create_user(
            full_name=full_name,
            username=username,
            phone_number=phone_number,
            password=password,  
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, unique = True)
    username = models.CharField(max_length=100, primary_key= True, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    profile_picture = models.ImageField(null=True, upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)   
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'phone_number', 'password']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        # Assume all users have all permissions
        return True

    def has_module_perms(self, app_label):
        # Assume all users have permission to view the admin module
        return True
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(blank=False, upload_to='image', null=False)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=87, blank=False, null=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.product_title
