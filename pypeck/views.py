from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import View
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

import json

from pypeck import PyPeck


class PyPeckView(View):

    def get(self, request, *args, **kwargs):
        if 'url' in request.GET:
            pypeck = PyPeck(
                request.GET.get('url'),
                settings.PYPECK_SETTINGS,
            )
            pypeck.process()
            datas = pypeck.get_datas()
            return HttpResponse(
                json.dumps(datas, cls=DjangoJSONEncoder),
                mimetype='application/json'
            )
        return HttpResponseBadRequest()
