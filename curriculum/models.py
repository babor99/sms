from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import os

# Create your models here.

class Standard(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(null=True, blank=True)
	image = models.ImageField(upload_to='standard', blank=True)
	description = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


def save_subject_image(instance, filename):
	upload_to = 'images/'
	ext = filename.split('.')[-1]
	# get filename
	if instance.subject_id:
		filename = 'Subject_Picture/{}.{}'.format(instance.subject_id, ext)
	return os.path.join(upload_to, filename)

class Subject(models.Model):
	subject_id = models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(null=True, blank=True)
	standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
	image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
	description = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


def save_lesson_files(instance, filename):
	upload_to = 'images/'
	ext = filename.split('.')[-1]
	# get filename
	if instance.lesson_id:
		filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
		if os.path.exists(filename):
			new_name = str(instance.lesson_id) + str('1')
			filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
	return os.path.join(upload_to, filename)

class Lesson(models.Model):
	lesson_id = models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=250)
	Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
	position = models.PositiveSmallIntegerField(verbose_name='chapter no.')
	slug = models.SlugField(null=True, blank=True)
	video = models.FileField(upload_to=save_lesson_files, verbose_name='Video', blank=True, null=True)
	ppt = models.FileField(upload_to=save_lesson_files, verbose_name='Presentation', blank=True)
	Notes = models.FileField(upload_to=save_lesson_files, verbose_name='Notes', blank=True)

	class Meta:
		ordering = ['position']

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('curriculum:lesson_list', kwargs={'standard':self.Standard.slug, 'slug':self.subject.slug})


class Comment(models.Model):
	lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, related_name='comments')
	comm_name = models.CharField(max_length=100, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField(max_length=500)
	date_added = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
		super().save(*args, **kwargs)

	def __str__(self):
		return self.comm_name

	class Meta:
		ordering = ['-date_added']


class Reply(models.Model):
	comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
	reply_body = models.TextField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "reply to" + str(self.comment_name.comm_name)
		