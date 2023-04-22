

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
        
        result = (M / (H * H))* 703
        return result
    
    
    def bmi_kg_meter(self):
        
        H = self.height
        M = self.mass
        
        return float(M / H)
        