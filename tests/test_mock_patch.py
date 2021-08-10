from unittest import mock
import requests

def get_fake_get(status_code, content):
  m = mock.Mock()
  m.status_code = status_code
  m.content = content

  def fake_get(url):
    return m

  return fake_get


@mock.patch('requests.get', get_fake_get(200, 'foo'))
def test_foo():
  r = requests.get('http://foo') 
  assert r.content == 'foo'

@mock.patch('requests.get', get_fake_get(200, 'bar'))
def test_foo():
  r = requests.get('http://bar') 
  assert r.content == 'bar'

