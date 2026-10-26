import  requests
def get_product_info(barcode):
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}"
    response = requests.get(url)
    data = response.json()
    nutriscore = data.get("product", {}).get("nutriscore_grade")
    ingredients = data.get("product", {}).get("ingredients_text_en", "Product name not found")
    product_name = data.get("product", {}).get("product_name", "Product name not found")
    status_check = data.get('status')

    product_info = {
        "name": product_name,
        "ingredients": ingredients,
        "nutrition_score": nutriscore,
        "status": status_check
    }
    return product_info

def main():
    default_barcode = 3017624010701
    product_info = get_product_info(default_barcode)
    while True:
        print("1. Nutriscore")
        print("2. Change barcode")
        print("3. Exit")
        user_input = input("Enter selection: ")
        if user_input == "1":
            print(f"\nProduct Name: {product_info['name']}")
            print(f"Ingredients: {product_info['ingredients']}")
            print(f"Nutrition Score: {product_info['nutrition_score'].upper()}")
            if product_info["nutrition_score"] == "a":
                print("Nutri-Score A: Healthy choice!")
            elif product_info["nutrition_score"] == "b":
                print("Nutri-Score B: Good choice")
            elif product_info["nutrition_score"] == "c":
                print("Nutri-Score C: Average choice")
            elif product_info["nutrition_score"] == "d":
                print("Nutri-Score D: Consume with care")
            elif product_info["nutrition_score"] == "e":
                print("Nutri-Score E: Consume in moderation")
            else:
                print("something went wrong")
        elif user_input == "2":
            new_barcode = input("Enter new barcode: ")
            product_info = get_product_info(new_barcode)
            if product_info["status"] == 0:
                print("Product not found")
                product_info = get_product_info(default_barcode)
            elif product_info["status"] == 1:
                print("\nProduct found")
        elif user_input == "3":
            print("Exit")
            break

           

if __name__ == "__main__":
    main()
