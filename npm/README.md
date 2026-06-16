# boffyn

Install and manage your self-hosted docker compose stack with one manifest.

Define the sites and applications you want to your server to serve in a single yaml
file, then use boffyn to provision a server, deploy the stack, and help you manage your
docker compose installation.

Designed to serve static frontend sites, server-side projects and services, and a wide
range of off-the-shelf applications.

This is a convenience wrapper to make it easy for JavaScript developers to install
Boffyn and manage it with their other project dependencies.

## Installation

Install boffyn with:

```
npm install -g boffyn
```

Either install this on your local Linux or macOS machine, or install and run it directly
on your Linux server.

Upgrade boffyn as you would any other npm package.


## Usage

Once installed, follow the standard usage instructions:

```
boff use host.yml
boff provision
boff deploy
```
