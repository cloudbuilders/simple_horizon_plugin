# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Openstack, LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import tempfile
import zipfile

from django import http
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from horizon import api
from horizon import exceptions
from horizon import forms


LOG = logging.getLogger(__name__)


class CatForm(forms.SelfHandlingForm):
    cat = forms.ChoiceField(label=_("Select a Cat"))

    # forms.SelfHandlingForm doesn't pass request object as the first argument
    # to the class __init__ method, which causes form to explode.
    @classmethod
    def _instantiate(cls, request, *args, **kwargs):
        return cls(request, *args, **kwargs)

    def __init__(self, request, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        # Populate cat choices
        cat_choices = []
        self.fields['cat'].choices = ('', 'No Available Cats')

    def handle(self, request, data):
        return shortcuts.redirect(request.build_absolute_uri())
