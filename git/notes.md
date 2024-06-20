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

# 
Set remote URL
```
git remote set-url origin https://github.com/user/repo2.git
```

Add Remote URL
```
git remote add origin https://github.com/user/repo2.git
```

# Configure Multiple Github accounts
generate keys
```
ssh-keygen -t rsa -C "Your Email Address"
```

- Public key will be added in github (.pub file)
- Private key will be reside in you PC


config
```
# vis7 - keep 'Host' as it is for default account
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa

# vis-websmith
Host github.com-vis-websmith
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_websmith
```


To test that your keys added in github successfully
```
ssh -T git@github.com-vis-websmith
```


# Cloning Repository
```
# syntax
git clone git@<HostName>:username/repository_name.git

git clone "git@github.com:vis7/notes.git"
git clone "git@github.com-vis-websmith:vis-websmith/scrapping_pharma_info.git"
```
