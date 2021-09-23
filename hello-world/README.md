# hello world from a container

Build and tag the image
```
docker build -t hello_world:my_image .
```

Find the IMAGE ID
```
docker image ls <IMAGE ID>
```

Run the container
```
docker run <IMAGE ID>
```

Output:
```
hello world!
```
