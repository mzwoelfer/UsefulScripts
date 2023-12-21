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


# Links
OF https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
shamelessly copied from: https://github.com/lalatgithub/gitlab-in-docker/blob/master/4.%20auto-register-gitlab-runner-with-docker-executor/docker-compose.yml
