# src/configs/config_modules/db_default_data.py

DEFAULT_CATEGORIES = [
    {"name": "Housing", "subcategories": [
        {"name": "Utilities", "subcategories": ["Electricity", "Heating", "Propane"]},
        {"name": "Maintenance", "subcategories": ["Repairs", "Lawn Care", "Snow Removal", "Home Improvement"]},
    ]},
    {"name": "Transportation", "subcategories": [
        {"name": "Vehicle", "subcategories": ["Fuel", "Maintenance & Repairs", "Registration/License", "Annual Inspection"]},
        {"name": "Ride-Sharing", "subcategories": ["Rental", "Taxis"]},
        {"name": "Parking & Tolls", "subcategories": []}
    ]},
    {"name": "Household Expenses", "subcategories": [
        {"name": "Groceries", "subcategories": []},
        {"name": "Furniture", "subcategories": []},
        {"name": "Dining Out", "subcategories": ["Restaurants", "Takeout/Delivery", "Coffee Shops"]}
    ]},
    {"name": "Health and Medical", "subcategories": [
        {"name": "Health Insurance", "subcategories": ["Premiums"]},
        {"name": "Medical Expenses", "subcategories": ["Doctor Visits", "Medications", "Dental Care", "Eye Care", "Hospital Fees", "Medical Marijuana"]},
        {"name": "Fitness", "subcategories": ["Gym Membership", "Exercise Equipment", "Fitness Classes"]}
    ]},
    {"name": "Personal Care", "subcategories": [
        {"name": "Hair Care", "subcategories": []},
        {"name": "Salon", "subcategories": []}
    ]},
    {"name": "Education", "subcategories": [
        {"name": "Education", "subcategories": ["School Supplies", "Tuition", "Textbooks", "Extracurricular Activities"]}
    ]},
    {"name": "Entertainment and Recreation", "subcategories": [
        {"name": "Streaming Services", "subcategories": []},
        {"name": "Mobile Devices", "subcategories": []},
        {"name": "Recreational Substances", "subcategories": ["Alcohol", "Cigars", "Marijuana"]},
        {"name": "Hobbies", "subcategories": ["Books", "Video Games", "Sports Equipment", "Music"]},
        {"name": "Vacations", "subcategories": ["Travel Expenses", "Hotel Accommodations", "Activities"]}
    ]},
    {"name": "Clothing", "subcategories": [
        {"name": "Work Clothing", "subcategories": []},
        {"name": "Casual Wear", "subcategories": []},
        {"name": "Shoes", "subcategories": []},
        {"name": "Accessories", "subcategories": []}
    ]},
    {"name": "Insurance", "subcategories": [
        {"name": "Health Insurance", "subcategories": []},
        {"name": "Life Insurance", "subcategories": []},
        {"name": "Home Insurance", "subcategories": []},
        {"name": "Auto Insurance", "subcategories": []},
        {"name": "Disability Insurance", "subcategories": []}
    ]},
    {"name": "Debt Repayment", "subcategories": [
        {"name": "Credit Cards", "subcategories": ["Interest Payments", "Principal Payments"]},
        {"name": "Loans", "subcategories": ["Student Loans", "Personal Loans", "Auto Loans", "Mortgage", "Consumer Proposal"]}
    ]},
    {"name": "Savings and Investments", "subcategories": [
        {"name": "Emergency Fund", "subcategories": []},
        {"name": "Retirement Savings", "subcategories": []},
        {"name": "Investment Accounts", "subcategories": []}
    ]},
    {"name": "Gifts and Donations", "subcategories": [
        {"name": "Gifts", "subcategories": ["Birthday", "Holiday Gifts", "Wedding Gifts", "Other"]},
        {"name": "Charity", "subcategories": ["Donations", "Volunteering"]}
    ]},
    {"name": "Taxes", "subcategories": [
        {"name": "Income Tax", "subcategories": []},
        {"name": "Property Tax", "subcategories": []},
        {"name": "Sales Tax", "subcategories": []}
    ]},
    {"name": "Business Expenses", "subcategories": [
        {"name": "Inventory", "subcategories": []},
        {"name": "Office Supplies", "subcategories": []},
        {"name": "Taxes", "subcategories": []},
        {"name": "Professional Services", "subcategories": ["Accounting", "Legal"]},
        {"name": "Marketing", "subcategories": ["Advertising", "Promotions"]}
    ]},
    {"name": "Miscellaneous", "subcategories": [
        {"name": "Pet Expenses", "subcategories": ["Food", "Grooming","Vet Bills", "Supplies"]},
        {"name": "Bank Fees", "subcategories": []},
        {"name": "Postage", "subcategories": []}
    ]}
]

DEFAULT_FREQUENCIES = [
    "One-time",
    "Weekly",
    "Bi-Weekly",
    "Bi-Monthly",
    "Monthly",
    "Semi-Monthly",
    "Quarterly",
    "Annually"
]
