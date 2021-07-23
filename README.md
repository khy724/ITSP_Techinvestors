![Flask: 2.0.1](https://img.shields.io/badge/Flask-2.0.01-yellowgreen)

# ITSP_Techinvestors

#### Problem Statement

* This platform aims at making the investment / trading decision taking process simpler for unexperienced or initial stage investors
* Our platform uses machine learning for efficient forecasting of assets prices and compares the ROI on each type of asset and provides the top n maximum profitable options
* Generally the investor / trader has to surf through a lot of sites and Asset categories before investing which makes the money investing process even more hectic ,cumbersome and time wasting for the individual. We plan to provide them with various aspects of fields wherein they could get information about , invest and directly compare based on what suits them the best .
* A website like this would highly benefit the people who have very less knowledge about various investment schemes and prevent them from investing blindly.

#### Motivation

Our projects aims at simplifying the investment related issues that most people face in their day to day lives.
Generally the investor has to surf through a lot of sites before investing which makes the money investing process even more hectic ,cumbersome and time wasting for the individual. We plan to provide them with various aspects of fields (as mentioned above )wherein they could invest and directly compare based on what suits them the best.
A website like this would highly benefit the people who have very less knowledge about various investment schemes and prevent them from investing blindfoldedly.


#### Learnings

*In order to create the model profoundly we  started with basics of python , we did with the use of various video lectures and material provided by our mentor , further various assignments were solved and problem set were practiced from hacker rank to get hands on with it so that we could apply it in our project. 
*Further to implement the project we had to get good amount of knowledge regarding the financial aspect of the project , Hence learning about the asset allocation , risk return profile , about different sectors of investments ( stocks , FD’s , bonds , Mutual funds ) through various research materials and books was a great Learning as well 
*To generate the web page for our website we learnt CSS , HTML , JAVA SCRIPT,CHART.JS  to create the front end part of the website and also used JINJA2 syntax to combine front end with the back end .	
*In order to predict stocks for users using technical analysis, Machine learning had a major part to play , So with the help of Andrew NG’s course on coursera along with reading various blogs on Linear Regression, Logistic Regression, Decision Tree Classification ,Random Forest and Neural Networks and watching various you tube videos we created a stock prediction model . 
*For back end of our project we used FLASK and for Web Scrapping we used various python libraries .

#### Working

*The investor inputs the amount he wants to invest and other required details pertaining to the risk he can afford.
*The platform then displays the page corresponding to the risk profile selected.  
*The user can then navigate to pages for various investment categories like bonds,stocks,mutual funds and fixed deposits.
*Under the FDs and Bonds category, the investor inputs information such as their age group, term of investment etc. according to which the interest rate/ interest is shown.  
*Under stock, the website would predict and display results for short term and long term investments respectively and also top results based on dividends.
*Under Mutual funds, the website predicts and shows the user which company and type ( for example: equity or growth schemes, hybrid / monthly Income Plans, money market funds etc.)would reap maximum returns.
*After viewing these options the user can make an informed and smart choice as to where to invest. 

####Disclaimer

The given project is just a model and hence for prediction of top stocks we have used the already trained which is not being updated every time the website loads(as training stock prediction model takes time).
However, if implemented on a large scale we could make this work by training models using active learning which will take not more than 5 secs for each model. 
This way we will be training model at the end of the day after the market closes and then these models will be ready for the next day.

#### How to use?
* Make sure you are using python version >= 3.6 

* Clone the repository 


 ```bash
  git clone khy724/ITSP_Techinvestors
  ```
  
* Change the directory to ITSP_Techinvestors


 ```bash
  cd ITSP_Techinvestors
  ```
  
 * Install the dependecies 


 ```bash
  pip3 install requirements.txt
  ```
  
  * run the following line


 ```bash
  python3 website.py
  ```
