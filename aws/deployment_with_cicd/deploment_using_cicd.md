# Deploy
- https://realpython.com/django-nginx-gunicorn/#putting-your-site-online-with-django-gunicorn-and-nginx


# deployemnt using cicd
- add hostname and content of .pem file in github secret (Repository Secrets) (Name can be any)
AWS_HOST_NAME - ec2-13-233-186-81.ap-south-1.compute.amazonaws.com
AWS_SSH_KEY - content of (.pem file (private key at the time of creating instance))

- use deploy.yml file and make changes accordingly

That's It deployment using cicd is done.

# make website secure using API Gateway
- create API Gateway
- http api (It can be any) -> build -> give name -> next util you can go (It will create and add default stage) -> create
- route -> create -> path = $default -> attech integration -> http uri -> provide ip name in url -> create

