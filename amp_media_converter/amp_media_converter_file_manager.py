import os
import os.path

class AMP_Media_Converter_File_Manager:
    ''' Text
    '''

    def validate_path(self, path):
        ''' Text
        '''

        is_valid_dir = os.path.isdir(path)  
        return is_valid_dir

    def list_directory_media(self, path, file_extensions):
        ''' Text
        ''' 
        
        #valid_dir = self.validate_path(path)

        relevant_path = path
        included_extensions = file_extensions
        file_names = [fn for fn in os.listdir(relevant_path)
                    if any(fn.endswith(ext) for ext in included_extensions)]

        return file_names

    def list_directory_contents(self, path, file_extensions):
        ''' Text
        '''

        print("This directory doesn't contain the media you're looking for")
        print("Here are some other sub directories to choose from: ")

        sub_dir_list = ["*** Search Again ***"]
        dirs = self.listdirs(path)
        for d in dirs:
            sub_dir_list.append(d)

        for i in range(len(sub_dir_list)):
            print("{} - {}".format(i,sub_dir_list[i]))

        return sub_dir_list


    def listdirs(self, path):
        ''' Text
            https://stackoverflow.com/a/31049707/2075215
        '''

        # https://stackoverflow.com/a/31049707/2075215
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    def search_file_types(self, path, types):
        ''' Text
        '''
        
        pass

    def create_directory(self, path):
        ''' Text
        '''

        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

    def delete_file(self, path):
        ''' Text
        '''
        
        pass