# Resale Ticket Pricing by Music Genres

A statistical analysis and model of ticket resale prices using concert features and musical features. The ticket resale market in the US is estimated to be a 5 billion dollar market. Given the size of the industry, it's important to understand how to sell tickets in a fashion that will find you a buyer but also not to leave money off the table. Therefore, I'm interested in the different factors that relate to the average resale price of concert tickets. 

## Project Goal
Predict average ticket resale prices with features covering the concert, itself, and musical features of the artist.

## Dataset and Methods

Used the SeatGeek API to retrieve information on ticket resales and the Spotify API to retrieve information on musical features of artists playing concerts.  

Tools: Python, Numpy, Pandas, Matplotlib, Scipy, Seaborn, Multiprocessing, Spotipy, Jupyter Notebook

## Results and Insight

### Does the time before the concert affect resale ticket prices?


### Does music genre affect resale ticket prices?

![Boxplot comparing Average Ticket Resale Price between Concert Residencies and Touring Concerts](images/ConcertResidency_AvgTickPrice.png)

There is a significant difference in the average ticket resale price between concerts of different genres (Kruskal-Wallis Test: H = 318.94; p-value = 6.41e-59). Punk concerts have the lowest resale price (mean: 60.0); while Pop, Country, Blues, and Latin concerts have high resale prices. 

### How do tickets for concert residencies compare to concerts on tour?

When I was looking at individual artists (ie. Dionne Warwick, The Lumineers, etc), I noticed that there was not much variation in average ticket price over time for artists that performed at the same venue multiple times and those that toured. Therefore, I wanted to look at the difference in average ticket resale price between the two groups. 

![Boxplot comparing Average Ticket Resale Price between Music Genres](images/MusicGenre_AvgTickPrice.png)

Residency concerts have higher average resale price than touring concerts (Mann-whitney-u (statistic=18467363.0, pvalue=1.84e-156)

### Predicting Ticket Prices

## Conclusions

## References
https://www.cnbc.com/2015/03/04/online-ticket-resellers-the-surreptitious-rise-of-the-online-scalper.html
