from pyramid.view import view_config
from pyramid.security import Authenticated
from pyramid.httpexceptions import  HTTPFound
from ..models.task import Task
from sqlalchemy import and_
import transaction
import sys

@view_config(route_name='close', permission='view')
def close_view(request):
    task_id = int(request.matchdict['id'])
    task = request.dbsession.query(Task).filter_by(id=task_id, status=False).first()
    task.status = True
    task.priority = sys.maxsize
    transaction.commit()
    request.session.flash('Eintrag erfolgreich in Erledigt verschoben!')
    return HTTPFound(location=request.route_url('list'))
