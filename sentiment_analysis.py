# Import all relevant libraries
import pandas as pd
import spacy
import random
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the 'en_core_web_sm' language model
# Load the more advanced language model which includes word vectors 
# This will allow more accurate similarity analysis to be performed
nlp = spacy.load("en_core_web_md")

# Add spacytextblob to the nlp pipeline so sentiment analysis can be performed
nlp.add_pipe("spacytextblob")

# Convert the amazon product reviews csv file to a pandas dataframe
df = pd.read_csv("amazon_product_reviews.csv")

# Select the 'reviews.text' column from the dataframe
reviews_data = df['reviews.text']


# Clean all the data in the 'reviews.text' column 
# Remove all missing values from the 'reviews.text' column
reviews_data.dropna(inplace = True)


# Convert all items into a string
# Remove any leading and trailing spaces
reviews_data = reviews_data.astype(str).str.strip()

# Select two random reviews for analysis
reviews_list = random.sample(list(reviews_data), k=2) # Select two random reviews to undergo sentiment and similarity analysis 
first_review = reviews_list[0] # First random review
second_review = reviews_list[1] # Second random review

# Print the selected reviews
print(f"1st review: {first_review} \n")
print(f"2nd review: {second_review} \n")

# Define function for sentiment analysis 
def sentiment_analysis(review):

    # Convert review string into lower case characters and then into an nlp doc object
    doc = nlp(review.lower()) 

    # Tokenize the doc object but exclude any tokens that are stop words
    token_list = [token.orth_ for token in doc if not token.is_stop]

    # Convert the tokenized list back into an nlp doc string without stop words
    cleaned_review = nlp(" ".join(token_list))
   
    # Perform sentiment analysis on the review to obtain the polarity and subjectivity scores
    sentiment = cleaned_review._.blob.sentiment

    # The function returns the sentiment analysis metrics for the chosen review
    return sentiment


# Print the sentiment analysis metrics for the two previously selected reviews
print(f"Sentiment analysis for 1st review: {sentiment_analysis(first_review)} \n")
print(f"Sentiment analysis for 2nd review: {sentiment_analysis(second_review)} \n")

''' Note: The polarity attribute measures the strength of the sentiment in a product review.
    A polarity score of 1 indicates a very positive sentiment, while a polarity score of -1 
    indicates a very negative sentiment. A polarity score of 0 indicates a neutral sentiment.
'''

''' Note: The subjectivity attribute measures the extent to which a sentiment in a product review
    is subjective or objective. It is a floating point between 0.0 and 1.0 inclusive where 0 denotes
    an objective sentiment and a subjectivity score of 1 denotes a subjective sentiment.
'''


# Define function for similarity analysis
# This function will return the similarity score between the two previously selected reviews
def similarity_analysis(review_1, review_2):
    return nlp(review_1).similarity(nlp(review_2))

print(f"The similarity score between these two reviews is {similarity_analysis(first_review, second_review)}")

''' Note: A similarity score of 1 indicates that the two reviews are
    more similar, while a similarity score of 0 indicates that the two 
    reviews are not similar.'''

