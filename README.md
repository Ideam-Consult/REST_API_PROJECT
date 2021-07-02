<<<<<<< HEAD
# Rest API project with Python-flask and docker
##Project Outline
The purpose of the project was to build a rest api that will store the firstname, surname and date of birth for a user when a post request is made.The api will also display all the users when get request is made.

##Tools used:
-I used python flask to build the application <br>
-Postgres database to store the user's information <br>
-Docker to deploy and ship the application.Please note that a container for the database had to be created and another container for the application.

##How I used docker?
####To know how docker was used,let's understand what is a docker <br>
Docker is an open platform for developing, shipping, and running
applications. Docker enables you to separate your applications from
your infrastructure so you can deliver software quickly. With Docker,
you can manage your infrastructure in the same ways you manage
your applications.

To be able to build a docker container.I needed to have a Dockerfile and docker-compose.yml file 
#####Dockerfile
A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.<br> Using docker build users can create an automated build that executes several command-line instructions in succession
 
#####docker-compose.yml
Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. A Compose file is used to define how the one or more containers that make up your application are configured. Once you have a Compose file, you can create and start your application with a single command: <code>docker-compose up</code> <br><br>
Commands needed for a docker: <br>

    docker-compose build
    docker-compose up -d //if you want to run the containers in deamon mode else
    docker-compose up
    docker ps // this should show you all running containers


#####Docker networking
One of the most important features to ensure the success of building a docker is docker networking <br>
The network named <code>bridge</code> is a special network. Unless you tell it otherwise, Docker always launches your containers in this network. 

###Challenges I faced in this project.

-One of the challenges for me what understanding how request works. Either <code> PUT</code>, <code>GET</code>, <code> DELETE</code>or <code> POST</code>. <br>
-Understanding ports connections. what the port 5000:5000 mean.<br>
-Understanding that inside the containers,the applications or database will identify each other not by localhost but by their image name
-The connectivity of database inside the container and the API inside another container. e.g <br>
I used SQLAlchemy to connect and here is the configuration i used.<br>
<code>app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://rest:pass@db:5432/users"</code>

-I also had the challenge that the applications were running well inside the containers but there seem to be no connection <br>
I had to include <code>host="0.0.0.0"</code> in my api code.
####Lessions I have learned
As much has I knew what I should do, it was very important for me to first understand the purpose of every tool I am going to use.I had to understand what is a docker and why I am using dockers<br>
I had to understand what is an API and Why REST API.
