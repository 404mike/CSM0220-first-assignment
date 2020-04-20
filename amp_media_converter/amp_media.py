#!/usr/bin/env python
"""
This class is an interface to the AmpMediaConverterUserInteraction
and AmpMediaConverterFileManager classes
"""
import os
from amp_media_converter import AmpMediaConverterUserInteraction
from amp_media_converter import AmpMediaConverterFileManager

class AmpMedia:
    ''' Class Interface for Media Converter classes

        This class is intended to be an interfce to the
        AmpMediaConverterUserInteraction and
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

    def __init__(self):
        self.amp_interact = AmpMediaConverterUserInteraction()
        self.amp_dir = AmpMediaConverterFileManager()

    def get_dir_path(self, file_extensions, path=''):
        '''
            Method to prompt a user for a directory path

            This method will call the get_dir_path in
            the AmpMediaConverterUserInteraction class
            which will prompt a user for a directory path
            and validate the input.
            It will then call validate_dir_path to check
            if the path submitted exists on disk.

            If the path is valid, it will call the
            check_fies_exist to check if there are
            files in that directory

            Args:
                path (string) - path to directory

            Returns:
                list
        '''

        # check if no path has been given
        if not path:
            # get user input for directory
            path = self.amp_interact.get_dir_path()

        # validate directory path
        valid_dir = self.validate_dir_path(path)

        if valid_dir:
            return self.check_files_exist(path, file_extensions)
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

        is_valid_dir = self.amp_dir.validate_path(path)

        if is_valid_dir:
            return True

        return False

    def check_files_exist(self, path, file_extensions):
        '''
            Method to check if there are files with the
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

        file_names = self.amp_dir.list_directory_media(path, file_extensions)

        # if list is not empty
        if file_names:
            return [True, path, file_names]

        return self.list_sub_dir(path, file_extensions)

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

        # get a list of sub directories
        sub_dir_list = self.amp_dir.list_sub_directory_contents(path)

        # ask user to choose from the list of directories
        chosen_sub_dir = self.amp_interact.get_user_sub_directory_choice(sub_dir_list)

        # if the user chooses to start again
        if chosen_sub_dir == '*** Search Again ***':
            return self.get_dir_path(file_extensions, '')

        # format the path with a slash
        if path.endswith('/'):
            new_path = os.path.join(path, chosen_sub_dir)
        else:
            new_path = os.path.join(path, chosen_sub_dir)

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
            from the AmpMediaConverterUserInteraction class.
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

        # check if directory already exists
        is_valid_dir = self.validate_dir_path(os.path.join(path, dir_name))

        # if it does - prompt the user to choose a new directory name
        if is_valid_dir:
            print("{} directory already exists, create a new directory".format(dir_name))

            # get user input
            new_dir_name = self.amp_interact.get_new_directory_name()

            # create new directory
            self.amp_dir.create_directory(os.path.join(path, new_dir_name))
            return new_dir_name

        # create new directory
        self.amp_dir.create_directory(os.path.join(path, dir_name))
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

            Returns:
                boolean
        '''

        return self.amp_dir.create_directory(os.path.join(path, dir_name))


    def move_file(self, path, destination):
        ''' Method to move a file

            The method accepts two parameters
            the current location of the file
            and the destination of where you
            want to move the file to?

            This method calls move_file from
            the AMP_Media_Converter_File_Manager class

            Args:
                path - path of the file
                desination - the location where the file is to be moved to

            Returns:
                boolean
        '''

        return self.amp_dir.move_file(path, destination)

    def delete_file(self, path):
        '''Method to delete a file

            This method accepts one parameter,
            the path to the file you want to delete.

            Args:
                path - path to file

            Returns:
                boolean
        '''

        return self.amp_dir.delete_file(path)
