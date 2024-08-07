import numpy as np
import pandas as pd
import streamlit as st
from distances import retrieve_similar_images
from fonctions import extract_features
import os
import matplotlib.pyplot as plt



descriptlist = ['Choisir descripteur','glcm','bitdesc','haralick','glcm_bitdesc','haralick_bitdesc']
distanceslist=['canberra','chebyshev','manhattan','euclidean']



def main():
    st.header("MT Image Search \U0001F600")
    st.write('-------------------------------------------------------------------')

    filename=st.sidebar.file_uploader(label='Telecharger votre image ici')
    
        
    if filename is not None:
        
        descripteur=st.sidebar.selectbox('Choix du descripteur',descriptlist)
        distances=st.sidebar.selectbox('Choix de la distance',distanceslist)
        
        
        Signatures=''
        if descripteur == 'glcm': 
            # Load offline Signature
            Signatures=np.load('glcm_signatures.npy')
        elif descripteur == 'bitdesc': 
            # Load offline Signature
            Signatures=np.load('bitdesc_signatures.npy')
        elif descripteur == 'haralick': 
            # Load offline Signature
            Signatures=np.load('haralick_signatures.npy')
        elif descripteur == 'glcm_bitdesc': 
            # Load offline Signature
            Signatures=np.load('glcm_bitdesc_signatures.npy')
        elif descripteur == 'haralick_bitdesc':  
            # Load offline Signature
            Signatures=np.load('haralick_bitdesc_signatures.npy')
            
        # Définissez un chemin de fichier temporaire pour l'image téléchargée
        temporary_file_path = "uploaded_image.jpg"  # Vous pouvez personnaliser le nom du fichier temporaire

        # Écrivez l'image téléchargée sur le disque
        with open(temporary_file_path, "wb") as f:
            f.write(filename.read())
        
        # Passez le chemin de fichier temporaire à extract_features
        features = extract_features(temporary_file_path, descripteur)
        nbr=st.sidebar.slider(label="Nombre Images", value=100)
        result = retrieve_similar_images(features_db=Signatures, query_features=features, distance=distances, num_results=nbr)
        col1,col2=st.columns(2)
        st.write('-------------------------------------------------------------------')
        with col1:
            
            st.image(filename,width=300)
            st.write('-------------------Image a chercher-------------------')
        with col2:
            # Compter le nombre d'images par catégorie
            categories_count = {}
            for result_item in result:
                category = result_item[1]
                if category in categories_count:
                    categories_count[category] += 1
                else:
                    categories_count[category] = 1

            # Créer un histogramme
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(categories_count.keys(), categories_count.values())
            ax.set_xlabel('Catégorie')
            ax.set_ylabel('Nombre d\'images')
            ax.set_title('Nombre d\'images par catégorie')
            plt.xticks(rotation=45) 
            # Afficher l'histogramme dans Streamlit
            st.pyplot(fig)
            st.write('------------------------Histogramme------------------------')
        st.subheader('--------------------------Affichage resultat-----------------------------')
        st.write('-------------------------------------------------------------------')
        
       # Affichage des images retournées en lignes de trois images chacune
        for i in range(0, len(result), 3):
            # Créer une nouvelle ligne pour afficher les images
            col1, col2, col3 = st.columns(3)
            for j in range(3):
                # Vérifier si l'index est valide dans la liste des résultats
                if i + j < len(result):
                    with eval(f"col{j+1}"):
                        st.image(result[i + j][2], width=200)
                        st.write(result[i + j][1])

       
        
            

       
        
        #print(f'Results:\n--------------------------------\n {result}')

        # Nettoyez le fichier temporaire 
        os.remove(temporary_file_path)

            
       
        
    
if __name__ == '__main__':
    main()
    
    