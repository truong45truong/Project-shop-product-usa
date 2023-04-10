from django.urls import path

from .views import BlogViewSet,CommentViewSet,HeartViewSet,get_blog_product,get_comment_child

blog = BlogViewSet.as_view({
    'get' : 'get_blog',
    'post': 'post_blog'
})

comment = CommentViewSet.as_view({
    'get' : 'get_comment',
    'post': 'post_comment'
})

heart = HeartViewSet.as_view({
    'post' : 'post_heart_product'
})
heart_blog = HeartViewSet.as_view({
    'post' : 'post_heart_blog'
})
post_heart_comment = HeartViewSet.as_view({
    'post' : 'post_heart_comment'
})
urlpatterns = [
    # path('blog/', get_blog_product, name = 'blogs_logs'),
    path('blog/product/', get_blog_product, name = 'blogs_logs'),
    path('blog/heart/', heart_blog, name = 'heart_blog'),
    path('comment/',comment, name = 'comment_logs'),
    path('comment/heart/',post_heart_comment, name = 'comment_heart'),
    path('comment/child/',get_comment_child, name = 'comment_child'),
]