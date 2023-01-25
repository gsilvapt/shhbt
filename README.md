<p align="center">
  <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="Python" />
  <img src="https://img.shields.io/github/workflow/status/paddypowerbetfair/shhbt/CI%20Process?style=plastic" alt="CI Build" />
  <a href='https://coveralls.io/github/PaddyPowerBetfair/shhbt?branch=main'><img src='https://coveralls.io/repos/github/PaddyPowerBetfair/shhbt/badge.svg?branch=main' alt='Coverage Status' /></a>
</p>

# shhbt  

shhbt (**shh**git for **b**lue **t**eams) is a modification of the original [shhgit](https://github.com/eth0izzle/shhgit) 
idea, to help blue teams proactively target, detect and avoid leaking sensitive data into public repositories.

To do so, this tool integrates with different Git host services, namely GitHub and GitLab, and runs the core scanner at 
each merge/pull request.
If it finds a secret, then it sets the status as failed (red, merge at your own risk), if not then it marks it as success.

The scanner also picks up custom configs from the repository, which allows users to add custom secret signatures and 
patterns, as well as remove the ones that are not necessary. 

Check the [shhbt_config.yaml](./shhbt_config.yaml) file to see how it is organised and add your own in your project! 


## CONTRIBUTING  
This is an internal project developed at [PaddyPower Betfair](https://github.com/paddypowerbetfair), and we use it in 
our own internal security controls. Despite that contributions are welcome, and we would like to encourage any developer 
to contribute to the project, either with code, issue triaging, feature proposals, and other tweaks.

All contributors should be familiar and respect the [code of conduct](./CODE_OF_CONDUCT.md) 

To get started, please read the [CONTRIBUTING.md](./CONTRIBUTING.md)


## INSTALLING & RUNNING  
To install and setup the tool to run, you need to:
1. Install the project dependencies (`pip install -r requirements.txt`);
1. Define the environment variables in a `.env` file ;
1. Start the start;
1. configure the webhook in the project's settings.

To install the project dependencies, simply run 
variables, and get the server running. After getting the server running, you only need to configure the webhook in the 
project's settings.

Before that t, considering you are under an environment with **Python 3.9**, and in a Unix-based environment 
(Windows users, please adapt the commands accordingly):
- `git clone git@github.com/paddypowerbetfair/shhbt.git`
- `cd shhbt`
- `python -m venv env`
- `source env/bin/active`
- `pip install -r requirements.txt`
- Create a `.env` file to contain, at least, the following keys and valid values: `CONFIG_LOCATION` (which should target 
  the `shhbt_config.yaml` that exists in this repository or yours if you need any customization); `GITLAB_URI` and `GITLAB_TOKEN`.
- If everything was done successfully, then running `flask run` inside the project's directory will start a flask server.

Now that you have the server running, you either use a service like [ngrok](https://ngrok.com/) to set-up a secure 
tunnel, and to receive the hooks simply paste the link ngrok provides in the **repository webhooks settings**, or, if 
you installed it and are running in a remote server with that open port, you can use your server's IP to configure the 
webhook.
In GitLab, the triggers you will need are **push events**, and **merge requests events**. It's recommended to use SSL.
