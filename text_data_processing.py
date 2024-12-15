import matplotlib.pyplot as plt
import re
import cv2
import os
import pandas as pd
import numpy as np

# Open the file and read its data
def readFile (path):
    with open(path, encoding="utf8") as file:
        data = file.read()
    return data


# Read captions from the file Flickr8k.token.txt
data = readFile(r"../fliker_30k/results.csv")

# Split the data into each line, to get a list of captions
captions = data.split('\n')
# Remove the last line since it is blank
captions = captions[:-1]



print("Total number of caption = " + str(len(captions)))
print(captions[0])

# Store the captions in a dictionary
# Each imageID will be mapped to a list of its captions
line_procesed=0
content = {}

for line in captions:
    line_procesed+=1
    # print(line_procesed)
    # print(line)
    imageID,number, caption = line.split('|')

    imageID = imageID.split('.')[0]

    # If the imageID doesn't exist in the dictionary, create a blank entry
    if content.get(imageID) is None:
        content[imageID] = []

    # Append the current caption to the list of the corresponding image
    content[imageID].append(caption)






#Check that the captions have been mapped correctly

# Choose a random number, say 25

IMG_PATH = "../fliker_30k/images/"
image_id = captions[25].split('.')[0]

img = cv2.imread(IMG_PATH + image_id + ".jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis("off")
plt.show()

print("CAPTIONS - ")
for caption in content[image_id]:
    print(caption)


#Clean the data and save it into a new file

def clean (data):
    # Convert all characters to lower case
    data = data.lower()

    # Convert all non-alphabet characters to ' '
    data = re.sub("[^a-z]+", " ", data)

    return data

for ID, caption_list in content.items():
    for i in range(len(caption_list)):
        content[ID][i] = clean(content[ID][i])

print(content[captions[25].split('.')[0]][-1])



with open ("cleanText.txt", "w") as file:
    file.write(str(content))



# Flickr_text_dir = "../fliker_30k/results.csv"
# Flickr_jpg_dir = "../fliker_30k/images"
# jpgs = os.listdir(Flickr_jpg_dir)  
# print("Number of .jpg flies in Flicker30k Dataset: {}".format(len(jpgs)))



# file = open(Flickr_text_dir,'r', encoding="utf8") 
# text = file.read() 
# file.close() 
# datatxt = []
# for line in text.split('\n'): 
#     col = line.split('\t') 
#     if len(col) == 1:
#         continue
#     w = col[0].split("#") 
#     datatxt.append(w + [col[1].lower()])
# df_txt_flickr = pd.DataFrame(datatxt,columns=["filename","index","caption"])
# uni_filenames = np.unique(df_txt_flickr.filename.values)  
# print("Total no. of Unique File Names: {}".format(len(uni_filenames)))