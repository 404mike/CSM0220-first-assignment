'''Class to manage user interactions'''

import re

class AmpMediaConverterUserInteraction:
    ''' Class to manage all user interactions.
    '''

    def get_dir_path(self):
        ''' Method to prompt the user for a path
            to a directory where their items are.

            Returns:
                path (string)
        '''

        path = input("Enter path to your Images directory: ")
        return path

    def get_user_sub_directory_choice(self, sub_dir_list):
        ''' Class to prompt the user to choose from a list
            of sub directories.

            This method will display the user with a choice
            of directories to choose from:

                This directory doesn't contain the media you're looking for
                Here are some other sub directories to choose from:
                0 - *** Search Again ***
                1 - images
                2 - empty_dir_two
                3 - empty_dir_one

            The user must select the number which corresponds to
            that directory.

            The method will check for a type response - int
            and to make sure that the number chosen is
            within the bounds of the list.

            Args:
                sub_dir_list (list) - a list of directories

            Returns:
                string - choice of sub-directory
        '''

        while True:
            try:
                # get user input
                option = int(input("Choose a number to search or 0 to choose a new directory: "))

                try:
                    # test to make sure the number chosen is within the list
                    response = sub_dir_list[option]
                    return response
                except IndexError:
                    print("Not a valid number, choose a number from the list")
                    self.get_user_sub_directory_choice(sub_dir_list)
                break
            except ValueError:
                print("Not a number, try again")

    def get_new_directory_name(self):
        ''' Method to prompt the user for a new
            directory name.

            The method will prompt the user to enter a new
            name for the directory.

            The input will be validated against a regular
            expression, to make sure that the name is vaild?

            The validation checks to see if the string is alphanumeric
            and/or an underscore _

            Returns:
                string - new directory name
        '''

        while True:
            try:
                new_dir_name = input("Enter a new directory name: ").strip()
                if re.match(r'^[A-Za-z0-9_]+$', new_dir_name):
                    return new_dir_name

                print("Not a valid directory name")
            except ValueError:
                print("Not a valid directory name")
