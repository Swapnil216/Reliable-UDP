The main.py file contains the specifications of the client and server protocol in separate classes. No need to compile/run main.py file separately, it gets compiled/interpretted as and when the client.py and server.py are executed.

How to use the file transfer application:
-Keep main.py, client.py and server.py in the same folder.

-First run the server side code:
* First change the server ip address and port number by editing the server.py file, if you want to change.
* Execute the server.py file using command "python3 server.py" or depending on your python version.

-Then run the client side code:
* Enter the desired client port by editing the client python file such that no other application is using that port.
* Execute the client.py file using command "python3 test_client.py" or depending on your python version.

Note : Interface and other details processed by the protocol while packet transmission can be seen on the terminal itself, such as IP address to connect, file path to transfer, etcetera.
This occurs at both client as well as the server side.
Details related to time taken, packets transmitted etc. are available on client side once acknowledge of the message sent is received.

The received file at server side begins with "received_datafile\"

To run multiple clients simultaneously, make multiple clients.py files with different port numbers
