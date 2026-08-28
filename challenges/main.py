import sys

def is_valid_isbn_10(isbn):
    if len(isbn) != 10:
        return False

    total_sum = 0
    for i in range(10):
        char = isbn[i]
        if i < 9:
            if not char.isdigit():
                return False
            digit = int(char)
        else:  # Last character
            if char.isdigit():
                digit = int(char)
            elif char.upper() == 'X':
                digit = 10
            else:
                return False
        
        total_sum += (10 - i) * digit

    return total_sum % 11 == 0

isbn_string = sys.stdin.readline().strip()
print(is_valid_isbn_10(isbn_string))