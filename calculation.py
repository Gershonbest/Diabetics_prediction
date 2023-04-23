

class body_mass_index():
    def __init__(self, mass, height) -> None:
        self.mass = mass 
        self.height = height 
        
        
        
    def bmi_pounds_inch(self):
        
        """
        A function to calculate the body mass index BMI
        using 
        """
        
        H = self.height
        M = self.mass
        
        height = float(H)/100
        mass = float(M)
        result = round((mass / (height * height))* 703,2)
        return result
    
    
    def bmi_kg_meter(self):
        
        H = self.height
        M = self.mass
        mass = float(M)
        height = float(H)
        return round(float(mass / (height*height)),2)
        