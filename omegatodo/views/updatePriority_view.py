from pyramid.view import view_config
from pyramid.response import Response
from ..models import Task
import transaction

@view_config(route_name='updatepriority', permission='view')
def updatePriority_view(request):
    data = request.POST['id']
    newData = data[1:]
    data = newData[:-1]
    dataArray = data.split(",")

    if data:
        i = 0;
        for element in dataArray:
            task = request.dbsession.query(Task).filter_by(id = int(element[1:-1])).first()
            task.priority = i
            i += 1
    return Response()