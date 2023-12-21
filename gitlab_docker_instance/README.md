# GitLab Docker Instance
Spin up a working GitLab environment, including runners locally.

# Usage
See [Dependencies](#dependencies)

Start gitlab via and wait:
```bash
docker-compose up
```

- Visit `localhost:8888`
- Login with credentials:
```
root
some_initial_password
```



# Dependencies
- Docker
- Docker-compose


#  Problems
### Pushing to locahost via SSH
Set gitlab_rails `gitlab_ssh_host` and `gitlab_shell_ssh_port` and add portforwarding:
```
environment:
      GITLAB_OMNIBUS_CONFIG: |
        gitlab_rails['gitlab_ssh_host'] = "localhost"
        gitlab_rails['gitlab_shell_ssh_port'] = 2222

[...]

    ports:
      - '2222:22'
```


### Error registering runner with --registration-token option
> Support for registration tokens and runner parameters in the 'register' command has been deprecated in GitLab Runner 15.6:

Apparently now use the `--token` parameter instead of `--registration-token`t

 URL: https://docs.gitlab.com/ee/ci/runners/new_creation_workflow#changes-to-the-gitlab-runner-register-command-syntax



# Links
OF https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
shamelessly copied from: https://github.com/lalatgithub/gitlab-in-docker/blob/master/4.%20auto-register-gitlab-runner-with-docker-executor/docker-compose.yml
