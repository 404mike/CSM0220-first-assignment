import os
import os.path
import shutil
import unittest
from amp_media_converter import AMP_Media_Converter_Image 
from PIL import Image

class Test_AMP_Media_Converter_Image(unittest.TestCase):

  def setUp(self):
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
    print("finished")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir_path = 'thumbnails'

    dir_path_remove = images_dir_path + thumbnail_dir_path

    try:
        shutil.rmtree(dir_path_remove)
    except OSError as e:
        print("Error: %s : %s" % (dir_path_remove, e.strerror))

  def test_convert_image(self):
    '''
    '''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir_path = 'thumbnails'

    # list of images to convert
    images_list = ['adorable-animal-breed-canine-374906.jpg',
                   'close-up-of-dog-yawning-248307.jpg',
                   'adult-tan-and-white-french-bulldog-545063.jpg',			'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg',
                   'animal-dog-pet-cute-2007.jpg',				'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg',
                   'animal-dog-puppy-pug-59523.jpg',
                   'grayscale-photo-of-french-mastiff-close-up-photo-1435517.png']

    amp_image = AMP_Media_Converter_Image()

    # create the thumbnails
    for image in images_list:
      amp_image.convert_image(image, images_dir_path, thumbnail_dir_path, 200)

    # test the thumbnails have been created
    for image in images_list:
      new_dir_path = images_dir_path + thumbnail_dir_path + '/' + image
      self.assertTrue(os.path.exists(new_dir_path))

  def test_converted_images_dimensions(self):
    '''
    '''

    dir_path = os.path.dirname(os.path.realpath(__file__))
    images_dir_path = dir_path + '/files/images/'
    thumbnail_dir_path = 'thumbnails'

    images_dict_dimensions = {
      'adorable-animal-breed-canine-374906.jpg' : {'width':200, 'height':115 },
      'close-up-of-dog-yawning-248307.jpg' : { 'width':200, 'height':133},
      'adult-tan-and-white-french-bulldog-545063.jpg' : {'width':200, 'height':133},
      'close-up-photography-of-fawn-pug-covered-with-brown-cloth-374898.jpg' : {'width':200, 'height':133},
      'animal-dog-pet-cute-2007.jpg' : {'width':200, 'height':300},
      'english-cocker-spaniel-puppy-sitting-on-ground-beside-grass-1254140.jpg' : {'width':200, 'height':133},
      'animal-dog-puppy-pug-59523.jpg' : {'width':200, 'height':130},
      'grayscale-photo-of-french-mastiff-close-up-photo-1435517.png': {'width':233,'height':234}
    }

    # test image file dimensions
    for k, v in images_dict_dimensions.items():
      image = k
      expected_width = v['width']
      expected_height = v['height']
      im = Image.open(images_dir_path + thumbnail_dir_path + '/' + image)
      w, h = im.size
      # print("{} - {} - {}".format(image,w,h))
      self.assertTrue(expected_width, w)
      self.assertTrue(expected_height, h)

    self.tearDownDir()



