from PIL import Image
from PIL import ImageOps
from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media

class AMP_Media_Converter_Image(AMP_Media_Converter_Interface):
    ''' Image class
    '''

    def convert(self):
        ''' TEXT
        '''
        
        # Ask the user path to directory
        foo = self.get_directory_path()
        print(foo)

    def get_directory_path(self):
        ''' TEXT
        '''

        file_extensions = ['jpg']
        amp = AMP_Media()
        dir_files = amp.get_dir_path(file_extensions)
        # print(dir_files)
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

    def create_directory(self):
        ''' TEXT
        '''

        pass

