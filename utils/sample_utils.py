def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount

    return round(final_price, 2)


if __name__ == "__main__":
    price = 100
    discount = 10
    print(f"Final price after {discount}% discount:", calculate_discount(price, discount))