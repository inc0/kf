import os
import bottle

app = bottle.app()

func = os.getenv('FUNC_HANDLER')
func_port = os.getenv('FUNC_PORT', 8080)
timeout = float(os.getenv('FUNC_TIMEOUT', 180))
function_context = {
    'function-name': func,
    'timeout': timeout,
    'runtime': os.getenv('FUNC_RUNTIME', 'python3.6'),
    'memory-limit': os.getenv('FUNC_MEMORY_LIMIT', '0'),
}


@app.route('/', method=['GET', 'POST', 'PATCH', 'DELETE'])
def handler():
    req = bottle.request
    content_type = req.get_header('content-type')
    data = req.body.read()
    event = {
        'data': data,
        'event-id': req.get_header('event-id'),
        'event-type': req.get_header('event-type'),
        'event-time': req.get_header('event-time'),
        'event-namespace': req.get_header('event-namespace'),
        'extensions': {
            'request': req
        }
    }
    f = __import__(func).handler
    return f(event, function_context)


if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=func_port, debug=True)

