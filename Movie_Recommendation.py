# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:29:54 2021

@author: Minh Nguyen

@inspired by: Niharika Pandit, Subin An
"""


import pandas as pd
import numpy as np
import seaborn as sns
import missingno as msno
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Read in the file:
data = pd.read_csv ('netflix_titles.csv')
data.shape
data.isna().sum()

#Drop missing value for Date_added and rating (only a few)
data = data[data['rating'].notna()]
data = data[data['date_added'].notna()]
data['country'] = data['country'].fillna(data['country'].mode()[0])
data = data.fillna('')
#Visualize and fill NULL for top 20 country:
data['country'] = data['country'].fillna(data['country'].mode()[0])
country =data['country'].str.get_dummies(sep=', ').sum() #strip the cells
country.sort_values(ascending=False, inplace = True)
top_country = country[:20]

from matplotlib import gridspec

fig = plt.figure(figsize=(20, 6))
gs = gridspec.GridSpec(nrows=1, ncols=2,
                       height_ratios=[6], 
                       width_ratios=[5, 10]) #width of two charts

ax = plt.subplot(gs[1]) # put this chart in 2nd place.
sns.barplot(top_country.index, top_country, ax=ax, palette="RdGy") 
ax.set_xticklabels(top_country.index, rotation='90')
ax.set_title('Top 20 producing countries', fontsize=15, fontweight='bold')

explode = [0 for _ in range(20)]
explode[0] = 0.06

ax2 = plt.subplot(gs[0])
ax2.pie(top_country, labels=top_country.index,
        shadow=True, startangle=0, explode=explode,
        colors=sns.color_palette("RdGy", n_colors=20)
       )
ax2.axis('equal') 

plt.show()


#Visualize the correlation between 5 top countries and time
top5 = country[:5]
country_name = top5.index.tolist() #convert top 20 countries to list
data2 = data[data['country'].isin(country_name)] #Subset data based on a list

year_country = data2.groupby('release_year')['country'].value_counts().reset_index(name='counts')
### Only take movies before 2020 because of the sharp decline in movies production as a result of Covid-19
year_country = year_country[(year_country['release_year'] >= 1990)  & (year_country['release_year'] < 2020)] 
sns.lineplot(data = year_country, x ='release_year', y ='counts', 
             hue = 'country').set_title('Production rate of 5 top countries')


# Movies and TV Shows visualization:
movie = data2[data2['type'] == 'Movie']
tv_show = data2[data2['type'] == 'TV Show']

### Plot the TV_Show and Movie: 
movie_plot = sns.countplot( x = 'type', data= data2, palette="rocket")

### Make the dataframe of TV show and Movies:
show_date = tv_show[['date_added']]
show_date['year'] = show_date['date_added'].apply(lambda x : x.split(', ')[-1])
show_date['month'] = show_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

movie_date = movie[['date_added']]
movie_date['year'] = movie_date['date_added'].apply(lambda x : x.split(', ')[-1])
movie_date['month'] = movie_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April',
               'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December'][::-1]

df = show_date.groupby('year')['month'].value_counts()
df = df.unstack().fillna(0)[month_order].T #for transforming df into a regular dataframe

df2 = movie_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order].T

### Visualize the correlation between Months and number of produced shows:
plt.figure(figsize=(15, 7), dpi=200)

gs = gridspec.GridSpec(nrows=1, ncols=2,
                       height_ratios=[6], 
                       width_ratios=[10, 10])

ax = plt.subplot(gs[1])
plt.pcolor(df, cmap='gist_heat_r', edgecolors='white', linewidths=2) # heatmap
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, fontsize=7, fontfamily='serif')
plt.yticks(np.arange(0.5, len(df.index), 1), df.index, fontsize=7, fontfamily='serif')

plt.title('Netflix TV Shows Release Date', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))

cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=8) 
cbar.ax.minorticks_on()

ax2 = plt.subplot(gs[0])
plt.pcolor(df2, cmap='gist_heat_r', edgecolors='white', linewidths=2) # heatmap
plt.xticks(np.arange(0.5, len(df2.columns), 1), df2.columns, fontsize=7, fontfamily='serif')
plt.yticks(np.arange(0.5, len(df2.index), 1), df2.index, fontsize=7, fontfamily='serif')

plt.title('Netflix Movies Release Date', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))

cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=8) 
cbar.ax.minorticks_on()

plt.show()

# Movies Rating Visualization: 
rating_order =  ['G', 'TV-Y', 'TV-G', 'PG',
                 'TV-Y7', 'TV-Y7-FV', 'TV-PG',
                 'PG-13', 'TV-14', 'R', 'NC-17', 'TV-MA']

movie_rating = movie['rating'].value_counts()[rating_order]

def rating_barplot(data, title, height, h_lim=None):
    fig, ax = plt.subplots(1,1, figsize=(20, 10))
    if h_lim :
        ax.set_ylim(0, h_lim)
    ax.bar(data.index, data,  color="#d0d0d0", width=0.6, edgecolor='black')

    color =  ['green',  'blue',  'orange',  'red']
    span_range = [[0, 2], [3,  6], [7, 8], [9, 11]]

    for idx, sub_title in enumerate(['Little Kids', 'Older Kids', 'Teens', 'Mature']):
        ax.annotate(sub_title,
                    xy=(sum(span_range[idx])/2 ,height),
                    xytext=(0,0), textcoords='offset points',
                    va="center", ha="center",
                    color="w", fontsize=16, fontweight='bold',
                    bbox=dict(boxstyle='round4', pad=0.4, color=color[idx], alpha=0.6))
        ax.axvspan(span_range[idx][0]-0.4,span_range[idx][1]+0.4,  color=color[idx], alpha=0.1)

    ax.set_title(f'Distribution of {title} Rating', fontsize=20, fontweight='bold', position=(0.5, 1.0+0.03))
    plt.show()
    
rating_barplot(movie_rating,'Movie', 1200)

# Word Cloud of Movie Genres:
movie['genre'] = movie['listed_in'].apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(',')) 
from wordcloud import WordCloud

text = str(list(movie['genre'])).replace(',', '').replace('[', '').replace("'", '').replace(']', '')

plt.rcParams['figure.figsize'] = (15, 15)
wordcloud = WordCloud(background_color = 'white', width = 1200,  height = 1200, max_words = 121).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

#Import IMDB rating for recommendation system:
## Link: https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+ratings.csv

imdb_ratings=pd.read_csv('IMDb ratings.csv',usecols=['weighted_average_vote'])
imdb_titles=pd.read_csv('IMDb movies.csv', usecols=['title','year','genre'])
ratings = pd.DataFrame({'Title':imdb_titles.title,
                    'Release Year':imdb_titles.year,
                    'Rating': imdb_ratings.weighted_average_vote,
                    'Genre':imdb_titles.genre})
ratings.drop_duplicates(subset=['Title','Release Year','Rating'], inplace=True)
ratings.dropna()
ratings.shape

data3 = ratings.merge(data, left_on ='Title', 
                      right_on = 'title', how = 'inner') #Merge ratings to Netflix
data3.info()
data3.to_csv('data3.csv')
data3['Rating'].value_counts()

#Recommendation system using Movies Features:
features=['title','director','cast','listed_in','description']
data4 = data[features]

def clean_data(x):
        return str.lower(x.replace(" ", ""))

for feature in features:
    data4[feature] = data4[feature].apply (clean_data )

def create_words(x):
    return x['title']+ ' ' + x['director'] + ' ' + x['cast'] + ' ' +x['listed_in']+' '+ x['description']

data4['words'] = data4.apply(create_words, axis = 1)             

### Parameter for the algorithim:
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(data4['words'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)           
             
data4 = data4.reset_index()             
indices = pd.Series(data4.index, index=data4['title'])             

def get_recommendations(title, cosine_sim2=cosine_sim2):
    title=title.replace(' ','').lower()
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim2[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return data['title'].iloc[movie_indices]
### Testing the recommendation system:
    
get_recommendations('3 Idiots', cosine_sim2)

get_recommendations('Black Mirror', cosine_sim2)
get_recommendations('Black Panther', cosine_sim2)
get_recommendations('Django Unchained', cosine_sim2)

