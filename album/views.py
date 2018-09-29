import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image
# Create your views here.

def album_today(request):
    date = dt.date.today()
    album = Image.objects.all()
    return render(request, 'all-album/today-album.html', {"date": date,"album":album})

# def past_days_album(request,past_date):
#         # Converts data from the string Url
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(album_day)
#     album = Image.past(date)
#     return render(request, 'all-album/past-album.html',{"date": date,"album":album})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-album/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-album/search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-album/album.html", {"image":image})