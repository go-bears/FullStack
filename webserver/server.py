import socket, urllib2


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5000))
print "Web server running..."
server_sock.listen(10)

while True:
    client_sock, addr = server_sock.accept()
    print 'We have opened a socket!'
    headers = client_sock.recv(100)  #  are the incoming headers, saved into variable
    headers = str(headers) #turn headers in string
    print headers
     
<<<<<<< HEAD
    split_headers = headers.split('\n') #split headers at newline \n
    first_line = split_headers[0] #store GET header into first_line
    parse_line1 = first_line.split() #split first line to isolate path and store as variable
    path = parse_line1[1] #store path
    print path
    
    if len(path) == 1: #if no path is sent from client to server open kittens.html
        with open('kittens.html') as f: #opens kittens.html
           htmlstring_kittens = str(f.read()) #opens error.html as string saves in variable
           print htmlstring_kittens
        client_sock.send(htmlstring_kittens) #opens html file as text file of html markdown
          
    if len(path) > 1: #if any path is sent from client to server open error.html
        with open('error.html')as e: #opens error.html
            htmlstring_error = str(e.read())  #opens html file as text file of html markdown, saves in variable
            print htmlstring_error
        client_sock.send(htmlstring_error)  #sends text file to client
        

        if path != "/" :
            error_msg = "<h1> Ooops, I did it again.\n Error 418. It's Teatime</h1>"
            client_sock.send(error_msg)
=======
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
>>>>>>> 188264fdcffb10c483bd8ccc886059f4da205400
            

    output = "<h1>Hello Client</h1>"
    client_sock.send("HTTP/1.1 200 OK\n" + "Content length: "+str(len(output)) + "Content-Type: text/html\n\n" + output)
    
    client_sock.close()
