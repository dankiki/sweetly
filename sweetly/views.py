from rest_framework import viewsets, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django import http
import sweetly.serializers as serializers
import sweetly.helpers as helpers
import sweetly.settings as settings


class Shortener(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def empty(self, request):
        serializer = serializers.URLSerializer()
        return Response({'serializer': serializer})

    def shorten(self, request):
        serializer = serializers.URLSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        long_url = serializer.data['long_url']
        base_url = settings.BASE_URL
        shortened_url = helpers.generate_short_url(long_url=long_url,
                                                   base_url=base_url)
        return Response({'serializer': serializer,
                         'shortened_url': shortened_url,
                         'long_url': long_url})


class Redirect(viewsets.ViewSet):
    def redirect(self, request, short_part):
        long_url = helpers.long_from_short(short_part)
        if long_url is None:
            content = 'Unfortunately the requested short URL was not found.'
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return http.HttpResponseRedirect(long_url)
