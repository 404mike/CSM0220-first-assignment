#!/usr/bin/env python
"""
This class is used to transform images to thumbnails
"""
import os
from PIL import Image
from amp_media_converter import AmpMediaConverterInterface
from amp_media_converter import AmpMedia


class AmpMediaConverterImage(AmpMediaConverterInterface):
    ''' Class to convert images using the Pillow library

        See https://pillow.readthedocs.io/en/stable/ for more details
        on Pillow library
    '''

    def __init__(self):
        # default directory name for
        # thumbnails are save to
        self.thumb_dir = 'thumbnails'

        self.amp = AmpMedia()

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

    def get_directory_path(self, file_extensions):
        ''' Method to prompt the user for a directory path

            Args:
                file_extensions (list): List of file types to convert

            Returns:
                list: boolean - True or False if everything worked correctly
                      path - the path to the directory specified by the user
                      files - a list of files in that path directory
        '''

        dir_files = self.amp.get_dir_path(file_extensions)
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
            raise Exception(
                "No file extensions found, pass a list of file extnesions, e.g. ['jpg','png']")

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

        return self.amp.delete_file(path)

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

        return self.amp.move_file(path, destination)

    def create_directory(self, path, dir_name):
        ''' Method to create a new directory

            This method is intended to be used programatically

            Args:
                path (string) - directory path
                dir_name (string) - new directory name

            Resturns:
                boolean
        '''

        response = self.amp.create_new_diretory(path, dir_name)
        return response

    def process_files(self, path, files):
        ''' Method to begin the image conversion

            The method will prompt a user for a thumbnail size,
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
                thumb_size = int(
                    input("Enter size of thumnail, number only e.g. 250: "))
                break
            except ValueError:
                print("Not a number, try again")

        # check thumbnail directory exists
        dir_name = self.amp.create_processed_items_directory(
            path, self.thumb_dir)

        dir_name = os.path.join(path, dir_name)

        # loop each file and send it to convert_image to be processed
        for img_file in files:
            self.convert_image(img_file, path, dir_name, thumb_size)

    def convert_image(self, img_file, path, dir_name, thumb_size):
        ''' Method to convert a single image to thumbnail

            The method accepts four parameters, see Args.
            It will open the image file, convert it to a thumbnail
            and save the thumbnail to the dir_name directory

            Args:
                f (string) - file name
                path (string) - directory path for images
                dir_name (string) - directory to store thumbnails
                thumb_size (int) - thumbnail size
        '''

        print("Converting {}".format(img_file))

        try:
            # open image to convert
            img = Image.open(os.path.join(path, img_file))
            (width, height) = img.size

            # deal with landscape vs potrait
            if width > height:
                new_width = thumb_size
                new_height = int(new_width * height / width)
            else:
                new_height = thumb_size
                new_width = int(new_height * width / height)

            img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # save thumbnail
            img.save(os.path.join(dir_name, img_file))
        except IOError:
            print("Unable to save file")
