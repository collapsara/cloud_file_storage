# Cloud file manager

## Start project commands
Start a project with commands: 

`docker-compose build` \
`docker-compose up -d`

Please open logs of minio server: \
`docker logs --tail 1000 -f cloud_file_storage-minio-1`

You can see api address of project. Please open API with port 9000.

Credentials of server:
- username: minio
- password: minio123

Create a bucket with name 'files'.

And now you can open http://localhost:8000/api/schema/swagger-ui/ to see all project endpoints.


- GET ALL FILES: \
GET 'http://localhost:8000/files/'
- ADD NEW FILE: \
POST 'http://localhost:8000/files/'

I add file with postman form-data. You need to fill only file field.

- DOWNLOAD FILE: \
GET http://localhost:8000/files/download/{id}/


## Containers list

- app - main application on django rest framework
- postgres - database for application
- pgadmin - postgres admin of database
- minio - file storage server

## Database
You can connect to database with pgadmin with http://localhost:5050/ path. You can find all credentials in .env file






