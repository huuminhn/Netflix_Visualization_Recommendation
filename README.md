## Netflix_Visualization_Recommendation
*A story-telling projects using visualization and a content-based recommendation system*  

### EDA and Visualization:  
- The dataset itself is quite clear, except for three columns with a noticeable amount of missing values, namely
['director', 'cast', 'country']. On the other hand, the column *'Rating'* and *'Date_added'* only have 7 and 10 NULL values respectively.   
--> Drop missing value for *'Date_added'* and *'Rating'*, and filling the NULL of *'country'* with its mode.  

- **Visualize the production of the top 20 countries:**  
 <img src="Country.png?raw=true"/>
 It can be seen that the majority of the Movies and TV shows are produced by America with nearly 3,500 products, following by 
 India, UK, Canada and France. The top 5 countries made approximately 75% of the overall movies and shows of the whole world. Thereby, 
 we will be focusing our further visualization on the top 5 countries.   
 
-  Visualize the release date of TV shows and movies on Netflix for the top 20 countries:  
   <img src="TV_Show_and_Movies.png?raw=true"/> 
-  Visualize the correlation between 5 top countries and time:  
-   <Insert year_country_top5 image>
-   Visualize the distribution of movie ratings among the audience:
-   <Insert Movie_Rating image> 

### Content-based Recommendation System:  

