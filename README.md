# The Fish Market
#### Video Demo:  <https://youtu.be/7r9fjNLjTF8>
#### Description:


- Source of dataset : [Kaggle](https://www.kaggle.com/datasets/aungpyaeap/fish-market)

#### About the data :

- The dataset contains 3 types of lenghts , weight , height and specie of the fishes.

- After cleaninf the dataset i have used only one types of length ,  height and specie of the fishes in order to predict weight.

- weight of the fish is in grams while its length , height and width is in centimenters. 


#### Computation Involved :



1. The web application uses multiple linear regression to estimate the weight of a fish. The application, therefore, uses machine learning which was trained by data provided by Kaggle under name of the Fish market.

2. The project has an ML_model.py file in which the model is trained. the model uses linear regression to estimate the weight of a fish. The model depends upon user input of length, height, width, and specie of the fish in order to estimate its weight. In order to train our model I have used clear.linear model library from which the linear regression class was imported.


3. While length, height, and width are integer data provided by the user in layout.html, the specie attribute provides options for 3 types of fish Bream, Roach and Whitefish . all these 3 return values of 0,1, and 2 respectively which are used in the model. In order to Deal with nominal data we are converting them to integers using a label encoder in python.

4. Upon filling out the form the user is let into the "/calculate" directory where our model is stored. now in order to avoid training the model everyone we send a request the model is converted into a pickle file using the pickle module in python which can be  dumped or opened and on which incoming data can be easily applied so that our value is computed.

5. The value coming to the pickled model is then converted into a numpy array and then using the model. predict() method we are able to get our weight. This value is formatted to the 3rd decimal and sent back to our layout.html which jinja is used in order to generate a paragraph below which our weight is displayed.

6. I have addtionally used train test split model from sklearn model slection which allows me to divide my dataset into 2 parts containg 75% of data from training and 25% for testing. Using these parameters i was able to achieve avccuracy of 80%.


6. Requirements in python version 3
    - sklearn
    - flask
    - pandas
    - numpy
    - pickle
