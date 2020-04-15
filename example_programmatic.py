from amp_media_converter import AMP_Media_Converter_Image
from amp_media_converter import AMP_Media_Converter_File_Manager
from amp_media_converter import AMP_Media_Converter_Image_To_PDF

amp = AMP_Media_Converter_Image()
amp_file = AMP_Media_Converter_File_Manager()
amp_pdf = AMP_Media_Converter_Image_To_PDF()

# path to images
path_to_images = './amp_media_converter/tests/files/images/'

# thumbnail directory
thumb_dir = 'example_thumbnails'

# create directory
amp.create_directory('./', thumb_dir)

# file types to search for
file_ext = ['jpg']

# get list of images from a directory
files = amp_file.search_file_types(path_to_images, file_ext)

# loop each image file and convert to thumbnail
for file in files:
  amp.convert_image(file, path_to_images, thumb_dir, 400)

# create pdf from the thumbnails
amp_pdf.convert_image_to_pdf(files, path_to_images, thumb_dir, 'test.pdf')