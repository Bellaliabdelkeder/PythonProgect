def swith():
    def tb(decimal):
        return bin(decimal)[2:]

    def td(binary):
        return int(binary, 2)

    def too(decimal):
        return oct(decimal)[2:]

    def th(decimal):
        return hex(decimal)[2:]

    def convert(number, fb, tbb):
        if fb == "decimal":
            decimal_number = number
        elif fb == "binary":
            decimal_number = td(number)
        elif fb == "octal":
            decimal_number = int(number, 8)
        elif fb == "hexadecimal":
            decimal_number = int(number, 16)
        
        if tbb == "binary":
            return tb(decimal_number)
        elif tbb == "decimal":
            return decimal_number
        elif tbb == "octal":
            return too(decimal_number)
        elif tbb == "hexadecimal":
            return th(decimal_number)

    def get_user_input():
        print('///////////////////////////////////////////////////////////////////////////////////')
        print("Choose the base you want to convert from:")
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        print("4. Hexadecimal")
        print('///////////////////////////////////////////////////////////////////////////////////')
        fb_choice = input("Enter your choice (1/2/3/4): ")
        
        number = input("Enter the number you want to convert: ")
        print('///////////////////////////////////////////////////////////////////////////////////')
        print("Choose the base you want to convert to:")
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        print("4. Hexadecimal")
        print('///////////////////////////////////////////////////////////////////////////////////')
        tbb_choice = input("Enter your choice (1/2/3/4): ")
        
    
        base_map = {"1": "decimal", "2": "binary", "3": "octal", "4": "hexadecimal"}
        fb = base_map[fb_choice]
        tbb = base_map[tbb_choice]
        
        
        result = convert(number, fb, tbb)
        print(f"Converted {number} from {fb} to {tbb}: {result}")


    get_user_input()
