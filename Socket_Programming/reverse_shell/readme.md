Direct VS Reverse Connection

Direct Connection :-
    In a DC we have craete a socket in our computer and bind a port to it, and the other party has to receieve the connection
    But the probleme here is , we need to know the IP of the other person computer, but as weknow that IP of the Computers are Dynamic, also our computer IP is also Dynamic

Reverese Connection :-
    In RC connect is initiated from the victimis computer, hackers create a pyhon file reverse shell where the IP address and port of hacker is stored. So now everytime the victims IP changes the file installed on the victims computer calibrated accordingly
    Still there is 1 problem to solve, the hackers computer is still haveing a dynamic IP , therefore hacker use a server(AWS) in ours case

Here we are creating a tool reverse shell, which will be used to connect to any computer
    Here we will craete 2 files server.py which we will install in our AWS server and client.py which we will send to our client
    We need to keep in mind that when we send data from one computer to another we dont send them in string/integers etc but in encoded bytes, so remember to convert





Some Useful Links:-
Try, Except concept --> https://www.youtube.com/watch?v=NIWwJbo-9_8
Reference :- https://github.com/attreyabhatt/Reverse-Shell
