#! /usr/bin/python3

# Import everything needed.
import web

#Define code paths (for now, just /)
urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return 42

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
