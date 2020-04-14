from amp_media_converter import AMP_Media_Converter_User_Interaction
from amp_media_converter import AMP_Media_Converter_File_Manager
import re

class AMP_Media:
    ''' Text
    '''
    
    def get_dir_path(self,file_extensions,path =''):
        ''' Text
        '''
        
        if not path:
            user_interact = AMP_Media_Converter_User_Interaction()
            # get user input for directory
            path = user_interact.get_dir_path(file_extensions)

        # validate directory path
        valid_dir = self.validate_dir_path(path)

        if valid_dir:
            return self.check_fies_exist(path,file_extensions)
        else:
            print("{} doesn't exist, try again".format(path))
            self.get_dir_path(file_extensions)  
        # return [True,foo]


    def validate_dir_path(self, path):
        ''' Text
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        is_valid_dir = amp_dir.validate_path(path)

        if is_valid_dir:
            return True
        else:
            return False

    def check_fies_exist(self, path, file_extensions):
        ''' Text
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        file_names = amp_dir.list_directory_media(path, file_extensions)
        
        # if list is not empty
        if file_names:
            return [True,path,file_names]
        else:
            return self.list_sub_dir(path,file_extensions)

    def list_sub_dir(self,path,file_extensions):
        ''' Text
        '''

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

        # return new_path
        return self.get_dir_path(file_extensions, new_path)

    def create_new_directory(self,path, dir_name):
        ''' Text
        '''

        amp_dir = AMP_Media_Converter_File_Manager()

        is_valid_dir = self.validate_dir_path(path + '/' + dir_name)

        if is_valid_dir:
            print("{} directory already exists, create a new directory".format(dir_name))
            
            while True:
                try:
                    new_dir_name = input ("Enter a new directory name ").strip()
                    if re.match(r'^[A-Za-z0-9_]+$', new_dir_name):
                        dir_name = new_dir_name
                        amp_dir.create_directory(path + '/' + new_dir_name)
                        return new_dir_name
                    else:
                        print("Not a valid directory name")
                except ValueError:
                    print ("Not a valid directory name")
        else:
            amp_dir.create_directory(path + '/' + dir_name)
            return dir_name