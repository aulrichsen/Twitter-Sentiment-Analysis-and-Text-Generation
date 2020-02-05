import tkinter as tk
from tweepy_API import Tweets
import os

HEIGHT = 100
WIDTH = 300

class GUI():
    
    def __init__(self, root):
        self.tweets = Tweets()
        
        self.root = root
        self.root.configure(background='DeepSkyBlue3')
        
        self.canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        
        #Title Label
        self.titleLabel = tk.Label(self.root, text="Twitter Sentiment Analysis & Text Generation", font=("Helvetica", 20), fg="white")
        self.titleLabel.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0)
        self.titleLabel.configure(background='DeepSkyBlue3')
        
        #Twitter Logo Label
        filePath = os.path.join("TwitterIcon.png")
        
        print(filePath)
        logo = tk.PhotoImage(file=filePath)
        self.logoLabel = tk.Label(self.root, image=logo)  
        self.logoLabel.image = logo
        self.logoLabel.place(relwidth=0.2, relheight=0.2, relx=0.8, rely=0)
        #self.logoLabel.configure(image=logo)
        
        #Keyword search
        self.searchText = tk.Entry(self.root)
        self.searchText.place(relwidth=0.3, relheight=0.1, relx=0.2, rely=0.2)
        self.searchText.insert(0, "Keyword")
        
        #User search
        self.searchUser= tk.Entry(self.root)
        self.searchUser.place(relwidth=0.3, relheight=0.1, relx=0.5, rely=0.2)
        self.searchUser.insert(0, "realDonaldTrump")
        
        #Search button
        self.searchButton = tk.Button(self.root, text='Search', command=lambda:self.updateTweet())
        self.searchButton.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.3)
        
        #Tweet Text Box
        self.tweetLabel = tk.Label(self.root, text="Tweet")
        self.tweetLabel.place(relwidth=0.4, relheight=0.1, relx=0.2, rely=0.6)
        self.tweet = tk.Label(self.root, text=self.tweets.tweet, wraplength=500)
        self.tweet.place(relwidth=0.4, relheight=0.2, relx=0.2, rely=0.7)
        
        #Sentiment Box
        self.sentimentLabel = tk.Label(self.root, text="Sentiment")
        self.sentimentLabel.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.6)
        self.sentimentVal = tk.Label(self.root, text=self.tweets.sentiment)
        self.sentimentVal.place(relwidth=0.2, relheight=0.2, relx=0.6, rely=0.7)
        
        
    def updateTweet(self):
        self.tweets.newTweet(self.searchText.get(), self.searchUser.get())
        self.tweet['text'] = self.tweets.tweet
        self.sentimentVal['text'] = self.tweets.sentiment

root = tk.Tk()

GUI = GUI(root)

root.mainloop()