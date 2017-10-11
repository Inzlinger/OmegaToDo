# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<% user = request.authenticated_userid %>
<% 
    import datetime
    today = datetime.datetime.now().date().__str__()
    %>
<h1>Neue Aufgabe Erstellen</h1>
<form action="${request.route_url('new')}" method="post">
  <label for="name">Name</label>
  <input type="text" maxlength="100" name="name">
  <label for="date">Deadline</label>
  <input type="date" name="date", value=${today}>
  <input type="submit" name="add" value="Speichern" class="button">
</form>