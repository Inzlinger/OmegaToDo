# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Nutzer erstellen</h1>

<form action="${request.route_url('signin')}" method="post">
  <label for="name">Name</label>
  <input type="text" maxlength="100" name="name">
  <label for="password">Passwort</label>
  <input type="password" maxlength="100" name="password">
  <input type="submit" name="add" value="Speichern" class="button">
</form>