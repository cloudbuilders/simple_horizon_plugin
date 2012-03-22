Overview
========
This is a simple Horizon plugin to demonstrate how to extend
the Openstack Horizon Dashboard.

It relies on https://github.com/cloudbuilders/simple_nova_extension
to display cats.  However, if you are just trying to get some framework
code this may still be useful.

Devstack Installation
=====================
To enable this plugin in your environment:

    git clone https://github.com/cloudbuilders/simple_horizon_plugin

    cd simple_horizon_plugin
    sudo python setup.py develop

This will add the appropriate paths to your system so that horizon
can find your plugin.

Local Settings Modifications
============================
Now, configure your plugin by including the following in
/opt/stack/horizon/openstack_dashboard/local/local_settings.py:

    HORIZON_CONFIG = {
        'dashboards': ('nova', 'animals', 'syspanel', 'settings',),
        'default_dashboard': 'nova',
        'user_home': 'openstack_dashboard.views.user_home',
    }

    INSTALLED_APPS = (
        'openstack_dashboard',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_nose',
        'horizon',
        'horizon.dashboards.nova',
        'horizon.dashboards.syspanel',
        'horizon.dashboards.settings',
        'animals',
    )

Now, restart your web server.  If you are using devstack:

    sudo /etc/init.d/apache2 restart


Using the Plugin
================
You should now be able to view the simple plugin in your dashboard
at the url:

    http://myhost/animals/
