# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import condition
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Application, Flavor, Version
import os.path, datetime

def show_downloads_latest(request):
    application = Application.objects.get(id=settings.APPLICATION_ID)
    flavor = Flavor.objects.get(id=settings.FLAVOR_ID, application=application)
    return application, flavor

def show_downloads_etag(request):
    if len(messages.get_messages(request)):
        return None
    try:
        application, flavor = show_downloads_latest(request)
        etag = '%d:%d:%d:%d' % (application.id,
                                flavor.id,
                                flavor.versions.count(),
                                flavor.versions.latest('date').id)
        if request.user.is_authenticated():
            etag += ':%d' % request.user.id
        return etag
    except Version.DoesNotExist, e:
        return None

def show_downloads_last_modified(request):
    if len(messages.get_messages(request)):
        return None
    try:
        application, flavor = show_downloads_latest(request)
        last_modified = max(flavor.versions.latest('date').date,
                            datetime.datetime.fromtimestamp(os.path.getmtime(__file__),
                                                            timezone.get_current_timezone()))
        if request.user.is_authenticated():
            last_modified = max(last_modified, request.user.last_login)
        return last_modified
    except Version.DoesNotExist, e:
        return None

@condition(etag_func=show_downloads_etag, last_modified_func=show_downloads_last_modified)
def show_downloads(request):
    application, flavor = show_downloads_latest(request)

    template_values = {
        'application': application,
        'flavor': flavor,
    }

    return render_to_response('show_downloads.html', template_values, context_instance=RequestContext(request))
