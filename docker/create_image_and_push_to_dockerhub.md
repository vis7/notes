- create Dockerfile using below content
```
# STEP 1: Install base image. Optimized for Python.
FROM python:3.8-slim-buster

# Step 2: Add requirements.txt file 
COPY requirements.txt /requirements.txt

# Step 3:  Install required pyhton dependencies from requirements file
RUN pip install -r requirements.txt

# Step 4: Copy source code in the current directory to the container
ADD . /app

# Step 5: Set working directory to previously added app directory
WORKDIR /app

# Step 6: Expose the port Flask is running on
EXPOSE 8501

# Step 9: Run Flask
CMD ["nohup", "tensorflow_model_server", "--rest_api_port=8501", "--model_name=my_mnist_model", "--model_base_path=${MODEL_DIR}", ">", "server.log", "2>", "err.txt"]
```

- create image from Dockerfile
docker build -t tensorflow-serving-docker .

- verify image created successfully
docker run <image_name> # verify that commands run successfully
docker images

# Push docker image to dockerhub
- login to dockerhub
docker login -u username

- assign your local image_id a name
docker tag 12db06a17aa4 vishvajeetramanuj95/tensorflow-serving-docker:latest

- push your image to dockerhub
docker push vishvajeetramanuj95/tensorflow-serving-docker:latest


