# AMP Media Converter

## Description
The AMP (Advanced Media Production) package allows users to:
* Convert images of different types to thumbnail
* Create directories
* Move files
* Delete files

The package can be used independently, users will be guided through the
process of converting images, or the package can be used programatical,
where you will be able to used the package methods to implement your 
own solutions.

## Example usage

### User Input

This package can be used in a number of ways.

You are able to get the user to enter all the information about image location,
thumbnail sizes and the package will validate all the user input.

  ```python
    from amp_media_converter import AMP_Media_Converter_Image
    amp = AMP_Media_Converter_Image()
    amp.convert()
  ```

To replace the convert type, import the relevant class and instantiate it.

  ```python
    from amp_media_converter import AMP_Media_Converter_Image_To_PDF
    amp = AMP_Media_Converter_Image_To_PDF()
    amp.convert()
  ```

The default image type is jpg, however, multiple types are supported.
To convert more than one image format, specify a list of image extensions.

  ```python
    from amp_media_converter import AMP_Media_Converter_Image
    amp = AMP_Media_Converter_Image()
    amp.convert(['jpg','png'])
  ```

### Programatical 

You can also implement your own Python script to create, delete, move directories
and convert images.

  ```python
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
```

## unit testing

To run unit test.
  ```
    python -m unittest -b
  ```

## Test images
The images used in this package are royalty free images from [https://www.pexels.com/search/dog/](https://www.pexels.com/search/dog/)