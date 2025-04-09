import streamlit as st
import random
import recommender_utils
import json
import os

## streamlit run app_negative_example.py

# Read keywords from JSON file
with open('category_tags.json', 'r') as f:
    img_to_key = json.load(f)

good_keys = ['high_fashion', 'sport', 'trad_wife_pos', 'dogs', 'party']
negative_keys = ['trad_wife_negative','mushrooms', 'alcohol', 'couple', 'thin']
good_bad_map = {'high_fashion': 'thin', 'thin': "thin",
                'sport': 'couple', 'couple':'couple', 
                'trad_wife_pos': 'trad_wife_negative', 'trad_wife_negative': 'trad_wife_negative',
                'dogs': 'mushrooms', "mushrooms": 'mushrooms',
                'party': 'alcohol', 'alcohol': 'alcohol'}
corrupt_images = ['IMG_6933.png', 'IMG_6934.png', 'IMG_6944.png','IMG_6949.png', 'IMG_6953.png','IMG_6955.png', 'IMG_6965.png', 'IMG_7002.png'] # they throw an error when trying to open

image_pool = []
neg_image_pool = []
# create dict with key (e.g. "katze") to img-name 
key_to_img = {}
not_recommended_img = {}
counter_per_group = {}
for img, keylist in img_to_key.items():
    for keyname in keylist:
        if keyname not in key_to_img:
            key_to_img[keyname] = []     
            not_recommended_img[keyname] = [] 
        key_to_img[keyname].append(img)
        not_recommended_img[keyname].append(img) #there are the images that we have not shown yet
        if len(keylist) > 1: # only append the fotos that have both a positive, and a negative key
            if keylist[0] not in counter_per_group:
                counter_per_group[keylist[0]] = 0
            if counter_per_group[keylist[0]] < 5: # only include max 5 examples per category
                if not img.split('/')[-1] in corrupt_images: # exclude the images that threwh a problem (see test_img.py)
                    image_pool.append(img)
                    counter_per_group[keylist[0]] = counter_per_group[keylist[0]]+ 1
        else:
            if keylist[0] in negative_keys:
                if not img.split('/')[-1] in corrupt_images:

                    
                        neg_image_pool.append(img)
                        
                else:
                    print('!!!!! problem with image:', img)

print(image_pool)
print('........................')
print(counter_per_group)
print('neg:', neg_image_pool)

random.shuffle(image_pool)

# Initialize session state
if 'liked_images' not in st.session_state:
    st.session_state.liked_images = []
if 'ignored_images' not in st.session_state:
    st.session_state.ignored_images = []
if 'shown_images' not in st.session_state:
    st.session_state.shown_images = []
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'current_image' not in st.session_state:
    st.session_state.current_image = image_pool[0]
if 'next_triggered' not in st.session_state:
    st.session_state.next_triggered = False
if 'prev_image' not in st.session_state:
    st.session_state.prev_image = None
if 'liked' not in st.session_state:
    st.session_state.liked = False
st.session_state.not_recommended_img = not_recommended_img

# Function to show a single image with like/next options
def display_image(page):
    # image_to_show =  image_pool[page-1]

    if st.session_state.current_image:
        st.session_state.prev_image = st.session_state.current_image  # Save the previous image
        print('prev:', st.session_state.prev_image)

    image_to_show = image_pool.pop(0)  # Get the next image and remove it from the pool

    while image_to_show in st.session_state.shown_images: # show each image only once
        image_to_show = image_pool.pop(0)
    st.session_state.current_image = image_to_show  # Update to the new image


    st.write(f"✨ Magst du dieses Bild?")
    st.image(image_to_show, use_container_width=True)
    
    st.write(" ")  # Add spacing for better UI

    # Centered column layout for buttons
    col = st.columns([1, 2, 1])[1]  # Centering trick

    img_key = img_to_key[image_to_show]
    for key in img_key:
        st.session_state.not_recommended_img[key].remove(image_to_show)
        # st.session_state.not_recommended_img = not_recommended_img

    st.session_state.shown_images.append(image_to_show)

    with col:
        like_clicked = st.button("❤️ Like", key="like_button", use_container_width=True, on_click=lambda: st.session_state.update(liked=True))
        next_clicked = st.button("➡️ Naja. Nächstes", key="next_button", use_container_width=True, on_click=lambda: st.session_state.update(liked=False))

    if like_clicked:
        st.session_state.liked_images.append(st.session_state.prev_image)
        st.session_state.page += 1
        # st.rerun()  # Using st.rerun() instead of experimental_rerun
    elif next_clicked:
        st.session_state.page += 1


def next_image():
    #st.session_state.page += 1  # Ensure the counter moves forward
    st.rerun()  # Force Streamlit to refresh the UI

# Show results after 5 pages
def show_results():
    if st.session_state.current_image:
        st.session_state.prev_image = st.session_state.current_image  # Save the previous image

    if st.session_state.liked:
        print('liked')
        st.session_state.liked_images.append(st.session_state.prev_image)
    else:
        print('not liked')

    st.markdown("## 🎯 Deine Auswahl")
    if st.session_state.liked_images:
        for img in st.session_state.liked_images:
            # st.image(img, use_container_width=True)
            st.image(img, width=100)
    else:
        st.write("Du hast keine Bilder geliked.")
    if st.button("Zeige Empfehlungen 💡"):
        st.session_state.page += 1
        st.rerun()

# Show recommendation
def show_recommendation():
    print('now recommending')
    print(st.session_state.not_recommended_img)
    st.markdown("## 🌟 Deine Empfehlung")
    st.write("Basierend auf deinen Lieblingsbildern empfehle ich dir:")
    rec, rec_img = recommender_utils.compute_recommendation_neg(st.session_state.liked_images, img_to_key, key_to_img, 
                                                                st.session_state.shown_images, negative_images=neg_image_pool, good_bad_map=good_bad_map)
    # st.success(f"🎉 {rec}") # we can delete this at some point.
    st.image(rec_img, width=300)


# Main logic
border = 15
if st.session_state.page < border: # show 5 images
    display_image(st.session_state.page)
elif st.session_state.page == border: # show overview of the liked images
    show_results()
else: # then show recommendations
    show_recommendation()
