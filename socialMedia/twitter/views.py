from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required



# Create your viewsk here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# def tweet_create(request):
#     if request.method == 'POST':
#         form = TweetForm(request.POST, request.FILES)
#         if form.is_valid():
#             tweet  = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save(commit=True)
#             return redirect('tweet_list')
#     else:
#         from = TweetForm()
#     return render(request, 'tweet_form.html', {'form': form})
#
# def tweet_update(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id ,user=request.user)
#     if request.method == 'POST':
#         from  = TweetForm(request.POST, request.FILES)
#         if from.is_valid():
#             tweet.user = request.user
#             tweet.save(commit=True)
#             return redirect('tweet_list')
#     else:
#         from = TweetForm(instance=tweet)
#     return render(request, 'tweet_form.html', {'form': from})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet  = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id ,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_delete.html', {'tweet': tweet})
# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id ,user=request.user)
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_delete.html', {'tweet': tweet})


# def register(request):
