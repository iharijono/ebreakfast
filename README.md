# Description
For my school project

# Requirements:
1. docker (and docker-compose)
2. mysql client on the host
3. curl (maybe available on Mac already)

# Quick Start (each step may take time, be patient):
1. check out the repo 'https://github.com/iharijono/ebreakfast.git' and read README.md (this file)
```
git clone https://github.com/iharijono/ebreakfast.git
```
1. go to directory 'ebreakfast' and create a directory 'database'
```
cd ebreakfast
mkdir database
```
2. assuming you are on directory 'ebreakfast', build the docker container (need only once unless you change the code)
```
docker compose build --no-cache

# if you want, you can clear all the images on your machine
# windows cmd
for /F %i in ('docker images -a -q') do docker rmi -f %i

# windows powershell
docker images -a -q | % { docker image rm $_ -f }

# macos
docker rmi -f $(docker images -aq)


```
3. run all the containers
```
docker compose up -d
```
after everything is up (check with 'docker ps -a')
4. Initialize the Database
```
mysql -h 127.0.0.1 -uroot -proot

mysql> source sql/deinit.sql
mysql> source sql/init.sql
mysql> source sql/data.sql
```
if you want to delete all tables:
```
mysql -h 127.0.0.1 -uroot -proot
mysql> source sql/deinit.sql
```
5. Connect to the app with the browser pointing to http://localhost:5000
```
open http://localhost:8765
Login with 'test' and password is 'secret'
```

# Clean up
1. All the container but keep the DB data
```
docker compose down
```
2. Delete database ALL (be careful!!! no need to do actually)
```
docker compose down
rm -rf database
```
