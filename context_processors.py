# -*- coding: utf-8 -*-
from django.conf import settings
from .models import Application, Flavor

def meta_software(request):
    application = Application.objects.get(id=settings.APPLICATION_ID)
    flavor = Flavor.objects.get(id=settings.FLAVOR_ID, application=application)

    main_version = flavor.versions.filter(stable=True).latest('date')
    beta_version = flavor.versions.latest('date')

    template_values = {
        'software_main_version': main_version,
        'software_beta_version': beta_version,
    }

    return template_values
