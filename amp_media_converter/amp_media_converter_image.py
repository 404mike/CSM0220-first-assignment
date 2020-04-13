from PIL import Image
from PIL import ImageOps
from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media_Converter_User_Interaction


class AMP_Media_Converter_Image(AMP_Media_Converter_Interface):
    ''' Image class
    '''

    def get_directory_path(self):
        ''' TEXT
        '''

        file_extensions = ['jpg']
        user_input = AMP_Media_Converter_User_Interaction()
        dir_files = user_input.get_dir_path(file_extensions)
        return dir_files

    def search_files(self):
        ''' TEXT
        '''

        pass

    def write_file(self):
        ''' TEXT
        '''

        pass

    def delete_file(self):
        ''' TEXT
        '''

        pass

    def move_file(self):
        ''' TEXT
        '''

        pass

    def convert(self):
        ''' TEXT
        '''

        # Ask the user path to directory
        self.get_directory_path()

    def create_directory(self):
        ''' TEXT
        '''
        

        pass

