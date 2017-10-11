import bcrypt
from pyramid.httpexceptions import  HTTPFound
from pyramid.view import view_config
from pyramid.security import Authenticated
import transaction
from ..models.user import User

@view_config(route_name='signin', renderer='omegatodo:templates/signin.mako')
def signin(request):
    if request.method == 'POST':
        if request.POST.get('name'): 
            login = request.POST['name']
            user = request.dbsession.query(User).filter_by(name=login)
            if not user.all() :
                if request.POST.get('password'):
                    newUser = User(name = login)
                    newUser.set_password(request.POST['password'])
                    request.dbsession.add(newUser)
                    transaction.commit()
                    request.session.flash('Nutzer erfolgreich Erzeugt!')
                    return HTTPFound(location=request.route_url('login'))
                else:
                    request.session.flash('Bitte geben Sie ein Passwort ein!')
            else:
                request.session.flash('Es existiert bereits ein Nutzer mit diesem Namen')
        else:
            request.session.flash('Bitte geben Sie einen Namen ein!')
    return {}