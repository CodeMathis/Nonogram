from img_converter_uniforme_output import Pixelisation
from img_converter_black_white import Conversion_noir_blanc

nom_fichier = "test3.png"

img, moy = Pixelisation(nom_fichier, 9, 300, True)

Conversion_noir_blanc(img, moy, 9, 300, True, nom_fichier)
