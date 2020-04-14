from PIL import Image
from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media

class AMP_Media_Converter_Image(AMP_Media_Converter_Interface):
    ''' Image class
    '''

    def __init__(self):
        self.thumb_dir = 'thumbnails'

    def convert(self):
        ''' TEXT
        '''
        
        # Ask the user path to directory
        _, path, files = self.get_directory_path()
        self.process_files(path, files)

    def get_directory_path(self):
        ''' TEXT
        '''

        file_extensions = ['jpg']
        amp = AMP_Media()
        dir_files = amp.get_dir_path(file_extensions)
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

    def process_files(self, path, files):
        ''' Text
        '''

        # get user thumbnail size
        while True:
            try:
                thumb_size =  int(input("Enter size of thumnail, number only e.g. 250: "))
                break
            except ValueError:
                print ("Not a number, try again") 
                 
        # check thumbnail directory exists
        amp_dir = AMP_Media()
        dir_name = amp_dir.create_new_directory(path, self.thumb_dir)

        for f in files:
            self.convert_image(f, path, dir_name, thumb_size)

    def convert_image(self, f, path, dir_name, thumb_size):
        ''' TEXT
        TODO try/catch
        '''

        print("Converting {}".format(f))
        basewidth = thumb_size
        img = Image.open(path + '/' + f)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(path + '/' + dir_name + '/' + f) 