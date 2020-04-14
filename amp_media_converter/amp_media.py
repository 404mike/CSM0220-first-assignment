from amp_media_converter import AMP_Media_Converter_User_Interaction
from amp_media_converter import AMP_Media_Converter_File_Manager

class AMP_Media:
    ''' Text
    '''
    
    
    def get_dir_path(self,file_extensions):
        ''' Text
        '''

        user_interact = AMP_Media_Converter_User_Interaction()
        # get user input for directory
        path = user_interact.get_dir_path(file_extensions)
        # validate directory path
        valid_dir = self.validate_dir_path(path, file_extensions)

        if valid_dir:
            return self.check_fies_exist(path, file_extensions)
        else:
            print("{} doesn't exist, try again".format(path))
            self.get_dir_path(file_extensions)  
      
    def validate_dir_path(self, path, file_extensions):
        ''' Text
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        is_valid_dir = amp_dir.validate_path(path)

        if is_valid_dir:
            return True
        else:
            return False

    def check_fies_exist(self, path, file_extensions):
        amp_dir = AMP_Media_Converter_File_Manager()
        file_names = amp_dir.list_directory_media(path, file_extensions)
        if not in file_names:
            self.list_sub_dir()
        else:
            return file_names

    def list_sub_dir(self):
        amp_dir = AMP_Media_Converter_File_Manager()  
        user_interact = AMP_Media_Converter_User_Interaction()
        
        # get a list of sub directories
        sub_dir_list = amp_dir.list_directory_contents(path,file_extensions)

        # ask user to choose from the list of directories
        chosen_sub_dir = user_interact.get_user_sub_directory_choice(sub_dir_list)

        if(path.endswith('/')):
            new_path = path + chosen_sub_dir
        else:
            new_path = path + '/' + chosen_sub_dir

        # self.validate_dir_path(new_path, file_extensions)