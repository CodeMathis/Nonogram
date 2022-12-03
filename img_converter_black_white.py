from PIL import Image

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
    
    for y in range(taille_multiple_3):
        for x in range(taille_multiple_3):
            couleur_pixel = l_moyenne[y*taille_multiple_3 + x]
            if couleur_pixel[0] >= moyenne_toute_r or couleur_pixel[1] >= moyenne_toute_g or couleur_pixel[2] >= moyenne_toute_b:
                noir_ou_blanc = (0, 0, 0)
            else:
                noir_ou_blanc = (255, 255, 255)
            
            for i in range(uniforme_taille_divise*x , uniforme_taille_divise + uniforme_taille_divise*x):
                for j in range(uniforme_taille_divise*y, uniforme_taille_divise + uniforme_taille_divise*y):
                    pixels[i,j] = noir_ou_blanc

    if enregistrer == True:
        img.save("output/output_bw_"+str(taille_multiple_3)+"pixels_"+nom_fichier)

    return img
