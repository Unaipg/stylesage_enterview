import pandas as pd
from decorators import timer

@timer()
def get_most_expensive(data: any, *args, sorted: bool = False, qty: int = 10, **kwargs) -> any:
    """Sort if needed by price and return the most expensive"""
    if not sorted:
        data = data.sort_values('_current_price_value')
    return data.tail(qty)

@timer()
def get_cheaper(data: any, *args, sorted: bool = False, qty: int = 10, **kwargs) -> any:
    """Sort if needed by price and return the cheaper"""
    if not sorted:
        data = data.sort_values('_current_price_value')
    return data.head(qty)

@timer()
def get_most_discounted(data: any, *args, qty: int = 10, **kwargs) -> any:
    """Calculate the discount per product and return the most discounted"""
    data['discount'] = data['_original_price_value'] - data['_current_price_value']
    return data.sort_values('discount', ascending=False).head(qty)

@timer()
def count_by_regex(data: any, regex: str, *args, **kwargs) -> int:
    data['red'] = data.color_name.str.contains(regex, case=False, na=False)
    return data[data['red']].count()[0]

if __name__ == '__main__':
    data = pd.read_csv('products/products.csv')
    print(get_most_expensive(data))
    print(get_cheaper(data, message='. Sorted again to test the standalone performance'))
    print(get_most_discounted(data))
    print(count_by_regex(data, r'\bred'))
