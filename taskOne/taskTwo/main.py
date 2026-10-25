from datetime import date
import  requests
barcode = 3033710065967 #3017624010701

while True:
    barcode = input ("barcode: ")
    url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}"
    response = requests.request.get(url, headers=headers)
    data = response.json()
    headers = {
        "User-Agent":"MyBarcodeApp/1.0 (ADD YOUR EMAIL)"
    }

    product_name = data.get("product", {}).get("product_name", "Product name not found")
    print (f"Product Name: {product_name}")

    def main():
        while True:


        
            if __name__=="__main__":
              main()