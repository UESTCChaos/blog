from django.contrib import admin
from .models import Blog,Tag,Category1,Album,Comment,Friend,Friend_Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'head_pic_url', 'brief', 'content', 'category1', 'tags']}),
		# ('Date information', {'fields': ['pub_time'], 'classes': ['collapse']}),
	]


class TagAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['tag']}),
			# ('Date information', {'fields': ['add_time'], 'classes': ['collapse']}),
	]


class AlbumAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,{'fields': ['title','descr','img_url']}),
	]

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,{'fields': ['email', 'user', 'psw', 'rep', 'content', 'typeID', 'blog_ID', 'img_ID']}),
	]
	

class FriendsAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['name', 'friend_url', 'tags', 'rank']}),
	]


class FriendTagAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['tag']}),
	]



admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Friend, FriendsAdmin)
admin.site.register(Friend_Tag, FriendTagAdmin)