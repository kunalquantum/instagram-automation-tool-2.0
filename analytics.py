import streamlit as st
def main_page():
    # Add a header with the title
    st.title("Analytics for instagram")

    # Sidebar for navigation
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to ", ["Sentiment Analysis", "User Segmentation"])

    if page == "Sentiment Analysis":
        sentiment()
    elif page == "User Segmentation":
        segment()
    elif page == "Followers insights":
        follow()
   



def sentiment():
    import streamlit as st
    import pandas as pd
    from textblob import TextBlob
    import matplotlib.pyplot as plt
    import seaborn as sns
    from wordcloud import WordCloud
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import LatentDirichletAllocation
    import pyLDAvis
    import umap

    # Upload a CSV file
    st.title("Advanced Sentiment Analysis App")

    uploaded_file = st.file_uploader("Upload a CSV file with comments", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
        # Display the raw data
        st.subheader("Step 1: Upload Your Data")
        st.write("Great! You've uploaded your data. Let's get started.")

        if 'Comment Text' in data.columns:
            st.subheader("Step 2: Data Cleaning and Sentiment Analysis")
            
            # Remove missing values
            data = data.dropna(subset=['Comment Text'])
            
            # Sentiment Analysis
            def analyze_sentiment(comment):
                analysis = TextBlob(comment)
                sentiment_score = analysis.sentiment.polarity
                if sentiment_score > 0:
                    return 'Positive'
                elif sentiment_score < 0:
                    return 'Negative'
                else:
                    return 'Neutral'

            data['Sentiment'] = data['Comment Text'].apply(analyze_sentiment)

            # Data Visualization
            st.subheader("Step 3: Sentiment Analysis Results")
            st.write("We've performed sentiment analysis on the comments. Here are the results:")

            sentiment_counts = data['Sentiment'].value_counts()
            st.bar_chart(sentiment_counts)
            
            # Word Cloud Visualization
            st.subheader("Step 4: Word Cloud Visualization")
            st.write("Let's visualize word clouds for each sentiment category.")
            sentiment_categories = data['Sentiment'].unique()
            
            for sentiment in sentiment_categories:
                comments = data[data['Sentiment'] == sentiment]['Comment Text']
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(comments))
                st.subheader(f"{sentiment} Comments")
                st.image(wordcloud.to_image())
            
            # Advanced Analysis
            st.subheader("Step 5: Advanced Analysis")
            st.write("Let's explore the comments in more depth.")
            
            # Interactive Exploration
            st.subheader("Interactive Exploration")
            st.write("Filter and explore comments interactively:")
            sentiment_filter = st.selectbox("Select a sentiment:", sentiment_categories)
            filtered_comments = data[data['Sentiment'] == sentiment_filter]
            st.write(filtered_comments.head(10))
            
            # Topic Modeling
            st.subheader("Topic Modeling")
            st.write("Discover topics within the comments using Latent Dirichlet Allocation (LDA).")
            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
            tfidf = tfidf_vectorizer.fit_transform(data['Comment Text'])
            lda = LatentDirichletAllocation(n_components=5, random_state=42)
            lda.fit(tfidf)
            st.write("Top words for each topic:")
            for topic_idx, topic in enumerate(lda.components_):
                top_words = [tfidf_vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-5:-1]]
                st.write(f"Topic {topic_idx + 1}: {', '.join(top_words)}")
            
            
            
        else:
            st.warning("No 'Comment Text' column found in the uploaded dataset. Please check the file.")

    else:
        st.subheader("Step 1: Upload Your Data")
        st.write("Please upload a CSV file with comments to get started.")

