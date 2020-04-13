import os.path
from amp_media_converter import AMP_Media_Converter_User_Interaction

class AMP_Media_Converter_File_Manager:
    ''' Text
    '''

    def validate_path(self, path):
        ''' Text
        '''

        isdir = os.path.isdir(path)  
        return isdir

    def list_directory_media(self, path, file_extensions):
        ''' Text
        '''

        valid_dir = self.validate_path(path)


        relevant_path = path
        included_extensions = file_extensions
        file_names = [fn for fn in os.listdir(relevant_path)
                    if any(fn.endswith(ext) for ext in included_extensions)]

        if not file_names:            
            return self.list_directory_contents(path,file_extensions)
        else:
            return file_names

    def list_directory_contents(self, path, file_extensions):
        ''' Text
        '''

        print("This directory doesn't contain the media you're looking for")
        print("Here are some other sub directories to choose from: ")

        sub_dir_list = ["*** Search Again ***"]
        for root,dirs,_ in os.walk(path):
            for d in dirs:
                sub_dir_list.append(d)

        for i in range(len(sub_dir_list)):
            print("{} - {}".format(i,sub_dir_list[i]))

        chosen_sub_dir = AMP_Media_Converter_User_Interaction.get_user_sub_directory_choice(sub_dir_list)

        new_path = path + '/' + chosen_sub_dir

        print("new dir is {} ".format(new_path))
        return self.list_directory_media(new_path, file_extensions)



    def search_file_types(self, path, types):
        ''' Text
        '''
        
        pass

    def create_directory(self, path, dirName):
        ''' Text
        '''
        
        pass

    def delete_file(self, path):
        ''' Text
        '''
        
        pass