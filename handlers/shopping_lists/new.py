# compra-melon (c) Baltasar 2020 MIT License <baltasarq@gmail.com>


import webapp2


class NewShoppingList(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([
    ('/', NewShoppingList)
], debug=True)
