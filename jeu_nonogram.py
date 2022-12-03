from img_converter_uniforme_output import Pixelisation, Conversion_noir_blanc, Grille_blanche

nom_fichier = "test2.png"
taille_image = 300
pixels = 21

img, moy = Pixelisation(pixels, taille_image, True, nom_fichier)

img = Conversion_noir_blanc(img, moy, pixels, taille_image, True, nom_fichier)

Grille_blanche(moy, pixels, taille_image, True, nom_fichier)
