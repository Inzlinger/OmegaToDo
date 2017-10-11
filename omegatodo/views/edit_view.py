from pyramid.view import view_config
from ..models.task import Task
import datetime

@view_config(route_name='edit', renderer ='omegatodo:templates/edit.mako', permission='view')
def edit_view(request):
    task_id = int(request.matchdict['id'])
    user = request.authenticated_userid
    eintrag = request.dbsession.query(Task).filter_by(id=task_id).filter_by(owner=user)
    text = eintrag.first().text
    date = eintrag.first().due.__str__()

    return {'zustand': (text, date)}