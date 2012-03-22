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

from django.conf.urls.defaults import patterns, url

from .forms import ContactForm1, ContactForm2
from .views import IndexView, DetailView
from .views import ContactWizard


CATS = r'^cats/(?P<cat_id>[^/]+)/%s$'


urlpatterns = patterns('animals.cats.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(CATS % 'detail', DetailView.as_view(), name='detail'),
    url(r'^cats/wizard/$', ContactWizard([ContactForm1, ContactForm2])),
)

