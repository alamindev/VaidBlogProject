from django.shortcuts import render, get_object_or_404,redirect
from .models import Article, Category, Comment
from .forms import CommentForm
from django.core.paginator import Paginator


def index_view(request):
	all_article = Article.objects.all()
	paginator = Paginator(all_article, 3) # Show 3 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
        "all_article":all_article,
        "all_article":page_obj,
	    }
	return render(request, "home-page.html", context)



def post_page_view(request, id):
	single_page = get_object_or_404(Article, id=id)
	related_post = Article.objects.filter(category_name=single_page.category_name).exclude(id=id)[:4]
	comment = Comment.objects.filter(article=id)
	comments = single_page.comments.filter(active=True, parent__isnull=True)
	if request.method == 'POST':
        # comment has been added
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_obj = None
            # get parent comment id from hidden input
			try:
                # id integer e.g. 15
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
            # if parent_id has been submitted get parent_obj id
			if parent_id:
				parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
				if parent_obj:
                    # create replay comment object
					replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
					replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
			new_comment = comment_form.save(commit=False)
            # assign ship to the comment
			new_comment.article = single_page
            # save
			new_comment.save()
			return redirect('post_page', id=id)
	else:
		comment_form = CommentForm()

	context = {
        "single_page":single_page,
        "related_post":related_post,
        "comment":comment,
        "comments":comments,
        "comment_form":comment_form,
    }    
	return render(request, "post-page.html", context)


def category_page_view(request, name):
	category = get_object_or_404(Category,category_name=name)
	print(category)
	article_category = Article.objects.filter(category_name=category.id)
	context = {
              "article_category":article_category,
	        }
	return render(request, "category-page.html", context)        
