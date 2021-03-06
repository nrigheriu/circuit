"""@package posts
Post and Hashtag model file.

@author 7Pros
@copyright
"""
from django.db import models
from django.http import Http404

from users.models import User
from circles.models import Circle


class Post(models.Model):
    """
    Post model that stores all information of a post
    """
    content = models.CharField(max_length=256)
    author = models.ForeignKey(User)
    # the post of which this is a repost
    repost_original = models.ForeignKey('self', null=True, blank=True, related_name='repost')
    reply_original = models.ForeignKey('self', null=True, blank=True, related_name='reply')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorites = models.ManyToManyField(User, related_name='favorites')
    circles = models.ForeignKey(Circle, null=True, blank=True, related_name='circles')
    image = models.ImageField(upload_to='tmp/', null=True, blank=True, height_field=None,
                              width_field=None)  # TODO:put right directory in here

    def original_or_self(self):
        """
        Helper method for getting the original post of a repost.

        Loops until the original is found to avoid database inconsistencies.

        @return `self.repost_original` if set, `self` otherwise
        """
        p = self
        while p.repost_original:
            p = p.repost_original
        return p

    def __str__(self):
        return self.content


class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

    @staticmethod
    def filter_posts_by_hashtag(hashtag_name):
        """
        Filters posts by hashtag.

        @param hashtag_name the hashtag name to filter with
        @return the posts that have used this hashtag
        """
        return Hashtag.objects.get(name=hashtag_name).posts.all()
