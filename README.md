## There are several calls to deprecated APIs that were removed in Django 4.0:

- django.conf.url.urls
- ugettext
- force_text

**Needs to be replaced:**

For ugettext use
$ from django.utils.translation import gettext_lazy as _

for force_text use
$ from django.utils.encoding import force_str as force_text

For django.conf.urls use
$ from django.urls import re_path as url