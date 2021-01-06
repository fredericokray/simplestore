# All the API views functions are defined here
# The functions here expands the 'core' functions of the application, to simplify the use
# All views call the 'core' functions with different parameters
# The views names are intuitive according to their function

from modelsfuncs import get_json_table_rows, save_json_table_rows, update_json_tables_rows, delete_json_table_rows, \
    get_json_table_by_date


def get_sales(values):
    table = "Sales"
    return get_json_table_rows(table, values)


def save_sale(sales):
    table = "Sales"
    return save_json_table_rows(sales, table)


def update_sale(sales):
    table = "Sales"
    return update_json_tables_rows(sales, table)


def delete_sale(values):
    table = "Sales"
    return delete_json_table_rows(values, table)


def get_sale_by_date(dates, interval):
    table = "Sales"
    return get_json_table_by_date(interval, dates, table)


def get_purchases(values):
    table = "Purchases"
    return get_json_table_rows(table, values)


def save_purchases(purchases):
    table = "Purchases"
    return save_json_table_rows(purchases, table)


def update_purchases(purchases):
    table = "Purchases"
    return update_json_tables_rows(purchases, table)


def delete_purchases(values):
    table = "Purchases"
    return delete_json_table_rows(values, table)


def get_purchases_by_date(interval, dates):
    table = "Purchases"
    return get_json_table_by_date(interval, dates, table)


def get_customers(values):
    table = "Customers"
    return get_json_table_rows(table, values)


def save_customers(customers):
    table = "Customers"
    return save_json_table_rows(customers, table)


def update_customers(customers):
    table = "Customers"
    return update_json_tables_rows(customers, table)


def delete_customers(values):
    table = "Customers"
    return delete_json_table_rows(values, table)


def get_employees(values):
    table = "Employees"
    return get_json_table_rows(table, values)


def save_employees(employees):
    table = "Employees"
    return save_json_table_rows(employees, table)


def update_employees(employees):
    table = "Employees"
    return update_json_tables_rows(employees, table)


def delete_employees(values):
    table = "Employees"
    return delete_json_table_rows(values, table)


def get_suppliers(values):
    table = "Suppliers"
    return get_json_table_rows(table, values)


def save_suppliers(suppliers):
    table = "Suppliers"
    return save_json_table_rows(suppliers, table)


def update_suppliers(suppliers):
    table = "Suppliers"
    return update_json_tables_rows(suppliers, table)


def delete_suppliers(values):
    table = "Suppliers"
    return delete_json_table_rows(values, table)


def get_products(values):
    table = "Products"
    return get_json_table_rows(table, values)


def save_products(products):
    table = "Products"
    return save_json_table_rows(products, table)


def update_products(products):
    table = "Products"
    return update_json_tables_rows(products, table)


def delete_products(values):
    table = "Products"
    return delete_json_table_rows(values, table)


def get_services(values):
    table = "Services"
    return get_json_table_rows(table, values)


def save_services(services):
    table = "Services"
    return save_json_table_rows(services, table)


def update_services(services):
    table = "Services"
    return update_json_tables_rows(services, table)


def delete_services(values):
    table = "Services"
    return delete_json_table_rows(values, table)


def get_payments(values):
    table = "Payments"
    return get_json_table_rows(table, values)


def save_payments(payments):
    table = "Payments"
    print(payments)
    return save_json_table_rows(payments, table)


def update_payments(payments):
    table = "Payments"
    return update_json_tables_rows(payments, table)


def delete_payments(values):
    table = "Payments"
    return delete_json_table_rows(values, table)


def get_payments_by_date(interval, dates):
    table = "Payments"
    return get_json_table_by_date(interval, dates, table)


def get_receipts(values):
    table = "Receipts"
    return get_json_table_rows(table, values)


def save_receipts(receipts):
    table = "Receipts"
    return save_json_table_rows(receipts, table)


def update_receipts(receipts):
    table = "Receipts"
    return update_json_tables_rows(receipts, table)


def delete_receipts(values):
    table = "Receipts"
    return delete_json_table_rows(values, table)


