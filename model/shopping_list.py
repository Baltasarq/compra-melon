# compra-melon (c) Baltasar 2020 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb

from item import Item


class Entry(ndb.Model):
    item_index = ndb.KeyProperty(kind=Item, required=True)
    checked = ndb.BooleanProperty(default=False)


class ShoppingList(ndb.Model):
    updated = ndb.DateProperty(auto_now=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    authorized_emails = ndb.StringProperty(repeated=True)
    entries = ndb.StructuredProperty(Entry, repeated=True)

    @staticmethod
    def retrieve(req):
        toret = None

        try:
            id = req.GET["id"]
        except ValueError:
            return req.redirect("/error?msg=Missing shopping list's id.")

        try:
            toret = ndb.Key(urlsafe=id).get()
        except:
            return req.redirect("/error?msg=No shopping list for id: " + str(id))

        return toret
