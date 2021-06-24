    class SuperChaine(object):
        def __init__(self, texte):
    	self.texte = texte
     
        def majuscule(self):
    	return self.texte.upper()
     
        def minuscule(self):
    	return self.texte.lower()
     
        def titre(self):
    	return self.texte.capitalize()
     
    chaine = SuperChaine("udemy")
    print(chaine.majuscule())
    print(chaine.minuscule())
    print(chaine.titre())
