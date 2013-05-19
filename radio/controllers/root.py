# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates
from radio import model
from radio.controllers.secure import SecureController
from radio.model import DBSession, metadata
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController

from radio.lib.base import BaseController
from radio.controllers.error import ErrorController

__all__ = ['RootController']

#rockStreams = dict(
#                   'operator.applespajamas.com:8000':
#                   {'streams':
#                   {
#                   'HiFi':('/stream/1/','/stream/3/'),
#                   'LoFi':('/stream/2/','/stream/4/')
#                   }
#                   },
#                   'operator.applespajamas.com:8010':
#                   {'streams':
#                   {
#                   'HiFi':('/stream/1/','/stream/3/'),
#                   'LoFi':('/stream/2/','/stream/4/')
#                   }
#                   }
#                   )


class RootController(BaseController):
    """
    The root controller for the radio application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "radio"

    @expose('radio.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('radio.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('radio.templates.listen')
    def about(self):
        """Handle the 'listen' page."""
        return dict(page='listen')

    @expose('radio.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('radio.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data', params=kw)

    @expose('radio.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('radio.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('radio.templates.login')
    def login(self, came_from=lurl('/')):
        """Start the user login."""
        login_counter = request.environ.get('repoze.who.logins', 0)
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)

## By MattRock
    @expose(content_type='audio/x-scpls')
    def play(self,stream):
        """Handle the 'play' page."""
        if stream=="lofi":
            playlist="""[playlist]
NumberOfEntries=6
File1=http://operator.applespajamas.com:8000/lofi
Title1=LoFi
File2=http://operator.applespajamas.com:8000/axemp3lofi
Title2=LoFi
File3=http://operator.applespajamas.com:8000/axelofi
Title3=LoFi
File4=http://operator.applespajamas.com:8010/stream/2/
Title4=LoFi
File5=http://operator.applespajamas.com:8010/stream/6/
Title5=LoFi
File6=http://operator.applespajamas.com:8010/stream/4/
Title6=LoFi
Length1=-1
Version=2
"""
        else:
            playlist="""[playlist]
NumberOfEntries=6
File1=http://operator.applespajamas.com:8000/hifi
Title1=HiFi
File2=http://operator.applespajamas.com:8000/axemp3hifi
Title2=LoFi
File3=http://operator.applespajamas.com:8000/axehifi
Title3=HiFi
File4=http://operator.applespajamas.com:8010/stream/1/
Title4=HiFi
File5=http://operator.applespajamas.com:8010/stream/5/
Title5=HiFi
File6=http://operator.applespajamas.com:8010/stream/3/
Title6=HiFi
Length1=-1
Version=2
"""
        return playlist

    @expose('radio.templates.text')
    def text(self):
        """Handle the 'text' page."""
        return dict(page='text')
