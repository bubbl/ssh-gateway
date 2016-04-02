# SSH Gateway

A simple Python SSH menu in a Docker container.

## Configuration

1. Pull the image from Docker Registry:

```
docker pull bbania/ssh-gateway
```

2. Create an SSH key with

```
ssh-keygen -t rsa -b 4096 -C <your_comment>
```

3. Create `ssh_config` file with list of your hosts.

File format:

```
Host node1
  IdentityFile ~/.ssh/id_rsa
  HostName my.host.ip
  User user
  Port 22
```

4. Add the ssh key to remote hosts.

## Running container

Pass ssh key and ssh_config to the container as volumes:

```
docker run --rm -it \
  -v /path/to/ssh_config:/etc/ssh/ssh_config \
  -v /path/to/ssh-key:/root/.ssh/id_rsa \
  bbania/ssh-gateway
```

