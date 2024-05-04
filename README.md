# Sentiment-Analysis

Python code appears to be a comprehensive analysis of sentiment in product reviews using machine learning techniques. Here's a detailed overview based on the code :-

<h3>Data Import and Exploration:</h3>
Imported necessary libraries including matplotlib, pandas, numpy, and seaborn.
Loaded the dataset from a CSV file using pd.read_csv.
Conducted initial exploration of the dataset using methods like .head(), .describe(), and .info() to understand its structure and contents.<br>

<h3>Data Visualization:</h3>
Visualized various aspects of the dataset to gain insights:
Histograms of reviews.numHelpful and reviews.id for distribution analysis.
Countplot of reviews.rating to visualize the distribution of ratings.
Bar plots to analyze the frequency of ASINs (Amazon Standard Identification Numbers) in the dataset.

<h3>Data Preprocessing:</h3>
Removed NaN values from the reviews.rating column.
Converted reviews.rating to integer type.
Used StratifiedShuffleSplit for stratified sampling to split the dataset into training and testing sets while maintaining class distribution.<br>

<h3>Feature Engineering:</h3>
Derived additional features such as sentiment labels (Positive, Neutral, Negative) based on the rating scores.<br>

<h3>Data Analysis:</h3>
Analyzed ASIN frequency and ratings distribution.
Plotted point plots to visualize the relationship between ASINs and review ratings.<br>

<h3>Sentiment Analysis:</h3>
Defined a function sentiments() to classify ratings into positive, neutral, and negative sentiments.
Applied the sentiment classification function to both training and testing datasets.
Visualized the distribution of sentiment labels in both training and testing datasets using bar plots.

<br>

<p>Overall, your project demonstrates a structured approach to sentiment analysis of product reviews using Python and machine learning. It covers data preprocessing, exploration, visualization, feature engineering, and sentiment classification, providing valuable insights into customer sentiments towards different products.</p>
<br>
<img width="956" alt="Screenshot 2024-05-05 030212" src="https://github.com/Shivamup51/Sentiment-Analysis/assets/166123727/d07d1651-faa9-4a85-ba06-0636e54be5cd">
<img width="957" alt="Screenshot 2024-05-05 030252" src="https://github.com/Shivamup51/Sentiment-Analysis/assets/166123727/1affb41d-d8f5-4d38-95c9-da67b13e9bfc">
<img width="956" alt="Screenshot 2024-05-05 030314" src="https://github.com/Shivamup51/Sentiment-Analysis/assets/166123727/fe72bcc0-61e4-4cb8-b294-242964fdd128">
<img width="957" alt="Screenshot 2024-05-05 030334" src="https://github.com/Shivamup51/Sentiment-Analysis/assets/166123727/777eb457-f669-466d-91fc-86383d89d351">
<br>
<img width="118" alt="Screenshot 2024-05-05 030423" src="https://github.com/Shivamup51/Sentiment-Analysis/assets/166123727/fda065f4-8cd9-4394-a7c7-0a69b17fc703">


