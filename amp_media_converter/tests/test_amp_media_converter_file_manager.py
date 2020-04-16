import os
import os.path
import unittest
from amp_media_converter import AmpMediaConverterFileManager 

class Test_AMP_Media_Converter_File_Manager(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(Test_AMP_Media_Converter_File_Manager, self).__init__(*args, **kwargs)
    self.amp_dir = AmpMediaConverterFileManager()

  def setup(self):
    pass
  
  def tearDown(self):
    pass

  def get_current_dir(self):
    ''' Method to get the path to package
        test directory

        Returns:
          string - path to current directory 
    '''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

  def test_validate_path(self):
    ''' Test to validate a path is valid

        Test is passed a path to the currnet 
        directory which should be a valid directory.

        The test should pass.
    '''

    path = self.get_current_dir()

    is_dir = self.amp_dir.validate_path(path)
    
    self.assertTrue(is_dir)

  def test_invalidate_path(self):
    ''' Test to validate a path is valid

        Test is passed an invalid path dicrectory.

        The test should fail.
    '''

    path = self.get_current_dir()

    path = path + '/no_dir_here'

    is_dir = self.amp_dir.validate_path(path)
    
    self.assertFalse(is_dir)

  def test_jpg_list_directory_media(self):
    ''' Test to check the contents of the directory

        The test should be limited to searching for jpg
        images only.

        The test will compare the list that is returned 
        with the one that we expect.
    '''

    path = self.get_current_dir() + '/files/images'

    file_extensions = ['jpg']

    response = self.amp_dir.list_directory_media(path,file_extensions)

    expected_list = ['animal-dog-puppy-pug-59523.jpg', 'adorable-animal-breed-canine-374906.jpg', 'close-up-of-dog-yawning-248307.jpg', 'animal-dog-pet-cute-2007.jpg', 'adult-tan-and-white-french-bulldog-545063.jpg', 'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg', 'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg']

    self.assertListEqual(response, expected_list)

  def test_multi_content_list_directory_media(self):
    ''' Test to check the contents of the directory

          The test should be limited to searching for jpg
          images only.

          The test will compare the list that is returned 
          with the one that we expect.
    '''

    path = self.get_current_dir() + '/files/images'

    file_extensions = ['jpg','png']

    response = self.amp_dir.list_directory_media(path,file_extensions)

    expected_list = ['grayscale-photo-of-french-mastiff-close-up-photo-1435517.png', 'adorable-blur-breed-close-up-406014.png', 'black-and-brown-rottweiler-puppy-1307630.png', 'animal-dog-puppy-pug-59523.jpg', 'adorable-animal-breed-canine-374906.jpg', 'close-up-of-dog-yawning-248307.jpg', 'animal-dog-pet-cute-2007.jpg', 'adult-tan-and-white-french-bulldog-545063.jpg', 'adult-black-pug-1851164.png', 'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg', 'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg']

    self.assertListEqual(response, expected_list)

  def test_list_sub_directory_contents(self):
    ''' Test to check the list of sub-directories

        If no images have been found we need to show a
        list of other directories to search.

        This test should compare a list of directories
        with the ones we expect.

        The response should also include the option
        to search again.
    '''

    path = self.get_current_dir() + '/files/empty_images_dir'

    response = self.amp_dir.list_sub_directory_contents(path)

    expected_list = ['*** Search Again ***', 'images', 'empty_dir_two', 'empty_dir_one']

    self.assertListEqual(response, expected_list)

  def test_listdirs(self):
    ''' Test to check the list of sub-directories

        If no images have been found we need to show a
        list of other directories to search.

        This test should compare a list of directories
        with the ones we expect
    '''
    path = self.get_current_dir() + '/files/empty_images_dir'

    response = self.amp_dir.listdirs(path)
    
    expected_list = ['images', 'empty_dir_two', 'empty_dir_one']

    self.assertListEqual(response, expected_list)

  def test_search_file_types(self):
    ''' Test to check the contents of the directory

        The test should be limited to searching for jpg
        images only.

        The test will compare the list that is returned 
        with the one that we expect.
    '''

    path = self.get_current_dir() + '/files/images'

    file_extensions = ['jpg']

    response = self.amp_dir.search_file_types(path,file_extensions)

    expected_list = ['animal-dog-puppy-pug-59523.jpg', 'adorable-animal-breed-canine-374906.jpg', 'close-up-of-dog-yawning-248307.jpg', 'animal-dog-pet-cute-2007.jpg', 'adult-tan-and-white-french-bulldog-545063.jpg', 'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg', 'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg']

    self.assertListEqual(response, expected_list)

  def test_create_directory(self):
    ''' Test to check that you can create a 
        new directory.

        The test will create a new directory in
        the current directory within the /files/empty_images_dir
        and create an empty directory test_dir.

        The test will check if the directory has been created
        then will delete the test_dir directory.
    '''

    path = self.get_current_dir() + '/files/empty_images_dir'

    new_dir_path = path + '/test_dir'

    self.amp_dir.create_directory(new_dir_path)

    self.assertTrue(os.path.exists(new_dir_path))

    # delete created directory
    os.rmdir(new_dir_path)
    
  def test_delete_file(self):
    ''' Test deleting a file

        Create a tempory file temp.amp

        Test to make sure it has been created.

        Then delete the file.

        Then delete the file.

        Then test to make sure the file has been deleted
    '''

    path = self.get_current_dir() + '/files/empty_images_dir/'

    # create a test file
    testFile  = path + "temp.amp"
    try:
      fo = open(testFile, 'x')
    except FileExistsError:
      print("Could not create file")
      pass

    fo.close()

    # make sure the file exists
    file_exists = os.path.isfile(testFile)

    self.assertTrue(file_exists)

    # delete file
    self.amp_dir.delete_file(testFile)

    # check to make sure the file has been removed
    file_exists = os.path.isfile(testFile)

    self.assertFalse(file_exists)

  def test_move_file(self):
    ''' Test to move a file from location to another

        The test will attempt to move a file
        from one location to another.
        It will make sure the file is no longer
        present in location 1 but is present
        in location 2.

        The test will then attempt to move the 
        file from location 2 to location 1.
        It will make sure the file is no longer
        present in location 2 but is present
        in location 1.
    '''

    path = self.get_current_dir() + '/files/empty_images_dir/'

    file1 = path + 'empty_dir_one/temp.amp'
    file2 = path + 'empty_dir_two/temp.amp'

    # move file from location 1 to location 2
    self.amp_dir.move_file(file1,file2)

    file1_exists = os.path.isfile(file1)
    file2_exists = os.path.isfile(file2)

    self.assertFalse(file1_exists)

    self.assertTrue(file2_exists)

    # move file from location 2 to location 1
    self.amp_dir.move_file(file2,file1)

    file1_exists = os.path.isfile(file1)
    file2_exists = os.path.isfile(file2)

    self.assertTrue(file1_exists)

    self.assertFalse(file2_exists)

if __name__ == '__main__':
    unittest.main()