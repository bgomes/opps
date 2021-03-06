"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'project_name.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
#from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    """
    Custom index dashboard for www.
    """
    title = "Opps CMS Dashboard"

    def init_with_context(self, context):
        site = context.get("site")

        #site_name = get_admin_site_name(context)
        # append a group for "Administration" & "Applications"
        #self.children.append(modules.Group(
            #_('Group: Administration & Applications'),
            #column=1,
            #collapsible=True,
            #children=[
                #modules.AppList(
                    #_('Administration'),
                    #column=1,
                    #collapsible=True,
                    #css_classes=('collapse closed',),
                    #models=('django.contrib.*',),
                #),
                #modules.AppList(
                    #_('Applications'),
                    #column=1,
                    #css_classes=('collapse closed',),
                    #exclude=('django.contrib.*',),
                #)
            #]
        #))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            collapsible=True,
            column=1,
            css_classes=('collapse',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=True,
            css_classes=('grp-closed',),
            models=('django.contrib.*',),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Opps Documentation'),
                    'url': 'http://www.oppsproject.org/',
                    'external': True,
                },
                {
                    'title': _('YACOWS'),
                    'url': 'http://www.yacows.com.br/',
                    'external': True,
                },
            ]
        ))

        # append a feed module
        self.children.append(modules.Feed(
            _('Latest Publications'),
            column=2,
            feed_url='http://{}/rss'.format(site.domain),
            limit=10
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
