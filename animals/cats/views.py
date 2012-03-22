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

from django.contrib import messages
from django.views import generic
from horizon import api
from horizon import forms
from horizon import tables
from novaclient import exceptions as novaclient_exceptions


from .tables import CatsTable


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = CatsTable
    template_name = 'animals/cats/index.html'

    def get_data(self):
        # Gather our cats
        try:
            cats = api.novaclient(self.request).cats.list()
        except novaclient_exceptions.ClientException, e:
            cats = []
            LOG.exception("ClientException in cats index")
            messages.error(self.request, _('Unable to fetch cats: %s') % e)
        return cats


class DetailView(generic.TemplateView):
    template_name = 'animals/cats/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Wait!  Something is amiss!
        context['cat'] = {'thumb': ('http://images.ansolabs.com/'
                                    'mini-dog-pic11236.jpg'),
                          'id': 3,
                          'type': 'cute',
                          'url': 'http://www.liewcf.com/cute-mini-dog-1009/'}
        return context
