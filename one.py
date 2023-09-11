import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from util import classify, set_background





# unable to show the image 
#image = Image.open('AG-S-001.jpg')
# If 'image' is None, you can't perform operations on it.
#image.show()



rad=st.sidebar.radio("Options",["Home","Map","Upload Image","Test the name"])

if rad == "Home":
    st.title("Welcome!")
    st.markdown("""---""")

    st.subheader("Classification of the object is followed in these following steps:")
    st.markdown("""
    ### 1.Medicinal / Non-medicinal.<br>
    ### 2.Plant(Leaf)/Raw.<br>
    ### 3.If leaf,Which genetic breed they belong.<br><br>
    """,True)
    st.graphviz_chart("""
    digraph{
    Object -> Medicinal
    Object -> Nonmedicianl
    Medicinal -> Leaves
    Medicinal ->Raw
    Leaves -> Species
    }
    """)
    st.markdown("""---
## Categories 
#### -Herbal Medicine.<br> 
#### -Traditional Medicine.<br>
#### -Ayurveda, Medicinal Use of Plants.<br>
#### -Medicinal Crop, Leaf Studies.<br><br>
---
_Botanical Name and its Common Name_""",True)

    d={
    "Alpinia Galanga":"Rasna",
    "Amaranthus Viridis":"Arive-Dantu",
    "Artocarpus Heterophyllus":"Jackfruit",
    "Azadirachta Indica":"Neem",
    "Basella Alba":"Basale",
    "Brassica Juncea":"Indian Mustard",
    "Carissa Carandas":"Karanda",
    "Citrus Limon":"Lemon",
    "Ficus Auriculata":"Roxburgh fig",
    "Ficus Religiosa":"Peepal Tree",
    "Rosa-sinensis":"Hibiscus",
    "Jasminum":"Jasmine",
    "Mangifera Indica":"Mango",
    "Mentha":"Mint",
    "Moringa Oleifera":"Drumstick",
    "Muntingia Calabura":"Jamaica Cherry-Gasagase",
    "Murraya Koenigii":"Curry",
    "Nerium Oleander":"Oleander",
    "Nyctanthes Arbor-tristis":"Parijata",
    "Ocimum Tenuiflorum":"Tulsi",
    "Piper Betle":"Betel",
    "Plectranthus Amboinicus":"Mexican Mint",
    "Pongamia Pinnata":"Indian Beech",
    "Psidium Guajava":"Guava",
    "Punica Granatum":"Pomegranate",
    "Santalum Album":"Sandalwood",
    "Syzygium Cumini":"Jamun",
    "Syzygium Jambos":"Rose Apple",
    "Tabernaemontana Divaricata":"Crape Jasmine",
    "Trigonella Foenum-graecum":"Fenugreek"

    }

    st.write(d)
    st.markdown("""
    ### Source<br>
    ### Medicinal Leaf Dataset- <br> 
    ###### <https://data.mendeley.com/datasets/nnytj2v3n5/1> 

    """,True)


if rad == "Map":
    st.header("Map")
    st.map()

if rad == "Upload Image":
    st.title('Fish Classification')

# set header
    st.header('Please upload an image of a fish of the following species: Black Sea Sprat, Gilt-Head Bream, Hourse Mackerel, Red Mullet, Red Sea Bream, Sea Bass, Shrimp, Striped Red Mullet, Trout')

# upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
    model = load_model('model.h5')

# load class names
# with open('./model/labels.txt', 'r') as f:
#     class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
#     f.close()
    class_names=['Black Sea Sprat', 'Gilt-Head Bream', 'Hourse Mackerel', 'Red Mullet', 'Red Sea Bream', 'Sea Bass', 'Shrimp', 'Striped Red Mullet', 'Trout']

# display image
    if file is not None:
     image = Image.open(file).convert('RGB')
     st.image(image, use_column_width=True)

    # classify image
     class_name, conf_score = classify(image, model, class_names)

    # write classification
     st.write("## {}".format(class_name))
     st.write("### score: {}%".format((conf_score*10)))

if rad == "Test the name":
    st.markdown("""---
### Testing -
""",True)
    name= st.text_input("Enter the botinacial name to know the common name:")
    d={
    "Alpinia Galanga":"Rasna",
    "Amaranthus Viridis":"Arive-Dantu",
    "Artocarpus Heterophyllus":"Jackfruit",
    "Azadirachta Indica":"Neem",
    "Basella Alba":"Basale",
    "Brassica Juncea":"Indian Mustard",
    "Carissa Carandas":"Karanda",
    "Citrus Limon":"Lemon",
    "Ficus Auriculata":"Roxburgh fig",
    "Ficus Religiosa":"Peepal Tree",
    "Rosa-sinensis":"Hibiscus",
    "Jasminum":"Jasmine",
    "Mangifera Indica":"Mango",
    "Mentha":"Mint",
    "Moringa Oleifera":"Drumstick",
    "Muntingia Calabura":"Jamaica Cherry-Gasagase",
    "Murraya Koenigii":"Curry",
    "Nerium Oleander":"Oleander",
    "Nyctanthes Arbor-tristis":"Parijata",
    "Ocimum Tenuiflorum":"Tulsi",
    "Piper Betle":"Betel",
    "Plectranthus Amboinicus":"Mexican Mint",
    "Pongamia Pinnata":"Indian Beech",
    "Psidium Guajava":"Guava",
    "Punica Granatum":"Pomegranate",
    "Santalum Album":"Sandalwood",
    "Syzygium Cumini":"Jamun",
    "Syzygium Jambos":"Rose Apple",
    "Tabernaemontana Divaricata":"Crape Jasmine",
    "Trigonella Foenum-graecum":"Fenugreek"

    }
    if name in d:
        st.write("The common name is:", d[name])
