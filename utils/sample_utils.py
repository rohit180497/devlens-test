def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount

    return round(final_price, 2)

def calculate_tax(price, tax_percent):
    """
    Calculate the final price after applying tax.
    """
    if tax_percent < 0:
        raise ValueError("Tax percent cannot be negative")

    tax_amount = price * (tax_percent / 100)
    final_price = price + tax_amount

    return round(final_price, 2)

if __name__ == "__main__":
    price = 100
    discount = 10
    tax = 8

    discounted_price = calculate_discount(price, discount)
    final_price = calculate_tax(discounted_price, tax)

    print(f"Price after {discount}% discount:", discounted_price)
    print(f"Final price after {tax}% tax:", final_price)
    print(f"Final price after {discount}% discount and {tax}% tax:", calculate_tax(calculate_discount(price, discount), tax))