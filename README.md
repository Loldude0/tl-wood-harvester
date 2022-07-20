### tl-wood-harvester

harvests wood for you

## how to use(in simple terms)

# With Tensorflow Serving on Linux

note - I recommend you to do this in a virtual machine

Step 1 - make sure you have python installed, preferably the latest version

Step 2 - ensure that Tensorflow is installed, if not, run this command - ```python3 -m pip install tensorflow```

Step 3 - install tensorflow-model-server with these commands
  ```echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && \ curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add - ```
  ```apt-get update && apt-get install tensorflow-model-server```
	
Step 4 - create 2 folders with different names and upload the folders containing the model and rename them to "1", make sure you know which one is model1 and model2

Step 5 - run this command to run them in different terminals for both of them, make sure both have different ports ```tensorflow_model_server --model_base_path=directory --rest_api_port=port --model_name=name```

Step 6 - run the script, make sure you change the url within them, getDistance is model2

# Windows

you need to use Tensorflow Serving with Docker, follow the official guide and in the end perform Step 6 as given above

https://www.tensorflow.org/tfx/serving/docker

