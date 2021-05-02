from selenium import webdriver                     #Selenium-WebDriver makes direct calls to the browser using each browser’s native support for automation
from selenium.webdriver.common.keys import Keys    #this is import to pass the input and perform actions like deletion enter etc.
import time

class Twitter_Bot:
    def __init__(self, email,password):  #this will create email and password field
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()    #this is used open any link on firefox
    

    def login(self):                       #create login page
        bot = self.bot                     #this will call a  bot which will help to open link      
        bot.get('https://twitter.com/')    #here we will give a link to open 
        time.sleep(3)                       # it is used to wait for lil bit second 

        email = bot.find_element_by_class_name('email-input')                #after opening up og link bot will find email 
        password = bot.find_element_by_name('session[password]')             # and password field by their classes and attribute
        email.clear()                                                        #its is used to clear email
        password.clear()                                                     #and password field just fro security purpose 
        email.send_keys(self.email)                                          # this is used to put the email and password 
        password.send_keys(self.password)                                    # in email and password field
        password.send_keys(Keys.RETURN)                                      # this is used to hit rhe enter on login key automatically
        time.sleep(3)
     

    def like_tweet(self):                                                     #after login we have create like_tweet to like the tweet
        bot = self.bot                                                        # now again call  the bot
        bot.get('https://twitter.com/')                                       #it is used to open homepage where all tweet will get likes
        time.sleep(3)                                                          #then wait for 3 seconds
                                                       
        for i in range (1,10):                                                      #for loop is used so that scrolling time can be set                                              
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #this is used to scroll homepage 
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')                       #bot find tweets by their classes name
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]  #by looping from each tweets we will indentified 
                                                                                     #each tweet by their profilre link

            for link in links:                                                    #then we use for loop to iterate over the all links                                          
                bot.get('https://twitter.com/' + link)                            #after getting link one by one we all cocatenate to link so that
                                                                                  #we can access each profile tweet
                
                
                try:                                                              #this is use when tweet link accesed                                                            
                    bot.find_element_by_class_name('HeartAnimation').click()      #then this command will find perticular icon on which we have to perfom action using click() keyword
                    time.sleep(10)                                                #then wait for 10 seconds
                except Exception as ex:                                           #this is used when tweet no found then it will perform otherwise it will not performed
                    time.sleep(10)                                                ##then wait for 10 seconds         

obj1 = Twitter_Bot('emailid', 'password')
obj1.login()
obj1.like_tweet()