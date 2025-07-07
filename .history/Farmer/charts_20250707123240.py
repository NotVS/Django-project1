import matplotlib.pyplot as plt
from .models import Farmer, Crop

def generate_farmer_charts():
    farmers = Farmer.objects.all()
    
    for farmer in farmers:
        crops = Crop.objects.filter(farmer = farmer)
        if not crops:
            continue
    
        crop_types = 
        