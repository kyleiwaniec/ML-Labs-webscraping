# ML-Labs-webscraping

## Approach:

__IMPORTANT__: We are not concerned with the correctness of the classification. We merely use it as an opportunity to demonstrate a use case for webscraping in the context of Machine Learning.
First we generate a dataset with labels, by scraping the web for both 'fake', and 'not_fake' news stories.    

1. Identify sevral sites to scrape using a list of websites flagged as 'fake' from Benedictine University.
https://researchguides.ben.edu/c.php?g=608230&p=4352564

* http://usanewstoday.com/
* http://www.thetruthseeker.co.uk/
* http://yesimright.com/

2. Scrape articles from the above websites. We will label these articles 'fake'.

3. Scrape a reputable news website which does not lean left or right. We will label these articles 'not_fake'.

* https://www.wsj.com/
* https://www.reuters.com/news/world

This combined dataset will give us the ability to build a simple model for the purposes of classification of articles as 'fake' or 'not_fake'. We can start with a Multinomial Naive Bayes. This is a simple bag-of-words model - its success is dependent on the assumption that 'fake' stories use different words than 'not_fake' stories. While NB is not particulary good at generating probabilities, it's been shown to be quite effective for classification. In other words, a probability of 0.9 is pretty far off a probability of 0.5, both result in the same clssification (assuming we split on 0.5).
