from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from .models import Blog

class ListBlog(APIView):
    """
    View to list all blogs in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all blog.
        """
        blogs = [{blog.title, blog.content, blog.pub_date} for blog in Blog.objects.all()]
        return Response(blogs)
    

