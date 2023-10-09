from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


data_voting = {
    'Ganjar': 0,
    'Prabowo': 0,
    'Anies': 0,
    'abstain': 0,
}


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')


with SimpleXMLRPCServer(('localhost', 8008), requestHandler=RequestHandler) as server:
    def list_calon():

        return "List Voting Presiden Indonesia 2024: \n" + "1. Ganjar Pranowo \n" + "2. Prabowo Subianto \n" + "3. Anies Baswedan"

    def vote_calon(vote):
        if vote == 1:
            data_voting["Ganjar"] += 1
        elif vote == 2:
            data_voting["Prabowo"] += 1
        elif vote == 3:
            data_voting["Anies"] += 1
        else:
            data_voting["abstain"] += 1

        return "anda telah voting"

    def perolehan_suara():
        return data_voting

    server.register_function(list_calon, "calon")
    server.register_function(vote_calon, "vote")
    server.register_function(perolehan_suara, "result")

    print("Server berjalan")

    server.serve_forever()
