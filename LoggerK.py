import logging
import logstash
import sys


if 'LOG_HOST' not in os.environ:
    raise(Exception("LOG_HOST NOT DEFINED"))

host = os.environ['LOG_HOST']


test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5000, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_string': 'Host ' + repr(socket.gethostname()),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)

j=0

while True:
    # Code executed here
    extra = {
    'test_string': 'Iteration ' + $j
    }
    test_logger.info('python-logstash: test extra fields', extra=extra)
    true $(( j++ ))
    time.sleep(60)
