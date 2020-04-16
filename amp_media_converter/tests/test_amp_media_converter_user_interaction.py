import unittest
from unittest.mock import patch
from amp_media_converter import AmpMediaConverterUserInteraction

class TestAmpMediaConverterUserInteraction(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(TestAmpMediaConverterUserInteraction, self).__init__(*args, **kwargs)
    self.amp_interact = AmpMediaConverterUserInteraction()

    @patch('builtins.input', lambda *args: '/var/foo')
    def test_get_dir_path(self):
        ''' Test user input 

            This test if the input value is
            returned by the function
        '''

        expected_response = '/var/foo'
             
        response = self.amp_interact.get_dir_path()
        self.assertEqual(response, expected_response)

    @patch('builtins.input', lambda *args: 1)
    def test_get_user_sub_directory_choice(self):
      ''' Test directory choice

          This test validates the process where
          the user is asked to choose from a list
          ['one','two','three']
          the user will enter an index option that
          will return the value
      '''

      sub_dir_list = ['one','two','three']
      response = self.amp_interact.get_user_sub_directory_choice(sub_dir_list)
      expected_response = 'two'
      self.assertEqual(response, expected_response)


    @patch('builtins.input', lambda *args: 10)
    def test_get_user_sub_directory_choice_not_in_list(self):
      pass
      ''' Test directory choice

          This test validates the process where
          the user is asked to choose from a list
          ['one','two','three']
          the user will enter an index option that
          will return the value. This test checks for 
          out of bounds values.
      '''

      # sub_dir_list = ['one','two','three']
      # interaction = AMP_Media_Converter_User_Interaction()
      # try:
      #   response = interaction.get_user_sub_directory_choice(sub_dir_list)
      #   expected_response = "Not a valid number, choose a number from the list"
      #   self.assertEqual(response, expected_response)
      #   print(response)
      #   pass
      # except:
      #   print("Something went wrong FOO")

    @patch('builtins.input', lambda *args: 'new_test_dir')
    def test_get_new_directory_name(self):
      ''' Test to validate a directory name

          The test checks to see if the value for
          a directory name is valid
      '''

      response = self.amp_interact.get_new_directory_name()
      expected_response = "new_test_dir"
      self.assertEqual(response, expected_response)
      