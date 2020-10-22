from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Park_number, Post
from posts.forms import PostForm
from urllib.request import urlopen
import json
# Create your views here.


def p_lists(request, area_name):
    return render(request, 'lists.html', {'area_name': area_name})


def p_detail(request, park_num):
    park_post = get_object_or_404(Park_number, p_idx=park_num)
    return render(request, 'detail.html', {'park_post': park_post})


def p_makedb(request):
    url = "http://openapi.seoul.go.kr:8088/534e6b7475686a6538386154554170/json/SearchParkInfoService/1/138/"
    responseBody = urlopen(url).read().decode('utf-8')
    jsonArray = json.loads(responseBody)
    InfosArray = jsonArray.get("SearchParkInfoService")
    resultArray = InfosArray.get("row")
    for i in resultArray:
        parknum_form = Park_number(p_local_name=i.get("P_ZONE"), p_idx=i.get("P_IDX"))
        parknum_form.save()

    return redirect('/')


def write_post(request, p_idx):
    park_post = get_object_or_404(Park_number, p_idx=p_idx)
    if request.method == 'POST':
        if request.FILES:
            post = Post(p_idx=park_post, author=request.user, images=request.FILES['images'])
        else:
            post = Post(p_idx=park_post, author=request.user, images=None)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            path = '/posts/{}/detail'.format(p_idx)
            return  redirect(path)
        # post_form = Post(p_idx=p_idx, author=request.user, starpoint=request.POST['starpoint'], contents=request.POST['contents'], images=request.FILES['images'])
        # post_form.save()
        # return redirect('posts:detail')
    else:
        post_form = PostForm()

    return render(request, 'write.html', {'post_form': post_form})

