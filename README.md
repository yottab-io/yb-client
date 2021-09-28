# Yottab client

  Yottab client is a command-line interface to interact with the [Yottab](https://yottab.io) server to create and manage workspaces and applications.
  ## Installation 
   Use the package manager pip to install Yottab client like below:
    
   `$ pip install yb-client`
    
  ## Usage
   There are four main commands in Yottab client. each one has its specific subcommands:
    
   - [user](#user) subcommands are used to [register](#register-your-account), [log in](#login-to-your-account) to, and [log out](#logout-of-your-account) of your account.
   - [workspace](#workspace) subcommands are used to [create](#create-a-workspace), [stop](#stop-a-workspace), [restart](#restart-a-workspace) and [delete](#delete-a-workspace) a workspace. You can also view the details of a workspace and the list of workspaces using the [detail](#workspace-details) and [list](#workspaces-list) subcommands, respectively.
   - [app](#app) subcommands are used to [create](#create-an-app), [stop](#stop-an-app), [start](#start-an-pp) and [delete](#delete-an-app) a application. You can also view receive the list of applications using [list](#apps-list) subcommand.
   - [product](#product) command is used to view the [products list](#products-list).
      
  
   ### User
   Before using operational commands such as workspace commands, You must first register (if you don't have an account) and then log in to your account.
   
   ##### Register your account
   
   If you want register a new account do the following:
   
   `$ yb user register [-u | --username] <your-preferred-username>`
   
   Then the CLI prompt to enter and confirm your password. When registration is done you must see **Registered successfully.** like below:
   ```
   $ yb user register -u yottabuser
   Password:
   Repeat for confirmation:
   Registered successfully.
  ```
   ##### Log in to your account
   
   If you want to log in to your account do the following:
   
   `$ yb user login [-u | --username] <your-username>`
   
   Then the CLI prompt to enter your password. If you log in successfully, you must see **Logged in successfully.** like below:
   
   ```
   $ yb user login -u yottabuser
   Password:
   Logged in successfully.
   ```


   ##### Log out of your account
   
   If you want to log out of your account do the following:
   
   ```
   $ yb user logout
   Logged out successfully.
   ```
   
   Then the CLI prompt to enter your password. If you log out successfully, you must see **Logged out successfully.**.
   
   ### Workspace
   
   For creating your desired applications, you need to have at least one workspace.
   
   ##### Create a workspace
    
   `$ yb workspace create [-n | --name] <workspace-name> [-p | --plan] <plan>`
   
   If workspace successfully is created, you must see the details of workspace.
   
   ```
   $ yb create -n ybworkspace -p medium 
 +-------------+---------+--------+
|    name     |  state  |  plan  |
+-------------+---------+--------+
| ybworkspace | pending | medium |
+-------------+---------+--------+
   ```
  If you see **Err: Not Enough Cash**, you should charge your cash then try again.
  
  ##### Workspace details
  
  To see the specific workspace state and the detail of its applications, do the following:
  
  `$ yb workspace detail [-w | --workspace] <workspace-name>`
  
```
$ yb workspace detail -w ybworkspace
+-----------------+---------+--------+----------+--------------+
| worskspace_name |  state  |  plan  | app_name |    app_id    |
+-----------------+---------+--------+----------+--------------+
|   ybworkspace   | running | medium |  ybapp2  | cekoqmhnqa8b |
|        -        |    -    |   -    |  ybapp   | cekon6o41dfw |
+-----------------+---------+--------+----------+--------------+
```
##### Stop a workspace
If you want to stop running a workspace, do the following:

`$ yb workspace stop [-w | --workspace] <workspace-name>`

```
$ yb workspace stop -w ybworkspace
Workspace stopped successfully.
```
**note**: If you want to **delete** a workspace, you have to **stop** it first.

##### Restart a workspace
If you want to start running a stopped workspace, do the following:

`$ yb workspace restart [-w | --workspace] <workspace-name>`

```
$ yb workspace restart -w ybworkspace
Workspace restarted successfully.
```
##### Delete a workspace
If you want to delete a stopped workspace, do the following:

`$ yb workspace delete [-w | --workspace] <workspace-name>`

```
$ yb workspace restart -w ybworkspace
Workspace deleted successfully.
```
##### Workspaces list
  If you want to see the workspaces list, do the following:
  
```
$ yb workspace detail -w ybworkspace
+-------------+---------+--------+
|    name     |  state  |  plan  |
+-------------+---------+--------+
| ybworkspace |  stop   | medium |
|    test     | running | medium |
+-------------+---------+--------+
```
#### App

To create your application, you must first view the [product list](#products-list) and select the desired product.

##### Create an app

If you want to create an application based on a specific product, do the following:

`$ yb app create [-n | --name] <app-name> [-id | --product-id] <product-id>`
```
$ yb app create -n ybapp -id "wordpress-5-7-1-debian-10-r21"
App created successfully.
```
##### Apps list
If you want to view the applications list, do the following:

`$ yb app list [-w | --workspace] <workspace-name>`

```
$ yb app list -w ybworkspace
+--------+---------+--------------+-------------------------------+
| name   | state   | app_id       | product_id                    |
+--------+---------+--------------+-------------------------------+
| ybapp2 | running | cekoqmhnqa8b | wordpress-5-7-1-debian-10-r21 |
| ybapp  | running | cekon6o41dfw | wordpress-5-7-1-debian-10-r21 |
+--------+---------+--------------+-------------------------------+
```
##### Stop an app
If you want to stop running an application, do the following:

`$ yb app create [-w | --workspace] <workspace-name> [-id | --app-id] <app-id>`

```
$ yb app stop -w ybworkspace -id cejqh2xhk873
App stopped successfully.
```
**note**: If you want to **delete** an application, you have to **stop** it first.

##### Start an pp
If you want to start a stopped application, do the following:

`$ yb app start [-w | --workspace] <workspace-name> [-id | --app-id] <app-id>`

```
$ yb app start -w ybworkspace -id cejqh2xhk873
App started successfully.
```

##### Delete an app
If you want to delete a stopped application, do the following:

`$ yb app delete [-w | --workspace] <workspace-name> [-id | --app-id] <app-id>`

```
$ yb app delete -w ybworkspace -id cejqh2xhk873
App deleted successfully.
```

#### Product

##### Products list
If you want to view the list of Yottab products which are available in a specific workspace, do the following:
`$ yb product list [-w | --workspace] <workspace-name>`
```
$ yb product list -w ybworkspace
+-------------------+--------------------------------+--------+
| name              | product_id                     | type   |
+-------------------+--------------------------------+--------+
| WordPress         | wordpress-5-7-1-debian-10-r21  | server |
| Redis (alpine)    | redis-alpine                   | server |
| RabbitMQ 2.8.22   | rabbitmq_3-8-22-debian-10-r7   | server |
| Prometheus 2.29.2 | prometheus_2-29-2-debian-10-r9 | server |
| PostgreSQL 13.3   | postgresql_13-3                | server |
| Nginx (alpine)    | nginx_1-21-1-alpine            | server |
| MongoDB (10.6.3)  | mongo_10-6-3-focal             | server |
| Memcached 1.6.10  | memcached_1-6-10-debian-10-r27 | server |
| Kafka 2.8.0       | kafka_2-8-0-debian-10-r94      | server |
| Jenkins 2.303.1   | jenkins_2-303-1-debian-10-r10  | server |
| GitLab CE         | gitLab_gitlab-ce-latest        | server |
| Elasticsearch     | elastic-7-12-0-debian-10-r2    | server |
+-------------------+--------------------------------+--------+
```
