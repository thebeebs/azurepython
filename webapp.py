import web
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/feed', 'feed'
)
app = web.application(urls, globals(), autoreload=False)

class index:        
    def GET(self):
        return render.index()

class feed:
    def GET(self):
        return 'The RSS feed of all the blogs on CS Blogs will appear here'

# If this file is being ran as the main program, start the web app.
if __name__ == "__main__":
    app.run()

# This function allows azure to hook up the correct URLs to the correct functions
def wsgiHandler():
    return web.application(urls, globals(), autoreload=False).wsgifunc()