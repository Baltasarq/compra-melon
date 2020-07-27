#!/usr/bin/env python
# compra-melon (c) Baltasar 2020 MIT License <baltasarq@gmail.com>


import webapp2
from webapp2_extras.users import users
from webapp2_extras import jinja2

from model.appinfo import AppInfo
from model.shopping_list import ShoppingList


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if not usr:
            shopping_lists = []
        else:
            shopping_lists = ShoppingList.query().order(-ShoppingList.updated)

        template_values = {
            "users": users,
            "info": AppInfo,
            "usr": usr,
            "shopping_lists": shopping_lists
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("list_shopping_list.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
