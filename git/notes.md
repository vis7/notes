# Initialize repo
- Create repo in github
- Create project in local using django-admin startproject (if not already have project)
- Go inside your project

```
git init
git remote add origin <your repo url>
git pull origin main

# current branch is master if you want to change it to main
git branch -m master main

# than it is ready to commit
git add .
git commit -m "your message"
git push origin main
```

Another method is to clone repo in local then add (move) your code in repository, than it is ready to commit


- To remove cached file from github
```
git rm --cached -r */*/__pycache__/
```
