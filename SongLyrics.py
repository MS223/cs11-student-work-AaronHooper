class Song(object):

    def __init__(self, lyrics, title):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        print self.title
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "These lyrics are copywrighted",
                   "So I'll stop here"],"happy birthday song")

# hotline_bling = Song(["You used to call me on my",
#                       "You used to, you used to",
#                       "Yeah",])
# This is your daily reminder that Drake is Canadian

happy_bday.sing_me_a_song()
#hotline_bling.sing_me_a_song()


class Song(object):

    def __init__(self, lyrics, title):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        print self.title
        for line in self.lyrics:
            print line

still_here = Song(["You not from the city,I could tell, I could tell dog"
                   " Did it, did it,did it by myself,by myself dog"
                   "Blew up and im in the city still, I'm in the city still, I'm still here dog"],"still here")

# hotline_bling = Song(["You used to call me on my",
#                       "You used to, you used to",
#                       "Yeah",])
# This is your daily reminder that Drake is Canadian

still_here.sing_me_a_song()
#hotline_bling.sing_me_a_song()
