# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Login</h1>

<form action="${request.route_url('login')}" method="post">
  <label for="name">Name</label>
  <input type="text" maxlength="100" name="name">
  <label for="password">Passwort</label>
  <input type="password" maxlength="100" name="password">
  <input type="submit" name="add" value="Login" class="button">
</form>