from prometheus_client import  make_wsgi_app, Summary
from wsgiref.simple_server import make_server
import os, subprocess, random, time

os.environ['prometheus_multiproc_dir'] = '/dev/shm'
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

metrics_app = make_wsgi_app()

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def my_app(environ, start_fn):
    # REQUESTS.inc()
    if environ['PATH_INFO'] == '/metrics':
      process_request(random.random())
      return metrics_app(environ, start_fn)
    elif environ['PATH_INFO'] == '/ready':
      start_fn('200 OK', [])
      return [b'ready']
    elif environ['PATH_INFO'] == '/health':
      start_fn('200 OK', [])
      return [b'healthy']
    start_fn('200 OK', [])
    return [b'Hello World']

if __name__ == '__main__':
    httpd = make_server('', 8000, my_app)
    httpd.serve_forever()
