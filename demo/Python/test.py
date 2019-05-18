import requests


host = '192.168.1.100'
port = '8888'
addr = 'http://%s:%s' % (host, port)


def submit(path, payload):
  server_addr = '%s%s' % (addr,path)

  try:
    r = requests.post(server_addr, data=payload)
  except:
    return None
  else:
    return r.text


def getvalue(tag):
  path = '/getvalue'
  payload = {'tag':tag}

  return submit(path, payload)


def storeavalue(tag, value):
  path = '/storeavalue'
  payload = {'tag':tag, 'value': value}

  return submit(path, payload)


# print(getvalue('light'))
# print(storeavalue('buzz', 'on'))