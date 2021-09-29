# Containerized flask app that will print hello world and from what container.

Build and tag the image
```
docker build -t hello_world_flask
```
Run the container
```
docker run hello_world_flask
```
Check the page on port 81
```
curl http://<YOUR IP>:81
```

Output:
```
Hello world from Python Flask
Greetings from container: 52b8ead1a08
```
