# boffyn

Install and manage your self-hosted docker compose stack with one manifest.

Define the sites and applications you want to your server to serve in a single yaml
file, then use boffyn to provision a server, deploy the stack, and help you manage your
docker compose installation.

Designed to serve static frontend sites, server-side projects and services, and a wide
range of off-the-shelf applications.

Coming soon.

## Installation

Install with [uv](https://docs.astral.sh/uv/#installation):

```
uv tool install boffyn
```

or install with pip:

```
pip install boffyn
```


## Usage

Once installed you can call either `boffyn` or the shorter alias `boff`:

First define your manifest in a YAML file - let's use the hello world demo:

```
curl -o hello-world.yml https://raw.githubusercontent.com/boffyn/boffyn/refs/heads/main/examples/hello-world.yml
boff use hello hello-world.yml
```

The manifest tells Boffyn where your server is, and what apps (websites and applications) to install on it.

Update the host and username variables to point at your server.

Wire up your own projects as apps within the manifest.

Then you can set up your server and deploy the apps with:

```
boff provision
boff deploy
```
