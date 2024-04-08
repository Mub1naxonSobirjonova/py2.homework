class Applications():

    def __init__(self, google, youtube, telegram, instagram, message, gmail, clock, galareya):

        self.data = google
        self.video = youtube
        self.chats = telegram
        self.account = instagram
        self.conversation = message
        self.e_mail = gmail
        self.time = clock
        self.picture = galareya



    def get_google(self):
        return self.data
    
    def get_youtube(self):
        return self.video
    
    def get_telegram(self):
        return self.chats
    
    def get_instagram(self):
        return self.account
    
    def get_gmail(self):
        return self.e_mail
    
    def get_message(self):
        return self.conversation
    
    def get_clock(self):
        return self.time
    
    def get_galareya(self):
        return self.picture
    


    def set_google(self, new_google):
        self.data = new_google

    def set_youtube(self, new_youtube):
        self.video = new_youtube

    def set_telegram(self, new_telegram):
        self.chats = new_telegram
        
    def set_instagram(self, new_instagram):
        self.account = new_instagram
 
    def set_message(self, new_message):
        self.conversation = new_message

    def set_gmail(self, new_gmail):
        self.e_mail = new_gmail

    def set_clock(self, new_clock):
        self.time = new_clock
        
    def set_galareya(self, new_galareya):
        self.picture = new_galareya




    def info(self):
        allData = f"Information: {self.data} ,  Watch a movie: {self.video} ,  Modern communication: {self.chats} ,   Different possibilities:{self.account} ,  Offline conversation: {self.conversation},  Electron mail: {self.e_mail} ,  Exact time: {self.time} ,  Sealing events: {self.picture}"
        return allData

    
    
    






phone = Applications("online searches", "paid movies","online conversation","no information about it","ordinary conversation","not many people use it", "to know the time", "stories")

phone.set_google("GOOGLE")
phone.set_youtube("YOUTUBE")
phone.set_telegram("TELEGRAM")
phone.set_instagram("INSTAGRAM")
phone.set_message("MEGGAGE")
phone.set_gmail("GMAIL")
phone.set_clock("CLOCK")
phone.set_galareya("GALAREYA")

print(phone.info())



