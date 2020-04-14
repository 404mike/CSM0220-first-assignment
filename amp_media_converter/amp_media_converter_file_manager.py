import os
import os.path

class AMP_Media_Converter_File_Manager:
    ''' Class to manage files and directories for the AMP_Media package
    '''

    def validate_path(self, path):
        ''' Method to validate directory path

            The method will look to see if the directory
            specified in the path parameter is on disk

            Args:
                path (string) - directory path 

            Returns:
                boolean
        '''

        is_valid_dir = os.path.isdir(path)  
        return is_valid_dir

    def list_directory_media(self, path, file_extensions):
        ''' Method to list any files in a directory

            This method will return all the files in the path
            directory that contain the specified file extensions
            e.g. search for jpg files in /var/www/html/images
            will return a list of file names that have the jpg file extension
            e.g. ['image1.jpg','image2.jpg','image3.jpg']

            Args:
                path (string) - path to directory
                file_extensions (list) - a list of file extensions, ['jpg','png']

            Returns:
                list - a list of file names 
        ''' 
    
        included_extensions = file_extensions
        file_names = [fn for fn in os.listdir(path)
                    if any(fn.endswith(ext) for ext in included_extensions)]

        return file_names

    def list_sub_directory_contents(self, path):
        ''' Method to list all the sub directories
            for the given path directory.

            This method will call listdirs to return
            a list of sub directories for the given path.
            It will then display the user with a choice of 
            which directory they want to use.

            Args:
                path (string): path to directory
            Returns:
                list - list of sub directory options

        '''

        print("This directory doesn't contain the media you're looking for")
        print("Here are some other sub directories to choose from: ")

        # default search option - to search again
        sub_dir_list = ["*** Search Again ***"]
        # get a list of sub directories
        dirs = self.listdirs(path)

        # add each of the sub directories to the
        # sub_dir_list list
        for d in dirs:
            sub_dir_list.append(d)

        # Loop through all the options
        for i in range(len(sub_dir_list)):
            print("{} - {}".format(i,sub_dir_list[i]))

        return sub_dir_list


    def listdirs(self, path):
        ''' Method to return a list of sub directories
            in the given file path.
            
            Args:
                path (string) - path to directory
            
            Returns:
                list - list of sub directories
        '''

        # credit to https://stackoverflow.com/a/31049707/2075215
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    def search_file_types(self, path, file_extensions):
        ''' Method to return a list of files in a directory
            limited to file extensions

            This method is intended to 
        '''
        
        return self.list_directory_media(path, file_extensions)

    def create_directory(self, path):
        ''' Method to create a directory

            The method will attempt to create a directory
            from the given path parameter

            Args:
                path (string) - directory path

            Returns:
                boolean
        '''

        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True

    def delete_file(self, path):
        ''' Method to delete a file

            This method accepts one parameter,
            the path to the file you want to delete.

            Args:
                path - path to file

            Returns:
                boolean
        '''
        
        try:
            os.remove(path)
            return True
        except (OSError, IOError):
            print("Error moving the file")
            print("Couldn't delete {}".format(path))

    def move_file(self, path, destination):
        ''' Method to move a file

            The method accepts two parameters
            the current location of the file
            and the destination of where you 
            want to move the file to?

            Args:
                path - path of the file
                desination - the location where the file is to be moved to

            Returns:
                boolean
        '''

        try:
            os.rename(path, destination)
            return True
        except (OSError, IOError):
            print("Error moving the file")
            print("Couldn't move {} to {}".format(path, destination))
        