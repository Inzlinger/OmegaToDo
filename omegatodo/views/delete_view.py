from pyramid.view import view_config
from pyramid.security import Authenticated
from pyramid.httpexceptions import HTTPFound
import transaction

from ..models.task import Task

@view_config(route_name='delete', permission='view')
def delete_view(request):
    task_id = int(request.matchdict['id'])
    task = request.dbsession.query(Task).filter_by(id = task_id).first()
    request.dbsession.delete(task)
    transaction.commit()
    request.session.flash('Eintrag erfolgreich gelöscht!')
    return HTTPFound(location=request.route_url('list'))