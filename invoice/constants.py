class CompanyChoices:
    CATEGORY_TECH = 'TECH'
    CATEGORY_FINANCE = 'FIN'
    CATEGORY_HEALTH = 'HEALTH'
    CATEGORY_EDUCATION = 'EDU'

    COMPANY_CATEGORIES = [
        (CATEGORY_TECH, 'Technology'),
        (CATEGORY_FINANCE, 'Finance'),
        (CATEGORY_HEALTH, 'Health'),
        (CATEGORY_EDUCATION, 'Education'),
        ]
class ProductCategory:
    GROCERY = 'GROCERY'
    ELECTRONICS = 'ELECTRONICS'
    CLOTHING = 'CLOTHING'
    COSMETICS = 'COSMETICS'
    MEDICINES = 'MEDICINES'
    BOOKS = 'BOOKS'
    SPORTS = 'SPORTS'
    FURNITURE = 'FURNITURE'
    TOYS = 'TOYS'
    STATIONARY = 'STATIONARY'
    OTHERS = 'OTHERS'

    PRODUCT_CATEGORIES = [
        (GROCERY, 'Grocery'),
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (COSMETICS, 'Cosmetics'),
        (MEDICINES, 'Medicines'),
        (BOOKS, 'Books'),
        (SPORTS, 'Sports'),
        (FURNITURE, 'Furniture'),
        (TOYS, 'Toys'),
        (STATIONARY, 'Stationary'),
        (OTHERS, 'Others')
    ]
class InvoiceStatus:
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    CANCELLED = 'CANCELLED'
    PENDING = 'PENDING'

    INVOICE_STATUSES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending')
    ]
class PaymentMethod:
    CASH = 'CASH'
    CARD = 'CARD'
    NETBANKING = 'NETBANKING'
    UPI = 'UPI'
    WALLET = 'WALLET'

    PAYMENT_METHODS = [
        (CASH, 'Cash'),
        (CARD, 'Card'),
        (NETBANKING, 'Netbanking'),
        (UPI, 'UPI'),
        (WALLET, 'Wallet')
    ]
class OrderStatus:
    PLACED = 'PLACED'
    DISPATCHED = 'DISPATCHED'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'

    ORDER_STATUSES = [
        (PLACED, 'Placed'),
        (DISPATCHED, 'Dispatched'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled')
    ]
class PaymentStatus:
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    PENDING = 'PENDING'

    PAYMENT_STATUSES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (PENDING, 'Pending')
    ]
class PaymentType:        
    FULL = 'FULL'
    PARTIAL = 'PARTIAL'
    ADVANCE = 'ADVANCE'

    PAYMENT_TYPES = [
        (FULL, 'Full'),
        (PARTIAL, 'Partial'),
        (ADVANCE, 'Advance')
    ]

