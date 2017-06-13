from django.db import models

from DjangoUeditor.models import UEditorField

import sys
import importlib
importlib.reload(sys)

# Create your models here.

class Category1(models.Model):
	category_1 = models.CharField(max_length=30,db_index=True,unique=True)
	add_time = models.DateTimeField(auto_now_add=True)    

	def __unicode__(self):
		return self.category_1

	class Meta:
		ordering = ['-add_time']


class Tag(models.Model):
	tag = models.CharField(max_length=30,db_index=True,unique=True)
	add_time = models.DateTimeField(auto_now_add=True)  ## 好像这里时间排序没必要
	
	def __unicode__(self):
		return self.tag

	class Meta:
		ordering = ['-add_time']


class Blog(models.Model):
	title = models.CharField(u'标题',max_length=100)
	head_pic_url = models.CharField(u'头图链接',max_length=250,default='img/default.jpg')
	pub_time = models.DateTimeField(auto_now_add=True)
	brief = models.CharField(u'摘要',max_length=200,blank=True,null=True)
	content = UEditorField(u'正文',width=900,height=600,toolbars="full",imagePath="",settings={})
	page_views = models.PositiveIntegerField(u'阅读量',default=0,editable=False)
	category1 = models.ForeignKey(Category1,verbose_name=u'一级目录',on_delete=models.CASCADE) # 类别： 文章, 工作记录等
	tags = models.ManyToManyField(Tag,blank=True,verbose_name=u'标签')
	comment_times = models.PositiveIntegerField(u'评论数',default=0,editable=False)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-pub_time']


class Album(models.Model):
	title = models.CharField(u'标题',max_length=100)
	add_time = models.DateTimeField(auto_now_add=True)
	descr = models.CharField(u'描述',max_length=100)
	img_url = models.CharField(u'图片链接',max_length=250,default='img/default.jpg')
	comment_times = models.PositiveIntegerField(u'评论数',default=0,editable=False)
	page_views = models.PositiveIntegerField(u'阅读量',default=0,editable=False)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering =  ['-add_time']


class Comment(models.Model):
	email = models.EmailField(u'邮箱',max_length=254,unique=True)
	user = models.CharField(u'用户名',max_length=30,unique=True)
	psw = models.CharField(u'密码',max_length=50)
	rep = models.CharField(u'回复人',max_length=30,null=True)
	pub_time = models.DateTimeField(auto_now_add=True)
	content = UEditorField(u'正文',width=700,height=400,toolbars="full",imagePath="",settings={})
	vote = models.PositiveIntegerField(u'点赞数',default=0,editable=False)

	typeID = models.PositiveIntegerField(u'类型编号',default=0) # 0: 留言板  1：blog  2: img
	blog_ID = models.ForeignKey(Blog,verbose_name=u'文章ID',null=True,on_delete=models.CASCADE)
	img_ID = models.ForeignKey(Album,verbose_name=u'图片ID',null=True,on_delete=models.CASCADE)

	def __unicode__(self):
		return self.user

	class Meta:
		ordering = ['pub_time'] 


class Profile_Tag(models.Model):
	tag = models.CharField(max_length=30,db_index=True,unique=True)
	add_time = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.tag

	class Meta:
		ordering = ['-add_time']


class Profile(models.Model):
	title = models.CharField(u'标题',max_length=100)
	head_pic_url = models.CharField(u'头图链接',max_length=250,default='img/default.jpg',null=True,blank=True)
	pub_time = models.DateTimeField(auto_now_add=True)
	content = UEditorField(u'正文',width=900,height=600,toolbars="full",imagePath="",settings={})
	tags = models.ManyToManyField(Profile_Tag,blank=True,verbose_name=u'标签')
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-pub_time']


class Friend_Tag(models.Model):
	tag = models.CharField(max_length=30,db_index=True,unique=True)
	add_time = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.tag

	class Meta:
		ordering = ['-add_time']


class Friend(models.Model):
	name = models.CharField(max_length=50,db_index=True,unique=True)
	friend_url = models.CharField(u'链接',max_length=250,default='http://')
	tags = models.ManyToManyField(Friend_Tag,blank=True,verbose_name=u'标签')
	rank = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['rank']





