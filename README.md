Merkle-Tree
===========

$ cd server

<h4>Start the server</h4>
<br>

$ python server.py <client_address> <location_of_client_folder>
<br>
For eg.
<br>
$ python server.py vishrutmehta@localhost /Users/vishrutmehta/Merkel_Tree/client/

<br><br>
Now manually change a file in server folder, like :
<br>
$ echo "Try out" >> vish

<br>
Now type the following command to synchonize the file 'vish' in client to the server.

> update vish

<br>
Now go and heck the client folder, it the file will be synchronized to the server.
