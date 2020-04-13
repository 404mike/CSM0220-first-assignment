from amp_media_converter import AMP_Media_Converter_File_Manager

class AMP_Media_Converter_User_Interaction:
    ''' Text
    '''

    def __init__(self):
        pass
    
    def get_dir_path(self, file_extensions):
        ''' Text
        '''

        path = input("Enter path to your Images directory: ")
        amp_dir = AMP_Media_Converter_File_Manager()
        is_valid_dir = amp_dir.validate_path(path)
        
        if is_valid_dir:
            files = amp_dir.list_directory_media(path, file_extensions)
            print(files)
        else:
            print("{} doesn't exist, try again".format(path))
            self.get_dir_path(file_extensions)

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