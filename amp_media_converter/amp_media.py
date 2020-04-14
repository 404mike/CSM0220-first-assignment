from amp_media_converter import AMP_Media_Converter_User_Interaction
from amp_media_converter import AMP_Media_Converter_File_Manager
import re

class AMP_Media:
    ''' Class Interface for Media Converter classes

        This class is intended to be an interfce to the 
        AMP_Media_Converter_User_Interaction and 
        AMP_Media_Converter_File_Manager classes
        and should be imported by classes such as
        Image converter and Docuemnt converters which 
        can use the following methods:

        get_dir_path
        validate_dir_path
        check_fies_exist
        list_sub_dir
        create_processed_items_directory
        create_new_diretory

    '''
    
    def get_dir_path(self,file_extensions, path =''):
        ''' Method to prompt a user for a directory path

            This method will call the get_dir_path in 
            the AMP_Media_Converter_User_Interaction class
            which will prompt a user for a directory path
            and validate the input.
            It will then call validate_dir_path to check
            if the path submitted exists on disk.
            
            If the path is valid, it will call the
            check_fies_exist to check if there are 
            files in that directory

            Args:
                path (string) - path to directory
        '''
        
        # check if no path has been given
        if not path:
            user_interact = AMP_Media_Converter_User_Interaction()
            # get user input for directory
            path = user_interact.get_dir_path(file_extensions)

        # validate directory path
        valid_dir = self.validate_dir_path(path)

        if valid_dir:
            return self.check_files_exist(path,file_extensions)
        else:
            print("{} doesn't exist, try again".format(path))
            self.get_dir_path(file_extensions)  

    def validate_dir_path(self, path):
        ''' Method to validate if the directory path
            given exists on disk

            This method will use the validate_path
            from the AMP_Media_Converter_File_Manager class
            to check if the directory path is valid

            Args:
                path (string) - directory path
            
            Returns:
                boolean
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        is_valid_dir = amp_dir.validate_path(path)

        if is_valid_dir:
            return True
        else:
            return False

    def check_files_exist(self, path, file_extensions):
        ''' Method to check if there are files with the 
            file extentension in the directory path

            The method will use the list_directory_media
            from the AMP_Media_Converter_File_Manager class,
            the list_directory_media method will search for 
            files matching the file extensions in the directory
            path.

            if the response from list_directory_media, assigned to
            the file_names variable, is empty (ie no files found)
            call the list_sub_dir method which will return any sub directories
            to one level for the directory, this will prompt the
            user to chose one of these directories, which will start the 
            search for files again.
            However, if files are found we can return a list back to the 
            calling method.           

            Args:
                path (string) - directory path
                file_extensions (list) - a list of file extensions to search ['jpg','png']

            Returns:
                list - [boolean, list of file names]
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        file_names = amp_dir.list_directory_media(path, file_extensions)
        
        # if list is not empty
        if file_names:
            return [True,path,file_names]
        else:
            return self.list_sub_dir(path,file_extensions)

    def list_sub_dir(self, path, file_extensions):
        ''' Method to list sub directories in a given directory

            This method is called if no files are found
            in check_fies_exist method.

            A list of directries in the path directory
            if there are any, which is called from the
            sub_dir_list method from the 
            AMP_Media_Converter_File_Manager class.

            The user is then prompted to choose one of the
            sub directories or to start over from the start.

            Once a sub directory has been chosen, a new
            path is created and we call the get_dir_path
            method, to begin the process again.

            Args:
                path (string) - directory path

        '''

        amp_dir = AMP_Media_Converter_File_Manager()  
        user_interact = AMP_Media_Converter_User_Interaction()
        
        # get a list of sub directories
        sub_dir_list = amp_dir.list_sub_directory_contents(path)

        # ask user to choose from the list of directories
        chosen_sub_dir = user_interact.get_user_sub_directory_choice(sub_dir_list)

        # format the path with a slash
        if(path.endswith('/')):
            new_path = path + chosen_sub_dir
        else:
            new_path = path + '/' + chosen_sub_dir

        # return new_path
        return self.get_dir_path(file_extensions, new_path)

    def create_processed_items_directory(self, path, dir_name):
        ''' Method to create a processed item directory
            for the processed items - such as thumbnails.

            The method uses the create_directory method from 
            the AMP_Media_Converter_File_Manager class
            to create new directories.

            This method will first check to see if the directory
            we're trying to create already exists?

            If the directory does already exist, prompt the
            user to enter a new name for the directory, this 
            is done through the get_new_directory_name method 
            from the AMP_Media_Converter_User_Interaction class.
            Once a new name has been chosen, create the directory
            from the create_directory method from the
            AMP_Media_Converter_File_Manager class.

            If there isn't a directory with the directory name,
            create the directory from the create_directory method 
            from the AMP_Media_Converter_File_Manager class.

            Args:
                path (string) - directory path
                dir_name (string) - name of the new directory

            Returns:
                string - new processed items directory name
        '''

        amp_dir = AMP_Media_Converter_File_Manager()

        # check if directory already exists
        is_valid_dir = self.validate_dir_path(path + '/' + dir_name)

        # if it does - prompt the user to choose a new directory name
        if is_valid_dir:
            print("{} directory already exists, create a new directory".format(dir_name))
            
            # get user input
            user_interact = AMP_Media_Converter_User_Interaction()
            new_dir_name = user_interact.get_new_directory_name()
            # create new directory
            amp_dir.create_directory(path + '/' + new_dir_name)
            return new_dir_name
        else:
            # create new directory
            amp_dir.create_directory(path + '/' + dir_name)
            return dir_name

    def create_new_diretory(self, path, dir_name):
        ''' Method to create a processed item directory
            for the processed items - such as thumbnails.

            This method is intended to be used programatically.

            The new directory is created from the create_directory 
            method from the AMP_Media_Converter_File_Manager class.

            Args:
                path (string) - directory path
                dir_name (string) - name of the new directory

        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        amp_dir.create_directory(path + '/' + dir_name)
