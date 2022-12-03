from PIL import Image

if __name__ == "__main__":
    choix_img = input("Saisir le nom et l'extension de l'image\nRéponse : ")
    img = Image.open(choix_img)
    print("")

    taille_finale = int(input("Choisi une taille multiple de 3 entre 3 et 600\nRéponse : "))
    print("")

    uniforme_taille = 300
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
    img.save("output/output_"+str(taille_finale)+"pixels_"+choix_img)
    print("Nom de l'image : output_"+str(taille_finale)+"pixels_"+choix_img+"\n")

else:
    def Pixelisation(taille_multiple_3, uniforme_taille = 300, enregistrer = False, nom_fichier = "input.png"):
        """Pixelisation(nom_fichier, taille_multiple_3) est une fonction qui prend en paramètre un nom de fichier avec son extension, une taille avec laquelle l'image sera pixelisée (max uniforme_taille/2),
        une taille uniforme_taille qui sera la taille de l'image output (doit être une puissance de 3, 300 reccomandé) et un boléen si on veut l'enregistrer.
        La taille doit être un multiple de trois pour le jeux. La fonction retourne l'image modifié qui peut être enregistrée et une liste de chaque moyenne."""
        
        img = Image.open(nom_fichier)

        l_moyenne = []

        uniforme_taille_divise = int(uniforme_taille/taille_multiple_3)

        img = img.resize((uniforme_taille, uniforme_taille), Image.ANTIALIAS)

        pixels = img.load()

        if taille_multiple_3 == 9:
            problem_fixe = 3
        else:
            problem_fixe = 0

        for y in range(taille_multiple_3):
            for x in range(taille_multiple_3):
                moy_r = 0
                moy_g = 0
                moy_b = 0

                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x + problem_fixe):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y + problem_fixe):
                        moy_r += pixels[i,j][0]
                        moy_g += pixels[i,j][1]
                        moy_b += pixels[i,j][2]

                moy_r = int(moy_r / uniforme_taille_divise ** 2)
                moy_g = int(moy_g / uniforme_taille_divise ** 2)
                moy_b = int(moy_b / uniforme_taille_divise ** 2)

                moyenne = (moy_r, moy_g, moy_b)

                l_moyenne.append(moyenne)

                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x + problem_fixe):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y + problem_fixe):
                        pixels[i,j] = moyenne

        if enregistrer == True:
            img.save("output/output_"+str(taille_multiple_3)+"pixels_"+nom_fichier)
            
        return img, l_moyenne


    def Conversion_noir_blanc(img, l_moyenne, taille_multiple_3, uniforme_taille = 300, enregistrer = False, nom_fichier = "output_black_white"):
        pixels = img.load()
        
        uniforme_taille_divise = int(uniforme_taille/taille_multiple_3)

        moyenne_toute_r = 0
        moyenne_toute_g = 0
        moyenne_toute_b = 0
        for i in l_moyenne:
            moyenne_toute_r += i[0]
            moyenne_toute_g += i[1]
            moyenne_toute_b += i[2]
        moyenne_toute_r = int(moyenne_toute_r / (taille_multiple_3 ** 2))
        moyenne_toute_g = int(moyenne_toute_g / (taille_multiple_3 ** 2))
        moyenne_toute_b = int(moyenne_toute_b / (taille_multiple_3 ** 2))

        if taille_multiple_3 == 9:
            problem_fixe = 3
        else:
            problem_fixe = 0
        
        for y in range(taille_multiple_3):
            for x in range(taille_multiple_3):
                couleur_pixel = l_moyenne[y*taille_multiple_3 + x]
                if couleur_pixel[0] >= moyenne_toute_r or couleur_pixel[1] >= moyenne_toute_g or couleur_pixel[2] >= moyenne_toute_b:
                    noir_ou_blanc = (0, 0, 0)
                else:
                    noir_ou_blanc = (255, 255, 255)
                
                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x + problem_fixe):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y + problem_fixe):
                        pixels[i,j] = noir_ou_blanc

        if enregistrer == True:
            img.save("output/output_bw_"+str(taille_multiple_3)+"pixels_"+nom_fichier)

        return img

    def Grille_blanche(l_moyenne, taille_multiple_3, uniforme_taille = 300, enregistrer = False, nom_fichier = "output_white"):
        uniforme_taille_divise = int(uniforme_taille/taille_multiple_3)

        img = Image.new('RGB', (uniforme_taille, uniforme_taille), color = 'white')

        pixels = img.load()

        if taille_multiple_3 == 9:
            problem_fixe = 3
        else:
            problem_fixe = 0

        for y in range(taille_multiple_3):
            for x in range(taille_multiple_3):
                for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x + problem_fixe):
                    for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y + problem_fixe):
                        if i == uniforme_taille_divise*x or j == uniforme_taille_divise*y:
                            pixels[i,j] = (0, 0, 0)

        if enregistrer == True:
            img.save("output/output_w_"+str(taille_multiple_3)+"pixels_"+nom_fichier)

        return img


