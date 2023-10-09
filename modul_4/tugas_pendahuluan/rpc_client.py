import xmlrpc.client
url = 'http://localhost:8008'
s = xmlrpc.client.ServerProxy('%s' % url)

print(s.calon())
voting = int(input("silahkan voting menurut anda terbaik : "))
print(s.vote(voting))
print(s.result())
