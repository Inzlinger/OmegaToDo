from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import Authenticated


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(settings=settings,
        session_factory=session_factory)
    config.include('pyramid_mako')
    config.include('.models')
    config.include('.routes')
    config.include('.security')

    config.scan()

    return config.make_wsgi_app()
