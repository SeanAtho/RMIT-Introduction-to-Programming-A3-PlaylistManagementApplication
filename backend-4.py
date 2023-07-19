class BackEnd:

    def __init__(self,playlist_filename: str):
        """__init__ method is responsible for intialising data from
        application, frontend and backend modules."""

        #The section below stores all songs that have been added throughout the program, with it also opening
        #the data.csv file from the folder the program is running from (if there is a data.csv file). While loop
        #will load the file along with it importing all playlist information from the file, in the event, there
        #isn’t a file to open it will not open a file but create one with the desired name passed through method. 
        #
        #Below list stores all the songs and is as a result referred to as ‘songs’, alternative names would
        #be ‘playlist’ or ‘song_items’. 
        self.__songs=[]
        #Assigns the parameter retried in method to variable ‘playlist_filename’ for later use. 
        self.__playlist_filename=playlist_filename
        fp=None
        try:
            fp=open(self.__playlist_filename)
        except:
            self.save_to_file()
        #Below code could alternatively be placed inside the try code block, but this would thus result in the try-except
        #being overly long which in the case of the requirements is not preferred. 
        if(fp!=None):
            
            #Below variables reads the line from the that is specified from a user. Alternative names would be ‘line_read’
            #however in the case of this variable one looking at the code directly will likely be able to determine its
            #purpose based on the readline following the creation of the variable.
            line=fp.readline()
            line=fp.readline()

            #A while loop is used to continually read all lines within the file until non are left, the use of operators and
            #for loops would make the loop only repeat once and a ‘==’ operator would result in an indefinite loop.
            while(line!=""):

                #Variable is created and used to split the items from the previous ‘line’ variable into fields. Alternative
                #names are not preferred as the variables current purpose is rather straightforward and isn’t dependent on
                #the type of data within the file. 
                fields=line.strip().split(",")
                self.add_song(fields[0],fields[1],fields[2])
                line=fp.readline()
            fp.close()
            
    #An accessor is created so the variable isn’t able to be altered.  
    @property
    def songs(self):
        return self.__songs
    
    #An accessor is created so the variable isn’t able to be altered.  
    @property
    def playlist_filename(self) -> str:
        return self.__playlist_filename
    
    #The method is created and used to calculate the number of songs that are stored within the song list.
    #Alternative names could be ‘song_count’ or ‘song_number’, these names were not used due to the fact
    #they are better suited for the naming schemes of variables, not method/functions. 
    def get_song_count(self):
        """Method is used to collect length values of the songs list"""
        
        return len(self.__songs)
    
    #Below code block and method are created and used to check for invalid inputs given by the user when
    #prompted to provide a year for their previously entered song, parameters are passed from the frontend
    #module which contains the unchecked version of the input upon completion of the try-except the variable
    #is returned from the method, in the event input is invalid a Type error is raised displaying details of
    #the error to the user. 
    def check_year(self,unchecked_year:str) -> int:
        try:
            self.__year=int(unchecked_year)
        except:
            raise TypeError("Year must be a valid integer")
        return self.__year

    #Code block and method gathers the information inputted by the user and appends it to the data contained
    #within the songs list. 
    def add_song(self,song: str,album: str,year: str):
        """Method allows user to add songs to song list"""
        
        self.__songs.append(Song(song,album,year))
    
    def save_to_file(self):
        """Method is used to save songs to CSV file"""
        
        #Below code block opens a file named data.csv and will write the information that has been inputted
        #by the user if any. Upon the completion of such the file will be closed. 
        fp=open(self.__playlist_filename,"w")
        fp.write("Song, Album, Year\n")
        fp.write(self.__str__())
        fp.close()

    def __str__(self) -> str:
        """Method is used to collect all strings that
        are inputted throughout the program."""
        
        len_songs= self.get_song_count()
        #Variable will store a summary of all the information and is as a result named as such. The value given
        #to the variable is an empty string since each time the program in question is run the summary will need
        #to start with nothing stored and will adapt/change depending on the operations completed and carried out
        #by the user. 
        summary=""
        i=0
        #While loop will repeat for items contained within the songs list. Alternatively, a for loop containing the
        #in operator could be used resulting in the same result, however, the current requirements prevent implementation of such. 
        while(i<len_songs):
            summary+=self.__songs[i].__str__() + "\n"
            i+=1
        return summary
    
class Song:
    """Class contains all details required for songs list."""
    
    def __init__(self,song,album,year):
        """Method initialises above class to program."""
        
        #naming schemes remain the same between both modules.
        self.__song=song
        self.__album=album
        self.__year=year
     
    #An accessor is created so the variable isn’t able to be altered.  
    @property
    def song(self)-> str:
        return self.__song
    #An accessor is created so the variable isn’t able to be altered.  
    @property
    def album(self)-> str:
        return self.__album
    #An accessor is created so the variable isn’t able to be altered.  
    @property
    def year(self) -> str:
        return self.__year

    def __str__(self) -> str:
        """Method is used to collect all strings that
        are inputted throughout the program."""
    
        summary=self.__song+","
        summary+=self.__album+","
        summary+=str(self.__year)
        return summary 
        
        
