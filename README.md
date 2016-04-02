# SSH Gateway

A simple Python SSH menu in a Docker container.

![alt Gateway Menu](screenshots/gateway.png "Gateway Menu")

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
  1.File format:
  ```
  Host node1
    IdentityFile ~/.ssh/id_rsa
    HostName my.host.ip
    User user
    Port 22
  ```
4. Edit menu.py `menu_data` to set menu entries for your hosts
  1. Format:
    * **title** - provides menu title
    * **subtitle** - additional title for menu
    * **type** (takes either `MENU` or `COMMAND` values):
      * **MENU** - creates a menu entity (requires `subtitle` to be set as well as `options` for submenu)
      * **COMMAND** - executes a shell command
![alt Gateway Submenu](screenshots/node_menu.png "Submenu")
5. Add the ssh key to remote hosts.

## Running container

Pass ssh key and ssh_config to the container as volumes:

```
docker run --rm -it \
  -v /path/to/ssh_config:/etc/ssh/ssh_config \
  -v /path/to/ssh-key:/root/.ssh/id_rsa \
  bbania/ssh-gateway
```

