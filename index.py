#-*-coding:utf-8
import web
import os

urls = (
    "/", "Index",
    "/blog/(.+)", "Blog",
)

dir_articles = "/home/yujie/sdb2/jobs/project/blog/html"
render = web.template.render(dir_articles)
app = web.application(urls, globals())


class Index:
    def GET(self):
        blogs = [each for each in os.listdir(dir_articles) if each.endswith(".html")and not each.startswith("index")]
        return render.index(blogs)


class Blog:
    def GET(self, title):
        title = title.encode("utf-8")
        article = web.template.frender(dir_articles + '/' + title)
        return article()

if __name__ == "__main__":
    app.run()
