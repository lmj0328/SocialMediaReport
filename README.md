# SocialMediaReport

Here is the link to our [Landing Page](https://lmj0328.github.io/SocialMediaReport/)

Here is the link to our [Demonstration](https://www.youtube.com/watch?v=0ESgZxsGHd8)

According to our research, people are spending an increasing amount of hours daily on a wide range of social media [1, 2]. As people post interesting facts about themselves and view contents about others, their self-presentation and identity are gradually changed by the affordances without their noticing [3, 4]. This lack of self-awareness is detrimental to people as it not only causes anxiety and confusion but also triggers mental health problems. However, the problem has not been addressed or even paid attention to, but worsened by the contradiction between business expansion and peer pressure. As a result, a considerable number of people have  inaccurate self-cognition and neglect self-reflection. 

We would like to mainly focus on people’s confusion and interest about their online identity. We want to help them regain accurate self-cognition and evaluate the difference or misunderstanding between the actual impression and the identification they believed about themselves on their social media platforms by conducting data analysis and data visualization.

## Closeout/handoff plan
* Step 1: Notify interviewers and survey respondents that our project is being transitioned to open source; with a date that the transition will be effective.
* Step 2: Post a notice on our landing page about the project being transitioned to open source; with a date that the transition will be effective.
* Step 3: Notify any users we collected data from that their data will be deleted; with a date the data deletion will be completed by. Delete all collected data.
* Step 4: Convert the code repository to a public repository.
* Step 5: Add a README document in the public repository with instructions on how to build, continue working on the project.

## Technical Documentation
We used the micro web framework Flask which was written in Python to build up our backend server. It supported us to build the connection between our client-side development and server-side development by allowing sending data back and forth. To keep the consistency of our Python backend, we planned to scrape users’ social media posts from different platforms by using third-party python APIs or write scrapper code by ourselves in python language. We used the python library called [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) to scrape all twitter data and wrote instagram scraping process on our own. While there is no need to construct a real-time database to support the functionality of our product, we saved the data each time into variables and passed them into the data wrangling code. We used pandas library in Python to process the data and summarize the results which would be shown on the final report. In terms of frontend implementation, we used jquery in Javascript to receive data from our backend and generate the interactive report. Last but not the least, we drew data visualization by using libraries [Chart.js](https://www.chartjs.org/) and [AnyChart](https://www.anychart.com/).

## Inital Set-up Guideline
This tutorial will guide you to do the initial set-up on your own computer enabling this project runs on your local machine. Once you have doen this tutorial, you are free to explore this project and see what impact you can bring to this project. This tutorial is applicable for Mac machine for current stage, we will add the guideline for Windows and Linux in the future.

### 1. Clone the repo

-------
##### a) Click the green 'Clone' button on the top-right of this github page
<img src="img_read/clone_button.png" width="300">

##### b) Copy the git address using the button besides the link
<img src="img_read/clone_link.png" width="300">

##### c) Open the Terminal on your machine


##### d) Use cd ... to direct to the folder you want to place this project in 
```bash
$ cd Desktop/
```

##### e) Then, you can clone this project on your local machine by using the link you copied previously
```bash
$ git clone https://github.com/lmj0328/SocialMediaReport.git
```

*Now, you successfully store the project on your local machine!!*

### 2. Install python3 on your machine

-------
##### a) First, you can check if you have python 3 on your machine by running flowing code on Terminal. If yes, you can skip this part
```bash
$ python --version
```

##### b) If you do not have python installed on your machine, don't worry! I recommend you to install Aconda enviroment on your local machine with python 3 in it. With Aconda, you can install and access the popular packages in python more easily. Fllow the instructions [here](https://docs.continuum.io/anaconda/install/). 

### 3. Install required packages in this project

-------
##### a) First, let's install the getoldtweet3 package in python which can help us to scrape the data on Twitter
```bash
$ pip install GetOldTweets3
```

##### b) Then, let's install the flask package which help us to host our website locally on the machine and have interaction with it

```bash
$ pip install Flask
```
*Now, you have all the required packages in your machine to run this project!*

### 4. Run the project

-------
##### a) Open the terminal, let's go to the root of our cloned folder
```bash
$ cd Desktop/SocialMediaReport/
```
##### b) Then, we use cd.. agian to go to the folder which stores our python code
```bash
$ cd flask_jquery/
```
##### c) Now we can start to run the project by inputting code below
```bash
$ python app.py
```

##### d) This is what will look like after you run the code above, copy the address showing below and paste it in your browser, you can start to play with our project!
<img src="img_read/run.png" width="700">


## Reference

[1] Demographics of Social Media Users and Adoption in the United States. (n.d.). Retrieved from https://www.pewresearch.org/internet/fact-sheet/social-media/

[2] The rise of social media. (n.d.). Retrieved from https://ourworldindata.org/rise-of-social-media

[3] DeVito, M. A., DeVito, M. A., Birnholtz, J., Hancock, J. T., Northwestern University, Northwestern University, … IBM T.J. Watson Research Center. (2017, February 1). Platforms, People, and Perception: Using Affordances to Understand Self-Presentation on Social Media. Retrieved from https://dl.acm.org/doi/abs/10.1145/2998181.2998192

[4] Social Media as a Source of Self Identity Formation ... (n.d.). Retrieved from http://scholar.sun.ac.za/bitstream/handle/10019.1/97862/ogidi_social_2015.pdf?sequence=1






