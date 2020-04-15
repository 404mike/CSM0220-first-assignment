import os
import os.path
import shutil
import unittest
from amp_media_converter import AMP_Media_Converter_Image 
from PIL import Image

class Test_AMP_Media_Converter_Image(unittest.TestCase):


  def __init__(self, *args, **kwargs):
    super(Test_AMP_Media_Converter_Image, self).__init__(*args, **kwargs)
    self.amp_image = AMP_Media_Converter_Image()

  def setUp(self):
    ''' Create new thumbnail directory'''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    thumbnail_dir_path = dir_path + '/files/images/thumbnails'

    try:
        os.mkdir(thumbnail_dir_path)
        print("Created " + thumbnail_dir_path)
    except OSError:
        print ("Creation of the directory %s failed" % thumbnail_dir_path)
    else:
        print ("Successfully created the directory %s " % thumbnail_dir_path)

    pass
  
  def tearDownDir(self):
    ''' Remove thumbnail directory'''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir_path = 'thumbnails'

    dir_path_remove = images_dir_path + thumbnail_dir_path

    try:
        shutil.rmtree(dir_path_remove)
    except OSError as e:
        print("Error: %s : %s" % (dir_path_remove, e.strerror))

  def test_convert_image(self):
    ''' Test to convert imgaes to thumbnails

        The test will loop through and create a thumbnail
        for each of the images in the imges_list list.
        The thumbnail will be save in the thumbnails directory.

        The test will then check the thumbnails directory
        to see if the image has been created?
    '''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir = 'thumbnails'
    thumbnail_dir_path = images_dir_path + thumbnail_dir

    # list of images to convert
    images_list = ['adorable-animal-breed-canine-374906.jpg',
                   'close-up-of-dog-yawning-248307.jpg',
                   'adult-tan-and-white-french-bulldog-545063.jpg',			'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg',
                   'animal-dog-pet-cute-2007.jpg',				'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg',
                   'animal-dog-puppy-pug-59523.jpg',
                   'grayscale-photo-of-french-mastiff-close-up-photo-1435517.png']

    # create the thumbnails
    for image in images_list:
      self.amp_image.convert_image(image, images_dir_path, thumbnail_dir_path, 200)

    # test the thumbnails have been created
    for image in images_list:
      new_dir_path = images_dir_path + thumbnail_dir + '/' + image
      self.assertTrue(os.path.exists(new_dir_path))

  def test_converted_images_dimensions(self):
    ''' Test to see if the image dimensions 
        for the thumnails are correct

        The test will loop through all the images
        in the images_dict_dimensions dictionary
        and using Pillow, get the width and height
        of the thumbnail and compare the values,
        to make sure the size of the thumbnail is correct?
    '''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir_path = 'thumbnails'
    # thumbnail_dir_path = images_dir_path + thumbnail_dir_dir

    images_dict_dimensions = {
      'adorable-animal-breed-canine-374906.jpg' : {'width':200, 'height':115 },
      'close-up-of-dog-yawning-248307.jpg' : { 'width':200, 'height':133},
      'adult-tan-and-white-french-bulldog-545063.jpg' : {'width':200, 'height':133},
      'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg' : {'width':200, 'height':133},
      'animal-dog-pet-cute-2007.jpg' : {'width':133, 'height':200},
      'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg' : {'width':200, 'height':133},
      'animal-dog-puppy-pug-59523.jpg' : {'width':200, 'height':130},
      'grayscale-photo-of-french-mastiff-close-up-photo-1435517.png': {'width':133,'height':200}
    }

    # test image file dimensions
    for k, v in images_dict_dimensions.items():
      image = k
      expected_width = v['width']
      expected_height = v['height']
      im = Image.open(images_dir_path + thumbnail_dir_path + '/' + image)
      w, h = im.size
      # print("{} - {} - {}".format(image,w,h))
      self.assertEqual(expected_width, w)
      self.assertEqual(expected_height, h)

    # Delete directory
    self.tearDownDir()



