# inet_4031_adduser_script

<h2>Two Sections:</h2>


<h3>Description Section</h3>
<p> These files are a part of my INET 4031 Course at the University of Minnesota. The goal of the script is to create an automation that can create new accounts on the server. Doing this will minimize the amount of manual work that needs to be done to complete such a tedious task. 
</p>

<br>

<h3>Operation Section</h3>
<p> In order to run the file, simply run the script by inputting the input data into the python file
</p>

```sudo ./create-users.py < create-users.input```
or
```cat create-users.input | sudo ./create-users.py```
<br>
<br>
<h4> Once the file has run, you can check your work by running these commands in the terminal: </h4>



Confirm the users' group memberships in /etc/group:
```grep user0 /etc/group```
<br>


Confirm the users are in /etc/passwd:
```grep user0 /etc/passwd```
<br>


Confirm user05 is a member of the user05 group:
```id user 05```


