# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question

# Register your models here.

# shows the Questions from the Polls App on the admin page

admin.site.register(Question)