def get_receipts_by_date(interval, dates):
    table = "Receipts"
    return get_json_table_by_date(interval, dates, table)


def get_expenses(values):
    table = "Expenses"
    return get_json_table_rows(table, values)


def save_expenses(expenses):
    table = "Expenses"
    return save_json_table_rows(expenses, table)


def update_expenses(expenses):
    table = "Expenses"
    return update_json_tables_rows(expenses, table)


def delete_expenses(values):
    table = "Expenses"
    return delete_json_table_rows(values, table)


def get_expenses_by_date(interval, dates):
    table = "Expenses"
    return get_json_table_by_date(interval, dates, table)


def get_cash_register(values):
    table = "Cash_register"
    return get_json_table_rows(table, values)


def save_cash_register(cash_register):
    table = "Cash_register"
    return save_json_table_rows(cash_register, table)


def update_cash_register(cash_register):
    table = "Cash_register"
    return update_json_tables_rows(cash_register, table)


def delete_cash_register(values):
    table = "Cash_register"
    return delete_json_table_rows(values, table)


def get_cash_register_by_date(interval, dates):
    table = "Cash_register"
    return get_json_table_by_date(interval, dates, table)


def get_agenda(values):
    table = "Agenda"
    return get_json_table_rows(table, values)


def save_agenda(agenda):
    table = "Agenda"
    return save_json_table_rows(agenda, table)


def update_agenda(agenda):
    table = "Agenda"
    return update_json_tables_rows(agenda, table)


def delete_agenda(values):
    table = "Agenda"
    return delete_json_table_rows(values, table)


def get_agenda_by_date(interval, dates):
    table = "Agenda"
    return get_json_table_by_date(interval, dates, table)


def get_appointments(values):
    table = "Appointments"
    return get_json_table_rows(table, values)


def save_appointments(appointments):
    table = "Appointments"
    return save_json_table_rows(appointments, table)


def update_appointments(appointments):
    table = "Appointments"
    return update_json_tables_rows(appointments, table)


def delete_appointments(values):
    table = "Appointments"
    return delete_json_table_rows(values, table)


def get_appointments_by_date(interval, dates):
    table = "Appointments"
    return get_json_table_by_date(interval, dates, table)


def get_activities(values):
    table = "Activities"
    return get_json_table_rows(table, values)


def save_activities(activities):
    table = "Activities"
    return save_json_table_rows(activities, table)


def update_activities(activities):
    table = "Activities"
    return update_json_tables_rows(activities, table)


def delete_activities(values):
    table = "Activities"
    return delete_json_table_rows(values, table)


def get_roles(values):
    table = "Roles"
    return get_json_table_rows(table, values)


def save_roles(roles):
    table = "Roles"
    return save_json_table_rows(roles, table)


def update_roles(roles):
    table = "Roles"
    return update_json_tables_rows(roles, table)


def delete_roles(values):
    table = "Roles"
    return delete_json_table_rows(values, table)


def get_inventories(values):
    table = "Inventories"
    return get_json_table_rows(table, values)


def save_inventories(inventories):
    table = "Inventories"
    return save_json_table_rows(inventories, table)


def update_inventories(inventories):
    table = "Inventories"
    return update_json_tables_rows(inventories, table)


def delete_inventories(values):
    table = "Inventories"
    return delete_json_table_rows(values, table)


def get_address(values):
    table = "Address"
    return get_json_table_rows(table, values)


def save_address(address):
    table = "Address"
    return save_json_table_rows(address, table)


def update_address(address):
    table = "Address"
    return update_json_tables_rows(address, table)


def delete_address(values):
    table = "Address"
    return delete_json_table_rows(values, table)


def get_deliveries(values):
    table = "Deliveries"
    return get_json_table_rows(table, values)


def save_deliveries(deliveries):
    table = "Deliveries"
    return save_json_table_rows(deliveries, table)


def update_deliveries(deliveries):
    table = "Deliveries"
    return update_json_tables_rows(deliveries, table)


def delete_deliveries(values):
    table = "Deliveries"
    return delete_json_table_rows(values, table)
