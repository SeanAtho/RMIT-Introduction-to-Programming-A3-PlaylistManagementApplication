import sys

class FrontEnd:
    """Class contains all code that will display to the user
    in running said program."""
    
    #The below method has been created to prevent users from giving empty string inputs, this is used in all
    #sections of the program where a string input is has been taken from the user. The reason for making the
    #below method for handling this operation is to prevent unneeded code repetition as there are dozens of
    #inputs that are taken throughout the program as a whole.
    #Alternative names would be ‘obtain_str’ and ‘str_input’, but given the fact the below is a method, not
    #a variable etc, the current name is left as the clearest indicator of its use and purpose in the program. 
    def get_str(prompt:str) -> str:
        """Method takes input from user and stores it as a string."""
        sys.stdout.write(prompt)
        
        #The below variable takes the input from the user via the readline strip statement.
        #Alternative names would be ‘str’ or 'input' however as the program at one point takes a non-string input
        #further clarification has been required to avoid confusion. 
        inputted_str=sys.stdin.readline().strip()
        
        #The while loop below is created and used to check for empty inputs with the write statement also used to
        #indicate as such directly to the user in the event they have provided an empty input.
        #The while loop below is created and used to check for empty inputs with the write statement also used to
        #indicate as such directly to the user in the event they have provided an empty input. This operation is
        #somewhat possible to do through an alternative like an if statement, however, this will require more code
        #than is needed and is generally not the best choice for a repeating operation such as below. 
        while(inputted_str==""):
            sys.stdout.write("Input Error! Cannot be empty: ")
            inputted_str=sys.stdin.readline().strip()  
        return inputted_str

    def __init__(self,backend: str):
        """Inititialses all code relevant to taking inputs and display them."""

        #The code block below will take the parameter passed from the application.py file containing information
        #about the backend file with it subsequently being assigned to a variable. Alternative names for a variable
        #that is assigned to parameter backend would be ‘backend_file’, however, given that in this case, the program
        #will only be using one backend file the current name is unlikely to cause confusion. 
        self.backend=backend
        sys.stdout.write(str(self.backend.get_song_count())+" playlist items loaded...\n")
        sys.stdout.write("Starting Music Playlist Program...\n")

        #The below code and strings variable concatenation is created and used to repeatably be outputted to the user
        #upon programs launch and condition/statement completion. Regarding the structure, they can be in any order.
        #Alternative names for string variable concatenation would be ‘menu’ or ‘main_display’, however, arguably the
        #first is not the only menu that is outputted to the user thus causing confusion upon code inspection and the
        #second would be better suited for a method or function name. 
        main_menu=""
        main_menu+="=================================\n"
        main_menu+="Music Playlist Management Program\n"
        main_menu+="=================================\n"
        main_menu+="[A]dd Song items\n"
        main_menu+="[D]isplay Songs\n"
        main_menu+="[S]ave Current Playlist\n"
        main_menu+="E[x]it\n"
        main_menu+="Menu Selection: "
        
        #The below variable calls the get_str method along with outputting the ‘main_menu’ in the current module which
        #as previously explained will take the input provided by the user and convert it into a string. Alternative names
        #for variable would be ‘option’, ‘menu_choice’ and ‘selection’, but given that the outputted strings contained with
        #the ‘main_menu’ string variable are the options it makes sense to refer to the user's response to them as the ‘menu_option’.
        menu_option = FrontEnd.get_str(main_menu).lower()
        sys.stdout.write("\n")
        
        #While loop is used to allow the user to exit the program when needed. String option of ‘x’ has been chosen based
        #on the letter enclosed within the square brackets of the ‘main_menu’ string variable and will subsequently prevent
        #a user from exiting unintentionally as ‘x’ is rarely used or intentionally inputted 
        while(menu_option!="x"):
            
            #**Justification below refers to if statements pertaining to menu operations for the frontend module.
            #
            #The below if statement is used to determine which of the menu operations was selected and needs to be carried out,
            #this is based on the user's stored input after the provide one after the main menu is displayed. As more than one
            #input is used additional elifs have also been created for the frontends operations. In the event of an invalid
            #input that doesn’t meet any of the conditions, an else will display an error message indicating to the user that their input is invalid. 
            if(menu_option=="a"):
                sys.stdout.write("Add song...\n")

                #Below variables call to the ‘get_str’ method which returns values inputted from the user which are then assigned to the variable in
                #question. Each of the variables names have been chosen based on the information it will store. Alternative names for variables are in
                #order, the variable song could alternatively be named ‘song_title’, the variable album could alternatively be named ‘record’, the last
                #variable ‘year’ is justified separately below. 
                song=FrontEnd.get_str("Enter song name: ")
                album=FrontEnd.get_str("Enter album name for "+song+": ")

                #Below code block is used to check for invalid inputs when for the year variable, initially the user's input is given to a separate variable
                #‘unchecked_year’ where it is passed to the method in the backend, upon the method's completion the value is returned and then finally assigned
                #to the ‘year’ variable.
                #
                #Below code block is used to check for invalid inputs when for the year variable, initially the user's input is given to a separate variable
                #‘unchecked_year’ where it is passed to the method in the backend, upon the method's completion the value is returned and then finally assigned
                #to the ‘year’ variable. A try-except is created to raise an exception when the input returned isn’t an integer. 
                year=None
                while(year==None):
                    try:
                        sys.stdout.write("Enter Year for "+song+": ")
                        unchecked_year=sys.stdin.readline().strip()
                        year=self.backend.check_year(unchecked_year)
                    except Exception as e:
                        sys.stdout.write(str(e)+"...")
                self.backend.add_song(song,album,year)
                sys.stdout.write("Song Item has been added...\n")
                        
            #**Refer to Justification for if, elif, and else statements on line 71
            elif(menu_option=="d"):
                
                #Below code block is used to output to the user all items contained within the CSV as well as any they have recently added but not saved to the CSV. A variable
                #named ‘song_summary’ calls to the method through the backend parameter which subsequently returns a formatted string containing all information pertaining
                #to the recently added and imported playlist items. 
                sys.stdout.write("Display all songs...\n")
                
                #The variable name will is responsible for calling to and retrieving the returned values of the method within the backend module, this is then outputted below
                #the variable through a sys write function. Alternative names would be ‘summary’ and ‘playlist’, however, as throughout this module and the backend, there are
                #references to variables of similar names the current one has been selected to avoid confusion. 
                song_summary = self.backend.__str__()
                sys.stdout.write(song_summary)
                
            #**Refer to Justification for if, elif, and else statements on line 71
            elif(menu_option=="s"):
                sys.stdout.write("Saving songs to .csv file\n")
                #Runs the backend modules method to save all information to CSV file.
                self.backend.save_to_file()
                sys.stdout.write("Success in saving songs!\n")
               
            else:
                sys.stdout.write("Error! Invalid menu selection\n")

            menu_option=FrontEnd.get_str(main_menu).lower()

        sys.stdout.write("Ending Program\n")

