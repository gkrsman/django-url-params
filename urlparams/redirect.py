import logging
from django.conf import settings
from django.urls.base import reverse
from django.http import HttpResponseRedirect


logger = logging.getLogger(__name__)


try:
    PP = settings.PARAMS_URL_CONF
except AttributeError:
    msg = 'Django URL params! PARAMS_URL_CONF is missing using default URL_CONF.'
    logger.info(msg)
    PP = settings.ROOT_URLCONF


def param_redirect(request, viewname, *args):
    """ Redirect and keep URL parameters if any. """
    url = reverse(viewname, PP, args)
    params = request.GET.urlencode().split('&')

    if hasattr(request, 'cparam'):
        for k, v in request.cparam.items():
            params.append('{0}={1}'.format(k, v))

    new_params = '&'.join(x for x in params if x != '')
    if len(new_params) > 0:
        return HttpResponseRedirect('{0}?{1}'.format(url, new_params))
    return HttpResponseRedirect(url)
