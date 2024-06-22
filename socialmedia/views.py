from django.shortcuts import render
from .models import Person, Post, Friendship


CURRENT_USERNAME = '013thedaniel'


def date_str(date):
    month_dict = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun', 7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'}
    hour = '0' + str(date.hour) if int(date.hour) < 10 else str(date.hour)
    minute = '0' + str(date.minute) if int(date.minute) < 10 else str(date.minute)
    day = '0' + str(date.day) if int(date.day) < 10 else str(date.day)
    month = month_dict[date.month]
    year = str(date.year)[-2:]
    return f'{hour}:{minute} on {day} {month} `{year}'


def feed(request):
    posts = Post.objects.all()
    for post in posts:
        # noinspection PyTypeChecker
        post.date = date_str(post.date)
    return render(request, 'socialmedia/feed.html', {'current_user': CURRENT_USERNAME, 'posts': posts})
