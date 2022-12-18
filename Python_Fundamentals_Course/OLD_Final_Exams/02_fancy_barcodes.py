<<<<<<< HEAD
import re

barcodes_count = int(input())

for barcode in range(barcodes_count):
    text = input()

    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])\1'
    result = re.findall(pattern, text)

    current_product_group = ''
    if result:
        temporary = str(result[0][1])
        for character in temporary:
            if character.isdigit():
                current_product_group += character
        if len(current_product_group) > 0:
            print(f"Product group: {current_product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")

=======
import re

barcodes_count = int(input())

for barcode in range(barcodes_count):
    text = input()

    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])\1'
    result = re.findall(pattern, text)

    current_product_group = ''
    if result:
        temporary = str(result[0][1])
        for character in temporary:
            if character.isdigit():
                current_product_group += character
        if len(current_product_group) > 0:
            print(f"Product group: {current_product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")

>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
