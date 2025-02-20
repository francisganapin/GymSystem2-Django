from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps



@receiver(post_migrate)
def create_default_sale(sender,**kwargs):
    if sender.name != 'function.sale_function':
        return

    Product = apps.get_model('sale_function','Product')


    product_list = [
            {
                "name": "Whey Protein",
                "description": "High-quality whey protein to support muscle recovery.",
                "price": 1500.00,
                "stock": 50
            },
            {
                "name": "Creatine Monohydrate",
                "description": "Boosts strength and performance during workouts.",
                "price": 800.00,
                "stock": 40
            },
            {
                "name": "BCAA Powder",
                "description": "Branched-chain amino acids for improved endurance.",
                "price": 1200.00,
                "stock": 30
            },
            {
                "name": "Mass Gainer",
                "description": "Calorie-dense formula for muscle mass increase.",
                "price": 1800.00,
                "stock": 20
            },
            {
                "name": "Pre-Workout",
                "description": "Energy-boosting formula for intense workouts.",
                "price": 950.00,
                "stock": 25
            },
            {
                "name": "Electrolyte Drink",
                "description": "Replenishes lost electrolytes during exercise.",
                "price": 100.00,
                "stock": 60
            },
            {
                "name": "Glutamine Powder",
                "description": "Supports muscle recovery and reduces soreness.",
                "price": 700.00,
                "stock": 15
            },
            {
                "name": "Fish Oil Capsules",
                "description": "Rich in Omega-3 fatty acids for joint support.",
                "price": 500.00,
                "stock": 35
            },
            {
                "name": "Multivitamins",
                "description": "Daily vitamins to support overall health.",
                "price": 450.00,
                "stock": 45
            },
            {
                "name": "L-Carnitine Liquid",
                "description": "Helps in fat metabolism and energy production.",
                "price": 850.00,
                "stock": 20
            },
            {
                "name": "Beta-Alanine",
                "description": "Improves endurance and reduces fatigue.",
                "price": 750.00,
                "stock": 10
            },
            {
                "name": "Casein Protein",
                "description": "Slow-digesting protein for overnight recovery.",
                "price": 1600.00,
                "stock": 25
            },
            {
                "name": "Energy Bars",
                "description": "Convenient snack to fuel workouts.",
                "price": 80.00,
                "stock": 100
            },
            {
                "name": "Protein Cookies",
                "description": "High-protein snacks to curb cravings.",
                "price": 120.00,
                "stock": 75
            },
            {
                "name": "ZMA Capsules",
                "description": "Supports recovery and improves sleep quality.",
                "price": 600.00,
                "stock": 30
            },
            {
                "name": "Caffeine Pills",
                "description": "Boosts energy and focus for workouts.",
                "price": 250.00,
                "stock": 50
            },
            {
                "name": "HMB Capsules",
                "description": "Helps in muscle preservation during training.",
                "price": 950.00,
                "stock": 20
            },
            {
                "name": "Protein Pancake Mix",
                "description": "Quick and healthy breakfast option.",
                "price": 500.00,
                "stock": 40
            },
            {
                "name": "Amino Energy Drink",
                "description": "Combines aminos and caffeine for workout energy.",
                "price": 130.00,
                "stock": 60
            },
            {
                "name": "Vitamin D3 Capsules",
                "description": "Supports bone health and immune function.",
                "price": 300.00,
                "stock": 50
            },
            {
                "name": "Magnesium Tablets",
                "description": "Aids in muscle function and reduces cramps.",
                "price": 280.00,
                "stock": 35
            },
            {
                "name": "Joint Support Capsules",
                "description": "Promotes joint flexibility and mobility.",
                "price": 700.00,
                "stock": 20
            },
            {
                "name": "Green Tea Extract",
                "description": "Natural metabolism booster.",
                "price": 400.00,
                "stock": 45
            },
            {
                "name": "Electrolyte Tablets",
                "description": "Easy-to-carry electrolyte replenishment.",
                "price": 150.00,
                "stock": 70
            },
            {
                "name": "Hydration Packets",
                "description": "Quick hydration solution for athletes.",
                "price": 200.00,
                "stock": 55
            }
            ]



    for data in product_list:
        Product.objects.get_or_create(
            name=data['name'],
            defaults={
                'description':data['description'],
                'price':data['price'],
                'stock':data['stock']
            }
        )