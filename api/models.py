from django.db import models
import hashlib


class InterestManager(models.Manager):
    def create(self, title):
        interest = self.create(title=title)
        return interest


class Interest(models.Model):
    title = models.CharField(max_length=200)


class VkUserManager(models.Manager):
    def create(self, name, vk_id):
        vk_user = self.create(name=name, vk_id=vk_id)
        return vk_user


class VkUser(models.Model):
    name = models.CharField(max_length=200)
    vk_id = models.IntegerField()
    friends = models.ManyToManyField("self")
    interests = models.ManyToManyField(Interest)


class GroupManager(models.Manager):
    def create(self, name, vk_id, interest):
        group = self.create(name=name, vk_id=vk_id, interest=interest)
        return group


class Group(models.Model):
    name = models.CharField(max_length=200)
    vk_id = models.IntegerField()
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)


class RoleManager(models.Manager):
    def create(self, name, slug):
        role = self.create(name=name, slug=slug)
        return role


class Role(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)


class UserManager(models.Manager):
    def create(self, name, password):
        pwd = password.encode().hexdigest()
        user = self.create(name=name, password=hashlib.sha256(pwd))
        return user


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
