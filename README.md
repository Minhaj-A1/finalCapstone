# Sentiment and Similarity Analysis
This repository includes the code for the final capstone project from HyperionDev's Data Science fundamentals course concerning sentiment and similarity analysis. 

This README file contains the following contents:
1. [Description of Project](#desc)
2. [Importance of Project](#imp)
3. [Installation Instructions](#install)
4. [Testing the Code](#test)
5. [Credits](#cred)

<a name="desc"></a>
### 1. Description of Project
This project highlights one of the applications of NLP (Natural Language Processing). It includes a Python program that performs sentiment and similarity analysis for a dataset of amazon product reviews (csv file). This involves identifying if reviews are positive or negative as well as comparing how similar reviews are to each other. 

<a name="imp"></a>
### 2. Importance of Project
Sentiment and Similarity Analysis is important as it helps organisations, such as Amazon, check brand and product opinion in customer feedback in order to better understand customer needs. This can translate into improving customer loyalty and retention through the implementation of better services and products. 

<a name="install"></a>
### 3. Installation Instructions
To run this project, the python program file entitled "sentiment_analysis.py" and the dataset of product reviews entitled "amazon_product_reviews.csv" should be downloaded locally onto your computer. Please ensure both files are saved in the same working directory. 

For the program to run successfully, python libraries such as pandas and spacy must be installed on your computer. In addition the spacy language models "en_core_web_sm" and "en_core_web_md" must be installed on your computer. Please use the web for detailed instructions on how to do this. 

<a name="test"></a>
### 4. Testing the Code
Once the files are downloaded, an IDE of your choice can be used to execute the code such as VS Code. Ensure that the working directory is set to the same directory that contains the python code and the dataset of amazon reviews. This will mean that the program is able to read the dataset csv file for the the amazon product reviews since it is in the same working directory. 

The code can also be modified if the user wants to test the code on a different dataset of reviews. 

The code will output 2 product reviews randomly selected from the dataset and will perform sentiment analysis on both reviews. This involves a polarity score and a subjectivity score for both reviews. A higher polarity score indicates a more positive sentiment and a higher subjectivity score indicates a higher subjective sentiment (0 subjectivity score indicates an objective review). The code will also output the similarity score between the 2 randomly selected reviews where a higher score is an indication of the reviews being more similar to each other. 

The below code output highlights an example of the program being run:

![image](https://github.com/Minhaj-A1/finalCapstone/assets/83793815/3b82a7da-aae3-40f0-b441-f1daf4e2ff93)

<a name="cred"></a>
### 5. Credits
This project is created solely by me (Minhaj Ahmed). 
