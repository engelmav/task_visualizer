import json
import web
import psycopg2
import taskmodel as t
import taskmodel_t as tt

render = web.template.render('templates/')
urls = (
        '/', 'index'
        ,'/get_task_json','get_task_json'
        ,'/live_json','live_json'
        ,'/live_view','live_view'
        )

class index:
    def GET(self):
        print "index class called"
        i = web.input(name=None)
        web.taskpoller.domain = i
        return render.index()

class live_view:
    def GET(self):
        i = web.input(domain=None)
        print "Received input", i
        return render.live_report()

class live_json:
    def GET(self):
        print "live_report hit"
        rs = []
        print web.taskpoller.tasks_for_interval
        web.header('Content-Type', 'application/json')
        return json.dumps(web.taskpoller.tasks_for_interval)

def session_hook():
        web.ctx.session = session
        web.template.Template.globals['session'] = session

if __name__ == "__main__":
    web.config.debug = False # for sessions to work
    app = web.application(urls,globals())
    session = web.session.Session(app, web.session.DiskStore('sessions'),
            initializer = { 'test': 'woot', 'foo':''})

    app.add_processor(web.loadhook(session_hook))

    # toward beginning of the 30th: 1414675800
    # toward the spike 1414690220
    tli = tt.TaskIntervalMock(1414690220,1,1)
    tl = tt.TaskList(tli)

    tl.start()
    web.hook = {} 
    web.taskpoller = tl

    app.run()


