from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Blog,Tag,Category1,Album,Comment,Friend,Friend_Tag

from django.views import generic
# Create your views here.


# default Data

__category1={
				'Essay':'文章',
				'WorkLog':'工作记录',
				'Joke':'瞎扯',
				'Others': '其他',
}


# Functions 

def __get_latest(objs, max_num=8):
	obj_num = objs.count()
	latest = []

	if obj_num > max_num:
		for i in range(max_num):
			latest.append({'title':objs[i].title, 'id':objs[i].id}) 
	else:
		for i in range(obj_num):
			latest.append({'title':objs[i].title, 'id':objs[i].id})

	return latest

def __get_img_latest(objs, max_num=5):
	obj_num = objs.count()
	latest = []

	if obj_num > max_num:
		for i in range(max_num):
			latest.append({'img_url': objs[i].img_url, 'id': objs[i].id})
	else:
		for i in range(obj_num):
			latest.append({'img_url': objs[i].img_url, 'id': objs[i].id})

	return latest


def __get_blog_info(objs):

	#exclude blog content!
	blog_info = []

	for blog in objs:
		category1 = blog.category1.category_1
		blog_info.append({'title': blog.title,
			'id': blog.id,
			'head_pic_url': blog.head_pic_url,
			'pub_time': blog.pub_time,
			'page_views': blog.page_views,
			'comment_times': blog.comment_times,
			'category1': __category1[category1]})

	return blog_info


#pagination
def __my_pagination(request, objs, display_num=8, after_range=12, before_range=6):
	paginator = Paginator(objs, display_num)

	try:
		page = int(request.GET.get('page'))
	except:
		page = 1
	try:
		objects = paginator.page(page)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	except:
		objects = paginator.page(1)

	if page > after_range:
		page_range = paginator.page_range[page-after_range:page+before_range]
	else:
		page_range = paginator.page_range[0:after_range]

	
	return objects,page_range


def __get_blog_list(request, obj_list):
	obj_latest = __get_latest(obj_list)
	obj_infos_all = __get_blog_info(obj_list)
	obj_infos,obj_page_range = __my_pagination(request,obj_infos_all)

	return obj_latest, obj_infos, obj_page_range



#############################################
#  Views 
#############################################

def index(request):
	blogs = Blog.objects.all()
	tags = Tag.objects.all()
	album = Album.objects.all()
	comment = Comment.objects.all()
	latest, blog_infos, page_range = __get_blog_list(request, blogs)
	friends = Friend.objects.all()
	content = {
					'blog_infos': blog_infos,
			 		'page_range': page_range,
			 		'tags': tags,
			 		'latest': latest,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends, 
	}
	print(len(album))
	 
	return render(request, 'blog/index.html', content)


def blog_detail(request, blog_id):
	blog = Blog.objects.get(id = blog_id)
	blog.page_views += 1
	blog.save()
	blog_tags = blog.tags.all()
	category1 = blog.category1.category_1
	
	return render(request, 'blog/blog_detail.html', {'blog': blog,
		'blog_tags': blog_tags,
		'category1': __category1[category1],
		})


def tag(request, tag_id):
	get_tag = Tag.objects.get(id = tag_id)
	blogs = Blog.objects.filter(tags = get_tag)
	tags = Tag.objects.all()
	album = Album.objects.all()
	comment = Comment.objects.all()
	tag_latest, tag_infos, page_range = __get_blog_list(request, blogs)
	friends = Friend.objects.all()
	content = {
					'tag_infos': tag_infos,
			 		'page_range': page_range,
			 		'tag_latest': tag_latest,
			 		'get_tag': get_tag,
			 		'tags': tags,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends,
	}

	return render('tag.html',content)

## 搜索页面，具体细节想法之后来补
def  search(request, msg):
	pass


def album(request):
	pass


def message(request):
	pass


def essay(request):
	essay = Category1.objects.get(category_1 = 'essay')
	blogs_essay = Blog.objects.filter(category1 = essay)

	tags = Tag.objects.all()
	
	essay_latest, essay_infos, essay_page_range = __get_blog_list(request, blogs_essay)
	
	album = Album.objects.all()
	comment = Comment.objects.all()
	friends = Friend.objects.all()
	
	content = {
					'essay_infos': essay_infos,
			 		'essay_page_range': essay_page_range,
			 		'essay_latest': essay_latest,
			 		'tags': tags,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends
	}

	return render('essay.html',content)


def worklog(request):
	essay = Category1.objects.get(category_1 = 'worklog')
	blogs_essay = Blog.objects.filter(category1 = essay)

	tags = Tag.objects.all()
	
	essay_latest, essay_infos, essay_page_range = __get_blog_list(request, blogs_essay)
	
	album = Album.objects.all()
	comment = Comment.objects.all()
	friends = Friend.objects.all()
	
	content = {
					'essay_infos': essay_infos,
			 		'essay_page_range': essay_page_range,
			 		'essay_latest': essay_latest,
			 		'tags': tags,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends
	}

	return render('worklog.html',content)

def joke(request):
	essay = Category1.objects.get(category_1 = 'joke')
	blogs_essay = Blog.objects.filter(category1 = essay)

	tags = Tag.objects.all()
	
	essay_latest, essay_infos, essay_page_range = __get_blog_list(request, blogs_essay)
	
	album = Album.objects.all()
	comment = Comment.objects.all()
	friends = Friend.objects.all()
	
	content = {
					'essay_infos': essay_infos,
			 		'essay_page_range': essay_page_range,
			 		'essay_latest': essay_latest,
			 		'tags': tags,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends
	}

	return render('joke.html',content)


def others(request):
	essay = Category1.objects.get(category_1 = 'others')
	blogs_essay = Blog.objects.filter(category1 = essay)

	tags = Tag.objects.all()
	
	essay_latest, essay_infos, essay_page_range = __get_blog_list(request, blogs_essay)
	
	album = Album.objects.all()
	comment = Comment.objects.all()
	friends = Friend.objects.all()
	
	content = {
					'essay_infos': essay_infos,
			 		'essay_page_range': essay_page_range,
			 		'essay_latest': essay_latest,
			 		'tags': tags,
			 		'album': album,
			 		'comment': comment,
			 		'friends': friends
	}

	return render('others.html',content)