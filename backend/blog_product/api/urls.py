from django.urls import path
from .views import BlogViewSet,CommentViewSet,HeartViewSet,get_blog_product,get_comment_child,get_comment_product ,post_comment_product

blog = BlogViewSet.as_view({
    'get' : 'get_blog',
    'post': 'post_blog'
})

comment = CommentViewSet.as_view({
    'get' : 'get_comment',
    'post': 'post_comment_blog'
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
edit_comment = CommentViewSet.as_view({
    'post': 'edit_comment'
})
delete_comment = CommentViewSet.as_view({
    'post': 'delete_comment'
})
urlpatterns = [
    # path('blog/', get_blog_product, name = 'blogs_logs'),
    path('blog/product/', get_blog_product, name = 'blogs_logs'),
    path('blog/heart/', heart_blog, name = 'heart_blog'),
    path('comment/blog/',comment, name = 'comment_logs'),
    path('comment/product/',get_comment_product, name = 'get_comment_product'),
    path('comment/product/create/',post_comment_product, name = 'comment_logs'),
    path('comment/edit/',edit_comment, name = 'edit_comment'),
    path('comment/delete/',delete_comment, name = 'delete_comment'),
    path('comment/heart/',post_heart_comment, name = 'comment_heart'),
    path('comment/child/',get_comment_child, name = 'comment_child'),
]