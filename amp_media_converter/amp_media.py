from amp_media_converter import AMP_Media_Converter_User_Interaction
from amp_media_converter import AMP_Media_Converter_File_Manager

class AMP_Media:
    ''' Text
    '''
    
    
    def get_dir_path(self,file_extensions):
        ''' Text
        '''

        user_interact = AMP_Media_Converter_User_Interaction()
        path = user_interact.get_dir_path(file_extensions)
        result = self.validate_dir_path(path, file_extensions)
        return result
        
    def validate_dir_path(self, path, file_extensions):
        ''' Text
        '''

        amp_dir = AMP_Media_Converter_File_Manager()
        is_valid_dir = amp_dir.validate_path(path)

        if is_valid_dir:
            file_names = amp_dir.list_directory_media(path, file_extensions)
            return self.check_files_exist(file_names, path, file_extensions)
            # return files
        else:
            print("{} doesn't exist, try again".format(path))
            self.get_dir_path(file_extensions)  


    def check_files_exist(self, file_names, path, file_extensions):
        ''' Text
        '''

        # if list is empty
        if not file_names:          
            amp_dir = AMP_Media_Converter_File_Manager()  
            user_interact = AMP_Media_Converter_User_Interaction()

            sub_dir_list = amp_dir.list_directory_contents(path,file_extensions)
            # print(sub_dir_list)

            chosen_sub_dir = user_interact.get_user_sub_directory_choice(sub_dir_list)

            if(path.endswith('/')):
                new_path = path + chosen_sub_dir
            else:
                new_path = path + '/' + chosen_sub_dir

            # print("new dir is {} ".format(new_path))
            dir_media = amp_dir.list_directory_media(new_path, file_extensions)
            return [new_path, dir_media]

        else:
            return [path, file_names]




