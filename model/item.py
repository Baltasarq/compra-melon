# compra-melon (c) Baltasar 2020 MIT License <baltasarq@gmail.com>


from google.appengine.ext import ndb


class Item(ndb.Model):
    name = ndb.StringProperty(required=True, indexed=True)
    desc = ndb.TextProperty(default="")

    @staticmethod
    def retrieve(req):
        toret = None

        try:
            id = req.GET["id"]
        except ValueError:
            return req.redirect("/error?msg=Missing item's id.")

        try:
            toret = ndb.Key(urlsafe=id).get()
        except:
            return req.redirect("/error?msg=No item for id: " + str(id))

        return toret
