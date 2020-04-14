from PIL import Image
from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media

class AMP_Media_Converter_Image(AMP_Media_Converter_Interface):
    ''' Class to convert images using the Pillow library

        See https://pillow.readthedocs.io/en/stable/ for more details
        on Pillow library
    '''

    def __init__(self):
        # default directory name for
        # thumbnails are save to
        self.thumb_dir = 'thumbnails'

    def convert(self, file_extensions=['jpg']):
        ''' Method to start converting images

            This is the main method of the AMP_Media_Converter_Image class
            and will prompt the user input and process the images.

            This method will will call the get_directory_path method,
            which will call a method in the AMP_Media class.
            The AMP_Media class will promt a user for a directory
            and will validate the input, by checking if the directory
            entered is valid and if it contains any files with the file_extensions
            parameter.

            Args:
                file_extensions (list): List of file types to convert

            Parameter has a default list contain the file extension for jpg
        '''
        
        # Ask the user path to directory
        _, path, files = self.get_directory_path(file_extensions)
        # send the files to be converted
        self.process_files(path, files)

    def get_directory_path(self,file_extensions):
        ''' Method to prompt the user for a directory path

            Args:
                file_extensions (list): List of file types to convert
            
            Returns:
                list: boolean - True or False if everything worked correctly
                      path - the path to the directory specified by the user
                      files - a list of files in that path directory
        '''

        amp = AMP_Media()
        dir_files = amp.get_dir_path(file_extensions)
        return dir_files 

    def convert_multi_type(self, file_extensions=''):
        ''' Method to convert multiple file extensions

            Although the convert method can accept multiple
            file extensions, this method is intended to be
            used as clear indication that the intention of the 
            method is to accept multiple file extensions

            The method calls the convert method

            Args:
                file_extensions (list): List of file types to convert

        '''
        
        # throw exception if no parameter specified
        if not file_extensions:
            raise Exception("No file extensions found, pass a list of file extnesions, e.g. ['jpg','png']")

        # call convert method with list of file extensions
        self.convert(file_extensions)

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
        ''' Method to begin the image conversion

            The method will prompt a user for a thumbnail size
            only a single number is required as convert_image method
            will convert the image by its longest path maintaining
            its aspect ratio

            The method will check that the location the thumbnails
            already exists. The default directory name is in the constructor
            self.thumb_dir
            The create_new_directory will try and create a new directory, but
            if one with the self.thumb_dir name already exists, it will prompt
            the user to enter a new directory name
        
            Args:
                path (string) - directory path
                files (list) - list of images to convert
        '''

        # get user thumbnail size
        while True:
            try:
                thumb_size =  int(input("Enter size of thumnail, number only e.g. 250: "))
                break
            except ValueError:
                print ("Not a number, try again") 
                 
        # check thumbnail directory exists
        amp_media = AMP_Media()
        dir_name = amp_media.create_processed_items_directory(path, self.thumb_dir)

        # loop each file and send it to convert_image to be processed
        for f in files:
            self.convert_image(f, path, dir_name, thumb_size)

    def convert_image(self, f, path, dir_name, thumb_size):
        ''' Method to convert a single image to thumbnail

            The method accepts four parameters, see Args.
            It will open the image file, convert it to a thumbnail
            and save the thumbnail to the dir_name directory

            Args:
                f (string) - file name
                path (string) - directory path
                dir_name (string) - directory to store thumbnails
                thumb_size (int) - thumbnail size
        '''

        print("Converting {}".format(f))
        try:
            # open image to convert
            img = Image.open(path + '/' + f)
            wpercent = (thumb_size/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((thumb_size,hsize), Image.ANTIALIAS)
            # save thumbnail
            img.save(path + '/' + dir_name + '/' + f) 
        except IOError:
            print("Unable to save file")
