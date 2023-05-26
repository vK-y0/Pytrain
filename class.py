class C:
    pass

a = C()
print(dir(a))
a.couleur = "bleu"
print(dir(a))

class Cube:
    taille = 52152
    couleur = ""
    def affiche(self):
        self.taille = 130
        print(Cube.taille)
        print(self.taille)


newCube = Cube()
newCube.affiche()
