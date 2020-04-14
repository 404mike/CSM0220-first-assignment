class AMP_Media_Converter_Interface:
    ''' Abstract Class for media converter classes

        Any class that converts media should inherit from this class
        and all method within this class should be implemented
        within these sub-classes
    '''

    def __init__(self):
        pass

    def get_directory_path(self):
        ''' Method to prompt the user for a directory path
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def write_file(self):
        ''' Method to allow a user to write a file
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def delete_file(self):
        ''' Method to allow a user to delete a file
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def move_file(self):
        ''' Method to allow a user to move a file
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def convert(self):
        ''' Method to convert media
            it should accept a list parameter - file_extensions
            which the class should search for an convert 
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def create_directory(self):
        ''' Method to allow a user to create a directory
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

