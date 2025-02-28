#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:  Eyong Kevin Enowanyo
# DATE CREATED: Oct 19, 2019                                  
# REVISED DATE: Oct 21, 2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from os.path import splitext

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    get_images = listdir(image_dir)
    print("Image size is:",len(get_images))
    results_dic = dict()

    for get_image in get_images:
        if not get_image.startswith('.'):
            label_names = ""
            label_name_list = []
            # Split text to remove the extension and use just the root name
            root_image_name = splitext(get_image)[0]

            splitImage = root_image_name.lower().split("_")
            for si in splitImage:
                if si.isalpha():
                    label_names += si +" "
            label_name_list.append(label_names.strip())
            # Make sure file name is not already in dict
            if get_image not in results_dic:
                results_dic[get_image] = label_name_list
            else:
                print("** Warning: Duplicate files exist in directory: ", 
                         get_image)
                
    return results_dic

