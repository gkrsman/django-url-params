import logging
from django.conf import settings
from django.urls.base import reverse
from django.http import HttpResponseRedirect


logger = logging.getLogger(__name__)


try:
    PARAMS_URL_CONF = settings.URL_PARAMS_CONF
except AttributeError:
    msg = 'Django URL params: URL_PARAMS_CONF is missing. Using ROOT_URLCONF.'
    logger.info(msg)
    PARAMS_URL_CONF = settings.ROOT_URLCONF


def param_redirect(request, viewname, *args):
    """ Redirect and keep URL parameters if any. """
    url = reverse(viewname, PARAMS_URL_CONF, args)
    params = request.GET.urlencode().split('&')

    if hasattr(request, 'cparam'):
        for k, v in request.cparam.items():
            params.append('{0}={1}'.format(k, v))

    new_params = '&'.join(x for x in params if x != '')
    if len(new_params) > 0:
        return HttpResponseRedirect('{0}?{1}'.format(url, new_params))
    return HttpResponseRedirect(url)
