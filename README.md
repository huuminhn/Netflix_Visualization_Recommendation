## Netflix_Visualization_Recommendation
*A story-telling projects using visualization and a content-based recommendation system*   

---

### EDA and Visualization:  
- The dataset itself is quite clear, except for three columns with a noticeable amount of missing values, namely
['director', 'cast', 'country']. On the other hand, the column *'Rating'* and *'Date_added'* only have 7 and 10 NULL values respectively.   
--> Drop missing value for *'Date_added'* and *'Rating'*, and filling the NULL of *'country'* with its mode.  

- **Visualize the production of the top 20 countries:**  
 <img src="Country.png?raw=true"/>
 It can be seen that the majority of the Movies and TV shows are produced by America with nearly 3,500 products, following by 
 India, UK, Canada and France. The top 5 countries made approximately 75% of the overall movies and shows of the whole world. Thereby, 
 we will be focusing our further visualization on the top 5 countries.  
 
-  **Visualize the release date of TV shows and movies on Netflix for the top 20 countries:**  
   <img src="TV_Show_and_Movies.png?raw=true"/> 
 The graph indicates that most of the TV shows and Movies are being produced during the Winter, from October to January. Besides, in both of the cases,
 the production rate increase sharply after 2015, from under 10 movies a year to over 120 movies a year, and from 5 TV shows a year to more than 40 TV shows a year.  
 
-  **Visualize the correlation between 5 top countries and time:**  
   <img src="year_country_top_5.png?raw=true"/>  
  Observing the TV shows and Movies production rate from the chart, it can be seen that America takes the lead in number of shows produced in any time. Similar to the above graph, the production rate increased sharply after 2015, especially for the United States. This can be a result of the blooming technology in film making, such as CGI, 3D Printing, Deep Cencor, etc.. Other countries also experience a noticeable increase in their production rate, but not as significant as America. Personally, I believe that due to the cutting edge technology of the film studios, they were capable of release extraodinary movies that attract the majoriy of audience, hence making other countries able to increase their movies production rate to serve such market demand.  
  
-   **Visualize the distribution of movie ratings among the audience:**
  <img src="Movie_Rating.png?raw=true"/> 
  Undoubtedly, the three most popular movie ratings were TV-MA, TV-14 and R. Those types of movies can take advantage of the advanced 3D technology in many genres, 
 such as Sci-Fi, Action, Fantasy, etc.. Moreover, due to the market demand, more and more movies and TV shows were created using CGI in newly adopted genres, namely Space Travel, Time Travel, Cerebral Science, Robot and Monster Films, Disaster and Alien Invasion. Those Movies with fancy animation and visuals effects are mostly served the teenagers or young aldult, hence making those to be categorized as TV-MA, TV-14 and R.  
 
 ***In conclusion, by exploring the data and visualizations, it can be seen that there are 5 countries that producuded the majority of TV shows and Movies, and 
 the Movie Industry bloomed after 2015 as a result of the advanced technology of the film studios.***

---

### Content-based Recommendation System:  

For the recommendation system, I used Content-based approach as it would be helpful in determining correlation between movies. In order to test the recommendation system, I will use one of my most favourite movie as an example, "3 idiots":  
<img src="3_idiots.png?raw=true"/>   
As a result, the recommended movies are all from Bollywood, and some of them have the same main actor as the one in "3 idiots", Aamir Khan. Seemingly the recommendation system works well on the scale of similarity between the movies based on actors, genres and country origins.  

P/S: "3 idiots" is a greate movie, I highly recommended it. But please prepare some napkins before watching, as it will leave you in tears =) 
