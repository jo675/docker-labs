# Lab using vagrant to provision four VirtualBox nodes on one host. 

## The nodes needs to be on the same subnet. Docker swarm cluster will be initialized on the control node. The rest of the nodes will join this cluster.

Bring up the virtual machines.
```
vagrant up
```
Copy the hosts file to the all virtual machines.
```
scp -P 2200 hosts vagrant@127.0.0.1:~
scp -P 2201 hosts vagrant@127.0.0.1:~
scp -P 2202 hosts vagrant@127.0.0.1:~
scp -P 2203 hosts vagrant@127.0.0.1:~

```
Login to all virtual machines and move the hosts file.
```
sudo cp hosts /etc/hosts

```
Connect to the control node.
```
vagrant ssh control
```
Install docker on node using using the official convenience script.
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
Check the docker configuration.
```
docker info
```
Run docker hello-world image to see that installation is working correctly.
```
docker run hello-world
```
Repeat the steps for the worker nodes.

Initialize docker swarm on the control node.
```
docker swarm init --advertise-addr <YOUR CONTROL NODE IP>
```

Join the cluster on all the worker nodes.
```
docker swarm join —token <TOKEN>
```
Check that all nodes are up on manager.
```
docker node ls
```

Output:
```
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
cc412r0dxcw5nytve164ofwse *   control    Ready     Active         Leader           20.10.8
0jj8ij3fsqvex6lnhm6c5jfme     node1      Ready     Active                          20.10.8
ireae2686omwny2bjv9jsrm5o     node2      Ready     Active                          20.10.8
4316lwypmd3rn55y8estg0xh8     node3      Ready     Active                          20.10.8

```
