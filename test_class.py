class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe Duree"""
        self.min=min
        self.sec=sec
    def __str__(self):
        """Display the objects"""
        return "{0:02}:{1:02}".format(self.min,self.sec)
    def __add__(self, i):
        """The object to add is an integer which is a number of seconds"""
        new_value=Duree()
        new_value.min=self.min
        new_value.sec=self.sec
        new_value.sec+=i
        if new_value.sec>60
            new_value.min+=//60
            new_value.sec=new_value.sec%60
        return new_value
"""now doing duree+54 will work even if 54 is an int"""

