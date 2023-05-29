import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, phone, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, phone and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          phone=phone,
          
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, phone, password=None):
      """
      Creates and saves a superuser with the given email, name, and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          phone=phone,
          
      )
      user.is_admin = True
      user.save(using=self._db)
      return user
  

#  Custom User Model
class User(AbstractBaseUser):
#   user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  phone = models.IntegerField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'phone']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class Music(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    ACCESS_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    access = models.CharField(max_length=20, choices=ACCESS_CHOICES, default=PUBLIC)
    allowed_emails = models.TextField(blank=True)