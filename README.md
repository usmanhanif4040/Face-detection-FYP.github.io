# Gender and age detection

# Functionality and Features

Users can register & sign-in into the app.

It is connected to a database to store user details and passwords which are hashed and stored.

We use the Demographic Model from Clarifai which along with Face Detection offers probably values for age and gender.

The user can input an image url and utilizing the Clarifai API the response is used to calculate the Face Highlight box and also display Number of Faces Detected in the supplied image.

For images with single face both number of faces detected and other details are displayed whereas for images with multiple faces only number of detected faces is displayed.

# Principles
Everything should be 100% responsive
Everything should be readable on any device
Everything should be as fast as possible
Designing in the browser should be easy
It should be easy to change any interface or part of an interface without breaking any existing interfaces
Doing one thing extremely well promotes reusability and reduces repetition
Documentation helps promote reusability and shared knowledge
CSS shouldn't impede accessibility or the default functionality of HTML
You should send the smallest possible amount of code to the user

# Features
Mobile-first CSS architecture
490 accessible color combinations
8px baseline grid
Multiple debugging utilities to reduce layout struggles
Single-purpose class structure
Optimized for maximum gzip compression
Lightweight (~14kB)
Usable across projects
Growing open source component library
Works well with plain HTML, React, Ember, Angular, Rails and more
Infinitely nestable responsive grid system
Built with PostCSS

# Facial-Expression-Detection
Facial Expression or Facial Emotion Detector can be used to know whether a person is sad, happy, angry and so on only through his/her face. This Repository can be used to carry out such a task.

# PLAN

This is a three step process. In the first, we load the XML file for detecting the presence of faces and then we retrain our network with our image on five diffrent categories. After that, we import the label_image.py program and set up everything in realtime.

# DEPENDENCIES

Hit the following in CMD/Terminal if you don't have already them installed:

pip install tensorflow
pip install opencv-python
That's it for now.

So let's take a brief look at each step.

# STEP 1 - Implementation of OpenCV HAAR CASCADES

I'm using the "Frontal Face Alt" Classifier for detecting the presence of Face in the WebCam. This file is included with this repository.

Next, we have the task to load this file, which can be found in the label.py program. E.g.:

# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
Now everything can be set with the Label.py Program. So let's move to the next Step.

# STEP 2 - ReTraining the Network - Tensorflow Image Classifier

We are going to create an Image classifier that identifies whether a person is sad, happy and so on and then show this text on the OpenCV Window. This step will consist of several sub steps:

We need to first create a directory named images. In this directory, create five or six sub directories with names like Happy, Sad, Angry, Calm and Neutral. You can add more than this.

Now fill these directories with respective images by downloading them from the Internet. E.g., In "Happy" directory, fill only those images of person who are happy.

Now run the "face-crop.py" program.

Once you have only cleaned images, you are ready to retrain the network. For this purpose I'm using Mobilenet Model which is quite fast and accurate. To run the training, hit the got to the parent folder and open CMD/Terminal here and hit the following:


python retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images
That's it for this Step.


# STEP 3 - Importing the ReTrained Model and Setting Everything Up

Finally, I've put everything under the "label_image.py" file from where you can get evrything. Now run the "label.py" program by typing the following in CMD/Terminal:

 python label.py

It'll open a new window of OpenCV and then identifies your Facial Expression. We are done now!