def segment():
    import streamlit as st
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import LatentDirichletAllocation
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    from textblob import TextBlob
    import spacy
    from collections import Counter
    import plotly.express as px
    import plotly.graph_objects as go

    # Load the spaCy NLP model for NER
    nlp = spacy.load("en_core_web_sm")

    # Upload a CSV file with user text data
    st.title("Advanced User Segmentation App")

    uploaded_file = st.file_uploader("Upload a CSV file with user text data", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Sidebar options
        st.sidebar.subheader("User Segmentation Options")
        num_topics = st.sidebar.number_input("Number of Topics", min_value=2, max_value=10, value=3)
        perform_sentiment_analysis = st.sidebar.checkbox("Perform Sentiment Analysis")
        perform_ner = st.sidebar.checkbox("Perform Named Entity Recognition")

        # Data preprocessing
        st.subheader("Data Preprocessing")
        st.write("Let's preprocess the text data before user segmentation.")

        # Assuming the dataset has a 'Text' column with user text data
        text_data = data['Comment Text']  # Replace 'Text' with the actual column name

        # Handle missing values
        text_data = text_data.dropna()

        if not text_data.empty:
            # Vectorize the text data using TF-IDF
            tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
            tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

            # User segmentation using LDA
            st.subheader("User Segmentation")
            st.write("Let's segment users based on topics in their text data using Latent Dirichlet Allocation (LDA).")

            lda = LatentDirichletAllocation(n_components=num_topics, random_state=0)
            topics = lda.fit_transform(tfidf_matrix)

            # Add topic labels to the original data
            data = data.iloc[text_data.index]  # Keep only rows without missing values
            data['Topic'] = topics.argmax(axis=1)

            st.write("Topic assignments:")
            st.write(data)

            # Topic visualization
            st.subheader("Topic Visualization")
            st.write("Explore the user segments based on topics.")

            # Create a bar chart to show the distribution of topics
            topic_counts = data['Topic'].value_counts().sort_index()
            st.bar_chart(topic_counts)

            # Dynamic word cloud for each topic
            st.subheader("Word Clouds for Each Topic")
            st.write("Explore the most frequent words in each topic.")

            for topic_id in range(num_topics):
                st.subheader(f"Topic {topic_id + 1}")
                topic_text = " ".join(data[data['Topic'] == topic_id]['Comment Text'])
                wordcloud = WordCloud(width=800, height=400).generate(topic_text)
                st.image(wordcloud.to_array())

            if perform_sentiment_analysis:
                # Sentiment analysis
                st.subheader("Sentiment Analysis")
                st.write("Analyze sentiment in user comments.")

                data['Sentiment'] = data['Comment Text'].apply(lambda x: TextBlob(x).sentiment.polarity)

                # Create a histogram to show sentiment distribution
                sentiment_chart = px.histogram(data, x="Sentiment", nbins=30)
                st.plotly_chart(sentiment_chart)

                # Sentiment-based conclusions
                st.subheader("Sentiment-Based Conclusions")
                sentiment_mean = data['Sentiment'].mean()
                sentiment_std = data['Sentiment'].std()

                if sentiment_mean > 0:
                    st.write("Overall, user comments are generally positive.")
                elif sentiment_mean < 0:
                    st.write("Overall, user comments are generally negative.")
                else:
                    st.write("Overall, user comments are relatively neutral.")

                st.write(f"Average Sentiment Score: {sentiment_mean:.2f}")
                st.write(f"Standard Deviation of Sentiment Scores: {sentiment_std:.2f}")

            if perform_ner:
                # Named Entity Recognition (NER)
                st.subheader("Named Entity Recognition (NER)")
                st.write("Identify named entities in user comments.")

                # Process each comment with spaCy
                entities = []
                for comment in data['Comment Text']:
                    doc = nlp(comment)
                    entities.extend([ent.text for ent in doc.ents])

                # Count and display named entities
                entity_counts = Counter(entities)
                st.write(entity_counts)

                # NER-based conclusions
                st.subheader("NER-Based Conclusions")
                if len(entities) > 0:
                    st.write("The most common named entities mentioned in comments are:")
                    top_entities = entity_counts.most_common(5)
                    for entity, count in top_entities:
                        st.write(f"{entity}: {count} mentions")
                else:
                    st.write("No named entities were identified in the comments.")

        else:
            st.warning("No valid text data found. Please ensure the 'Text' column does not contain missing values.")

    else:
        st.subheader("Upload User Text Data")
        st.write("Please upload a CSV file with user text data to get started.")
def follow():
    import streamlit as st
    import pandas as pd

    # Define a function to process followers for each user
    def process_followers(user_data):
        # Simulate the processing of followers for each user
        followers_list = []
        for username in user_data['Username']:
            # Replace this with your actual code to fetch followers for each user
            # Example: followers = fetch_followers(username)
            followers = [f"follower_{i}" for i in range(1, 6)]  # Simulated followers
            followers_list.append(followers)
        
        return followers_list

    # Upload a CSV file with user data
    st.title("Followers Processing App")

    uploaded_file = st.file_uploader("Upload a CSV file with user data", type=["csv"])
    if uploaded_file is not None:
        user_data = pd.read_csv(uploaded_file)

        # Data preprocessing
        st.subheader("Data Preprocessing")
        st.write("Let's preprocess the user data and process followers.")

        # Assuming the dataset has a 'Username' column
        usernames = user_data['Username']

        # Process followers for each user
        followers_list = process_followers(user_data)
        
        # Ensure the number of followers matches the number of users
        if len(followers_list) != len(user_data):
            st.warning("The number of followers does not match the number of users.")
        else:
            # Add a 'Followers' column to the DataFrame
            user_data['Followers'] = followers_list

            # Display the updated DataFrame
            st.subheader("Updated User Data with 'Followers' Column")
            st.write(user_data)

            # Iterate through and display followers
            st.subheader("Followers List")
            for i, (username, followers) in enumerate(zip(usernames, followers_list)):
                st.write(f"User: {username}")
                st.write(f"Followers: {', '.join(followers)}")
                st.write("-" * 50)  # Separator

    else:
        st.subheader("Upload User Data")
        st.write("Please upload a CSV file with user data to get started.")

main_page()