import socket
import httplib 

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5000))
print "Web server running..."
server_sock.listen(10)

while True:
    client_sock, addr = server_sock.accept()
    print 'We have opened a socket!'
    headers = client_sock.recv(100)  #  are the incoming headers
    headers = str(headers)
    print headers
     
    split_headers = headers.split('\n')
    first_line = split_headers[0]
    parse_line1 = first_line.split()
    path = parse_line1[1]
    
     if len(path) == 1:
        with open('kittens.html') as f:
            html_kittens = str(f.read())
            client_sock.send(html_kittens)
            
    
    if len(path) > 1:
        with open('error.html') as e:
            html_error = str(e.read(e))
            client_sock.send(html_error)
    else:
        client_sock.send("I'm a 404 error")
            

        
    output = "<h1>Hello Client</h1>"
#    client_sock.send("HTTP/1.1 200 OK\n" + "Content length: "+str(len(output)) + "Content-Type: text/html\n\n" + output)
    client_sock.send("HTTP/1.1 418 It's Teatime\n" + "Content length: "+str(len(output)) + "Content-Type: text/html\n\n" + output)    
    
    client_sock.close()
