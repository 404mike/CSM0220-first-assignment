from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media_Converter_User_Interaction
from PIL import Image
from PIL import ImageOps
import os

class AMP_Media_Converter_Image(AMP_Media_Converter_Interface):
    ''' Image class
    '''

    def get_directory_path(self):
        ''' TEXT
        '''

        user_input = AMP_Media_Converter_User_Interaction()
        user_input.get_dir_path()
        pass

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

        pass

    def create_directory(self):
        ''' TEXT
        '''

        pass

