import  requests
def get_product_info(barcode):
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}"
    response = requests.get(url)
    data = response.json()
    product = data.get('product', {})
    nutriments = product.get('nutriments', {})

    def nutrient_per_100g(nutrient_key):
        value = nutriments.get(f'{nutrient_key}_100g')
        if value is None:
            return 'Not available'
        unit = nutriments.get(f'{nutrient_key}_unit', '')
        return f'{value} {unit} per 100 g'.strip()

    nutriscore = product.get('nutriscore_grade')
    ingredients = product.get('ingredients_text_en', 'product name not found')
    product_name = product.get('product_name', 'product name not found')
    iron = nutrient_per_100g('iron')
    magnesium = nutrient_per_100g('magnesium')
    phosphorus = nutrient_per_100g('phosphorus')
    protein = nutrient_per_100g('proteins')
    sodium = nutrient_per_100g('sodium')
    saturated_fat = nutrient_per_100g('saturated-fat')
    selenium = nutrient_per_100g('selenium')
    vitamin_a = nutrient_per_100g('vitamin-a')
    vitamin_c = nutrient_per_100g('vitamin-c')
    vitamin_e = nutrient_per_100g('vitamin-e')
    vitamin_k = nutrient_per_100g('vitamin-k')
    zinc = nutrient_per_100g('zinc')
    status_check = data.get('status')

    product_info = {
        'name': product_name,
        'ingredients': ingredients,
        'nutrition_score': nutriscore,
        'iron': iron,
        'magnesium': magnesium,
        'phosphorus': phosphorus,
        'protein': protein,
        'sodium': sodium,
        'saturated_fat': saturated_fat,
        'selenium': selenium,
        'vitamin_a': vitamin_a,
        'vitamin_c': vitamin_c,
        'vitamin_e': vitamin_e,
        'vitamin_k': vitamin_k,
        'zinc': zinc,
        'status': status_check
    }
    return product_info

def main():
    default_barcode = 3017624010701
    product_info = get_product_info(default_barcode)
    while True:
        print('1. Nutriscore')
        print('2. Change barcode')
        print('3: Nutrient information')
        print('4: Exit')
        user_input = input('Enter selection: ')
        if user_input == '1':
            print(f"\nProduct Name: {product_info['name']}")
            print(f"Ingredients: {product_info['ingredients']}")
            nutrition_score = product_info['nutrition_score']
            if nutrition_score:
                print(f"Nutrition Score: {nutrition_score.upper()}")
            else:
                print("Nutrition Score: Not available")
            if product_info['nutrition_score'] == 'a':
                print('Nutri-Score A: Healthy choice!')
            elif product_info['nutrition_score'] == 'b':
                print('Nutri-Score B: Good choice')
            elif product_info['nutrition_score'] == 'c':
                print('Nutri-Score C: Average choice')
            elif product_info['nutrition_score'] == 'd':
                print('Nutri-Score D: Consume with care')
            elif product_info['nutrition_score'] == "e":
                print('Nutri-Score E: Consume in moderation')
            else:
                print('something went wrong')
        elif user_input == "2":
            new_barcode = input('Enter new barcode: ')
            product_info = get_product_info(new_barcode)
            if product_info['status'] == 0:
                print('Product not found')
                product_info = get_product_info(default_barcode)
            elif product_info['status'] == 1:
                print('\nProduct found')
                print(f"product is \"{product_info['name']}\"")
        elif user_input == '3':
            print("\nNutrient values per 100 g:")
            print(f"Iron: {product_info['iron']}")
            print(f"Magnesium: {product_info['magnesium']}")
            print(f"Phosphorus: {product_info['phosphorus']}")
            print(f"Protein: {product_info['protein']}")
            print(f"Sodium: {product_info['sodium']}")
            print(f"Saturated fat: {product_info['saturated_fat']}")
            print(f"Selenium: {product_info['selenium']}")
            print(f"Vitamin A: {product_info['vitamin_a']}")
            print(f"Vitamin C: {product_info['vitamin_c']}")
            print(f"Vitamin E: {product_info['vitamin_e']}")
            print(f"Vitamin K: {product_info['vitamin_k']}")
            print(f"Zinc: {product_info['zinc']}")
        elif user_input == '4':
            print('Exiting')
            break
        else:
            print('invalid input')

           

if __name__ == "__main__":
    main()
