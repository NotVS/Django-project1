import matplotlib.pyplot as plt
from .models import Farmer, Crop

def generate_farmer_charts():
    farmers = Farmer.objects.all()
    
    for farmer in farmers:
        crops = Crop.objects.filter(farmer = farmer)
        
        if not crops:
            continue
    
        crop_types = [crop.crop_type for crop in crops]
        areas = [crop.area for crop in crops]
        prices = [crop.price_per_m2 for crop in crops]
        
        # bar chart - crop areas
        
        plt.figure(figsize = (10, 6))
        plt.title(f"Areas of Land for Each Crop - {farmer.first_name}")
        
        plt.bar(crop_types, areas, color = 'green')
        plt.xlabel("Crop Type")
        plt.ylabel("Area of Land (m²)")
        
        
        plt.tight_layout()
        
        