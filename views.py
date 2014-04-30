# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from .models import User, Commit, Build, Tag

def show_downloads(request):
    #template_values = {}
    #return render_to_response('show_home.html', template_values, context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse('software:show_home'))
