import re

class AMP_Media_Converter_User_Interaction:
    ''' Text
    '''

    def get_dir_path(self, file_extensions):
        ''' Text
        '''

        path = input("Enter path to your Images directory: ")
        return path


    def get_user_sub_directory_choice(self, sub_dir_list):
        ''' Text
        '''

        while True:
            try:
                option =  int (input("Choose a number to search or 0 to choose a new directory: "))
                
                try:
                    gotdata = sub_dir_list[option]
                    return gotdata
                except IndexError:
                    print("Not a valid number, choose a number from the list")
                    self.get_user_sub_directory_choice(sub_dir_list)
                break
            except ValueError:
                print ("Not a number, try again")  

    def get_new_directory_name(self):
        while True:
            try:
                new_dir_name = input ("Enter a new directory name ").strip()
                if re.match(r'^[A-Za-z0-9_]+$', new_dir_name):
                    return new_dir_name
                else:
                    print("Not a valid directory name")
            except ValueError:
                print ("Not a valid directory name")