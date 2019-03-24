
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class UserMiddle(MiddlewareMixin):

    def process_request(self, request):
        path = request.path

        if path in ['/common/register/', '/common/login/', '/common/index/']:
            return None
        if 'user_id' in request.session:
            return None
        else:
            return HttpResponseRedirect(reverse('common:login'))


