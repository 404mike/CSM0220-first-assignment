from PIL import Image
from amp_media_converter import AMP_Media_Converter_Interface
from amp_media_converter import AMP_Media
import re

class AMP_Media_Converter_Image_To_PDF(AMP_Media_Converter_Interface):
    ''' Class to convert images using the Pillow library

        See https://pillow.readthedocs.io/en/stable/ for more details
        on Pillow library
    '''

    def __init__(self):
        # default directory name for
        # thumbnails are save to
        self.thumb_dir = 'pdf'

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
            method is to accept multiple file extensions.

            The method calls the convert method.

            Args:
                file_extensions (list): List of file types to convert

        '''
        
        # throw exception if no parameter specified
        if not file_extensions:
            raise Exception("No file extensions found, pass a list of file extnesions, e.g. ['jpg','png']")

        # call convert method with list of file extensions
        self.convert(file_extensions)

    def delete_file(self, path):
        ''' Method to delete a file

            This method accepts one parameter,
            the path to the file you want to delete.

            Args:
                path - path to file

            Returns:
                boolean
        '''

        amp_media = AMP_Media()
        return amp_media.delete_file(path)

    def move_file(self, path, destination):
        ''' Method to move a file

            The method accepts two parameters
            the current location of the file
            and the destination of where you 
            want to move the file to?

            This method calls move_file from
            the AMP_Media class

            Args:
                path - path of the file
                desination - the location where the file is to be moved to

            Returns:
                boolean
        '''

        amp_media = AMP_Media()
        return amp_media.move_file(path, destination)

    def create_directory(self, path, dir_name):
        ''' Method to create a new directory

            This method is intended to be used programatically
            
            Args:
                path (string) - directory path
                dir_name (string) - new directory name

            Resturns:
                boolean
        '''

        amp_media = AMP_Media()
        response = amp_media.create_new_diretory(path, dir_name)
        return response

    def process_files(self, path, files):
        ''' Method to begin the image conversion

            The method will prompt a user for a filename for the pdf.

            The method will check that the location the PDF directory
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
                pdf_file_name = input ("Enter a filename for the PDF: ").strip()
                if re.match(r'^[A-Za-z0-9_]+$', pdf_file_name):
                    break
                else:
                    print("Not a valid file name")
            except ValueError:
                print ("Not a valid file name")
                 
        # check thumbnail directory exists
        amp_media = AMP_Media()
        dir_name = amp_media.create_processed_items_directory(path, self.thumb_dir)

        # loop each file and send it to convert_image to be processed
        self.convert_image_to_pdf(files, path, dir_name, pdf_file_name)

    def convert_image_to_pdf(self, files, path, dir_name, pdf_file_name):
        ''' Method to convert a list of imges to PDF

            The method will attempt to loop through each
            image and creat a pdf of those images

            Args:
                files (list) - list of images
                path (string) - directory path
                dir_name (string) - directory to save PDF
                pdf_file_name (string) - name of PDF file
        '''
        # get first image
        im1 = Image.open(path + '/' + files[0])

        # remove the first image from the list
        files.pop(0)

        # list to store all the remaining images
        im_list = []

        # loop through the remaining images
        for f in files:
            # open the image and save to the list
            im_list.append( Image.open(path + '/' + f) )

        # create path and filename for the PDF we're trying to save
        pdf_file_name_path = path + '/' + dir_name + '/' + pdf_file_name + ".pdf"

        try:
            im1.save(pdf_file_name_path, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
        except (OSError, IOError):
            print("Could not save PDF")
            
