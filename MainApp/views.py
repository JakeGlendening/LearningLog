from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

def index(request):
 return render(request,'MainApp/index.html')

@login_required
def topics(request):
 topics=Topic.objects.filter(owner=request.user).order_by('date_added')
 return render(request,'MainApp/topics.html',{'topics':topics})

@login_required
def topic(request,topic_id):
 topic=get_object_or_404(Topic,id=topic_id,owner=request.user)
 entries=topic.entry_set.order_by('-date_added')
 return render(request,'MainApp/topic.html',{'topic':topic,'entries':entries})

@login_required
def new_topic(request):
 if request.method!='POST':form=TopicForm()
 else:
  form=TopicForm(data=request.POST)
  if form.is_valid():
   new_topic=form.save(commit=False)
   new_topic.owner=request.user
   new_topic.save()
   return redirect('MainApp:topics')
 return render(request,'MainApp/new_topic.html',{'form':form})

@login_required
def new_entry(request,topic_id):
 topic=get_object_or_404(Topic,id=topic_id,owner=request.user)
 if request.method!='POST':form=EntryForm()
 else:
  form=EntryForm(data=request.POST)
  if form.is_valid():
   entry=form.save(commit=False)
   entry.topic=topic
   entry.save()
   return redirect('MainApp:topic',topic_id=topic.id)
 return render(request,'MainApp/new_entry.html',{'topic':topic,'form':form})

@login_required
def edit_entry(request,entry_id):
 entry=get_object_or_404(Entry,id=entry_id,topic__owner=request.user)
 topic=entry.topic
 if request.method!='POST':form=EntryForm(instance=entry)
 else:
  form=EntryForm(instance=entry,data=request.POST)
  if form.is_valid():
   form.save()
   return redirect('MainApp:topic',topic_id=topic.id)
 return render(request,'MainApp/edit_entry.html',{'entry':entry,'topic':topic,'form':form})
