from PIL import Image

if __name__ == "__main__":
    choix_img = input("Saisir le nom et l'extension de l'image\nRéponse : ")
    img = Image.open(choix_img)
    print("")

    taille_finale = int(input("Choisi une taille multiple de 3 entre 3 et 600\nRéponse : "))
    print("")

    uniforme_taille = 1200
    uniforme_taille_divise = int(uniforme_taille/taille_finale)
    new_width  = uniforme_taille
    new_height = uniforme_taille

    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    pixels = img.load()

    for x in range(taille_finale):
        for y in range(taille_finale):
            moy_r = 0
            moy_g = 0
            moy_b = 0

            for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x):
                for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y):
                    moy_r += pixels[i,j][0]
                    moy_g += pixels[i,j][1]
                    moy_b += pixels[i,j][2]

            moy_r = int(moy_r / uniforme_taille_divise ** 2)
            moy_g = int(moy_g / uniforme_taille_divise ** 2)
            moy_b = int(moy_b / uniforme_taille_divise ** 2)

            for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x):
                for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y):
                    pixels[i,j] = (moy_r, moy_g, moy_b)

    print("Processing ...\n")
    img.show()
    img.save("output_"+choix_img)
    print("Nom de l'image : output_"+choix_img+"\n")

else:
    def Pixelisation(nom_fichier, taille_multiple_3, enregistrer = False):
        """Pixelisation(nom_fichier, taille_multiple_3) est une fonction qui prend en paramètre un nom de fichier avec son extension, une taille avec laquelle l'image sera pixelisée (max 150) et un boléen si on veut l'enregistrer.
        La taille doit être un multiple de trois pour le jeux. La fonction retourne l'image modifié qui peut être enregistrée et une liste de chaque moyenne."""
        
        img = Image.open(nom_fichier)

        l_moyenne = []

        uniforme_taille = 300
        uniforme_taille_divise = int(uniforme_taille/taille_multiple_3)

        img = img.resize((uniforme_taille, uniforme_taille), Image.ANTIALIAS)

        pixels = img.load()

        for y in range(taille_multiple_3):
            for x in range(taille_multiple_3):
                moy_r = 0
                moy_g = 0
                moy_b = 0

                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y):
                        moy_r += pixels[i,j][0]
                        moy_g += pixels[i,j][1]
                        moy_b += pixels[i,j][2]

                moy_r = int(moy_r / uniforme_taille_divise ** 2)
                moy_g = int(moy_g / uniforme_taille_divise ** 2)
                moy_b = int(moy_b / uniforme_taille_divise ** 2)

                moyenne = (moy_r, moy_g, moy_b)

                l_moyenne.append(moyenne)

                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y):
                        pixels[i,j] = moyenne

        if enregistrer == True:
            img.save("output_"+nom_fichier)
            
        return img, l_moyenne
