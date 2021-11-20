from amp_media_converter import AmpMediaConverterImage, AmpMediaConverterFileManager, AmpMediaConverterImageToPDF
import random
import string

amp = AmpMediaConverterImage()
amp_file = AmpMediaConverterFileManager()
amp_pdf = AmpMediaConverterImageToPDF()

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
    thumb_dir = thumb_dir + '_' + \
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    amp.create_directory('./', thumb_dir)
    print("Created new directory - {}".format(thumb_dir))
else:
    # create directory
    amp.create_directory('./', thumb_dir)

# file types to search for
file_ext = ['jpg', 'png']

# get list of images from a directory
files = amp_file.search_file_types(path_to_images, file_ext)

# loop each image file and convert to thumbnail
for img_file in files:
    amp.convert_image(img_file, path_to_images, thumb_dir, 40)

# create pdf from the thumbnails
amp_pdf.convert_image_to_pdf(files, thumb_dir, thumb_dir, 'dogs.pdf')
