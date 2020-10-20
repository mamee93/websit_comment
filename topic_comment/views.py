from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Topic, Comments
from .forms import CommentForm
# Create your views here.

def all_topic(request):
	all_topic = Topic.objects.all()
	return render(request,'topic/all-list.html',{'all_topic':all_topic})



def topic_details(request,id):
    topic = get_object_or_404(Topic,id=id)
    comments = topic.Comments_Topic.filter(active=True, parent__isnull=True)
    total_comments = comments.count()

    if request.method == 'POST':
        comment_form  = CommentForm(request.POST)

        if comment_form.is_valid():
            parent_obj  = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except :
                parent_id = None
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.topic = topic
            new_comment.save()

            return HttpResponseRedirect(topic.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request,
                  'topic/detail.html',
                  {'topic': topic,
                   'comments': comments,
                   'comment_form': comment_form})
    if request.is_ajax():
        html = render_to_string('topic/comment.html',context, request=request)
        return JsonResponse({'form':html})
    
