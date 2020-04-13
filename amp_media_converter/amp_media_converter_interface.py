class AMP_Media_Converter_Interface:
    ''' TEXT
    '''

    def __init__(self):
        pass

    def get_directory_path(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def search_files(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def write_file(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def delete_file(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def move_file(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def convert(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

    def create_directory(self):
        ''' TEXT
        '''

        raise NotImplementedError("Subclass must implement this abstract method")

