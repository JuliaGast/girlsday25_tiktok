def compute_recommendation(responses, img_to_key, key_to_img, shown_images, bad_good_map, rec_images):
    """ Compute recommendations based on the user's responses.
    """
    
    # Count the number of times each key appears in the responses
    res_dict ={}
    key_dict = {}
    rec_img = 'Images/robot.png'
    rec_key = 'none'
    for idx, response in enumerate(responses): # for each response
        if not response in res_dict: # if the response is not in the dict, add it
            res_dict[response] = 1      
        else:
            res_dict[response] += 1

        for keyname in img_to_key[response]: # for each key in the image
            if not keyname in key_dict: # if the key is not in the dict, add it
                key_dict[keyname] = 1
            else:
                key_dict[keyname] += 1
    
    if len(key_dict) == 0:
        return rec_key, rec_img

    rec_key = max(key_dict, key=key_dict.get) # get the key with the highest count
    print('recommended key:')
    print(rec_key) # print the key_dict
    rec_key = bad_good_map[rec_key]
    print(rec_key)

    # rec_img = None 
    for img in key_to_img[rec_key]: # find the images that correspond to the key
        print('img:', img)
        if img in rec_images:#not in shown_images: # if the image has not been shown yet, return it
            rec_img = img
            break

    return rec_key, rec_img


def compute_recommendation_neg(responses, img_to_key, key_to_img, shown_images, 
                               negative_images,good_bad_map):
    """ Compute recommendations based on the user's responses.
    """
    
    # Count the number of times each key appears in the responses
    res_dict ={}
    key_dict = {}
    rec_img = 'Images/robot.png'
    rec_key = 'none'
    for idx, response in enumerate(responses): # for each response
        if not response in res_dict: # if the response is not in the dict, add it
            res_dict[response] = 1      
        else:
            res_dict[response] += 1

        for keyname in img_to_key[response]: # for each key in the image
            if not keyname in key_dict: # if the key is not in the dict, add it
                key_dict[keyname] = 1
            else:
                key_dict[keyname] += 1
    
    if len(key_dict) == 0:

        return rec_key, rec_img
    rec_key = max(key_dict, key=key_dict.get) # get the key with the highest count

    # print(key_dict) # print the key_dict
    print('rec_key:', rec_key)
    rec_key = good_bad_map[rec_key]
    print('rec_key:', rec_key)
    rec_img = None 
    for img in key_to_img[rec_key]: # find the images that correspond to the key

        if img in negative_images:

        # if img not in shown_images: # if the image has not been shown yet, return it
            rec_img = img
            print(rec_img)
            return rec_key, rec_img

    
    

    return rec_key, rec_img
