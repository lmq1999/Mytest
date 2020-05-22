import web
import json

urls = ('/.*', 'hooks')
app = web.application(urls, globals())
print(web.data)
class hooks:
    def POST(self):

        # fetch hook and request data
        hook = web.ctx.env.get('HTTP_VERNEMQ_HOOK')
        data = json.loads(web.data())

        # print the hook and request data to the console
        print
        print ('hook:', hook)
        print ('data: ', data)

        # dispatch to appropriate function based on the hook.
        if hook == 'auth_on_register':
            return handle_auth_on_register(data)
        elif hook == 'auth_on_publish':
            return handle_auth_on_publish(data)
        elif hook == 'auth_on_subscribe':
            return handle_auth_on_subscribe(data)
        else:
            web.ctx.status = 501
            return "not implemented"

def handle_auth_on_register(data):
    # only allow user 'joe' with password 'secret', reject all others.
    if "joe" == data['username']:
        if "secret" == data['password']:
            return json.dumps({'result': 'ok'})

    return json.dumps({'result': {'error': 'not allowed'}})

def handle_auth_on_publish(data):
    # accept all publish requests
    return json.dumps({'result': 'ok'})

def handle_auth_on_subscribe(data):
    # accept all subscribe requests
    return json.dumps({'result': 'ok'})

if __name__ == '__main__':
    app.run()