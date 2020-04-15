from amp_media_converter import AMP_Media_Converter_Image, AMP_Media_Converter_File_Manager, AMP_Media_Converter_Image_To_PDF
import random
import string

amp = AMP_Media_Converter_Image()
amp_file = AMP_Media_Converter_File_Manager()
amp_pdf = AMP_Media_Converter_Image_To_PDF()

# path to images
path_to_images = './amp_media_converter/tests/files/images/'

# thumbnail directory
thumb_dir = 'example_thumbnails'

# check directory exists
dir_exists = amp_file.validate_path(thumb_dir)

# if thumbnail directory exists create a new one
# with a random file name: thumbnail_random_string
# else, create thumbnail directory
if dir_exists:
  thumb_dir = thumb_dir + '_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
  amp.create_directory('./', thumb_dir)
  print("Created new directory - {}".format(thumb_dir))
else:
  # create directory
  amp.create_directory('./', thumb_dir)

# file types to search for
file_ext = ['jpg','png']

# get list of images from a directory
files = amp_file.search_file_types(path_to_images, file_ext)

# loop each image file and convert to thumbnail
for file in files:
  amp.convert_image(file, path_to_images, thumb_dir, 400)

# create pdf from the thumbnails
amp_pdf.convert_image_to_pdf(files, thumb_dir, thumb_dir, 'test.pdf')
