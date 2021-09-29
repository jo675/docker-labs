# Containerized hello world flask app and message from running container.

Build and tag the image
```
docker build -t hello_world_flask .
```
Run the container
```
docker run -p 81:81 hello_world_flask
```
Check the page on port 81
```
curl http://0.0.0.0:81
```

Output:
```
Hello world from Python Flask
Greetings from container: 52b8ead1a08
```
