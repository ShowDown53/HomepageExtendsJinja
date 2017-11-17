#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):

        Omeni = "To sem jaz."
        params = {"Omeni": Omeni}

        return self.render_template("omeni.html", params=params)

class ProjektiHandler(BaseHandler):
    def get(self):

        projekti = "Moj najvecji projekt je, da se zjutraj zbudim."
        params = {"projekti": projekti}

        return self.render_template("projekti.html", params=params)

class BlogHandler(BaseHandler):
    def get(self):

        blog_posts = [{"title":"First post", "text":"A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with Burek"},
                        {"title":"Second post", "text":"One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin."},
                        {"title":"Third post", "text":"The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc,"}]

        params = {"blogs": blog_posts}

        return self.render_template("blog.html", params=params)

class KontaktHandler(BaseHandler):
    def get(self):

        phone = "123-456-789"
        email = "derp@herp.si"

        params = {"phone": phone, "email": email}
        return self.render_template("kontakt.html", params=params)

class RandomHandler(BaseHandler):
    def get(self):

        params = {"random": random.randint(1, 1000)}

        return self.render_template("random.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/projects', ProjektiHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/kontakt', KontaktHandler),
    webapp2.Route('/random', RandomHandler),

], debug=True)
