from config import db, ma
from marshmallow import fields, post_load

# Simple ORM for the DB
# Simple schemas for serializing/deserializing the models
# All class names are intuitive according to their functions


class Agenda(db.Model):
    __tablename__ = "Agenda"
    idAgenda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date_agenda = db.Column(db.String(32), nullable=False)
    Time_begin = db.Column(db.String(32), nullable=False)
    Time_finish = db.Column(db.String(32), nullable=False)
    Activity = db.Column(db.String(100), nullable=False)
    idActivities = db.Column(db.Integer, primary_key=True, nullable=False)
    Employee = db.Column(db.String(100), nullable=False)
    idEmployees = db.Column(db.Integer, primary_key=True, nullable=False)
    idAppointments = db.Column(db.Integer)


class AgendaSchema(ma.Schema):
    idAgenda = fields.Int()
    Date_agenda = fields.Str()
    Time_begin = fields.Str()
    Time_finish = fields.Str()
    Activity = fields.Str()
    idActivities = fields.Int()
    Employee = fields.Str()
    idEmployees = fields.Int()
    idAppointments = fields.Int()

    @post_load
    def make_sale(self, data):
        return Agenda(**data)


class Appointments(db.Model):
    __tablename__ = "Appointments"
    idAppointments = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSales = db.Column(db.Integer)
    idPurchases = db.Column(db.Integer)
    idAgenda = db.Column(db.Integer)


class AppointmentsSchema(ma.Schema):
    idAppointments = fields.Int()
    idSales = fields.Int()
    idPurchases = fields.Int()
    idAgenda = fields.Int()

    @post_load
    def make_sale(self, data):
        return Appointments(**data)


class Activities(db.Model):
    __tablename__ = "Activities"
    idActivities = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(500))


class ActivitiesSchema(ma.Schema):
    idActivities = fields.Int()
    Name = fields.Str()
    Description = fields.Str()

    @post_load
    def make_sale(self, data):
        return Activities(**data)


class Products(db.Model):
    __tablename__ = "Products"
    idProducts = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100))
    Supplier = db.Column(db.String(100))
    idSuppliers = db.Column(db.Integer)
    Cost = db.Column(db.Float)
    Price = db.Column(db.Float)


class ProductsSchema(ma.Schema):
    idProducts = fields.Int()
    Name = fields.Str()
    Supplier = fields.Str()
    idSuppliers = fields.Int()
    Cost = fields.Float()
    Price = fields.Float()

    @post_load
    def make_sale(self, data):
        return Products(**data)


class Cash_register(db.Model):
    __tablename__ = "Cash_register"
    idCash_register = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date_cash_register = db.Column(db.String(32), nullable=False)
    Cash_value = db.Column(db.Float, nullable=False)
    Withdraw = db.Column(db.Float)
    Deposit = db.Column(db.Float)
    Expense = db.Column(db.Float)
    idExpenses = db.Column(db.Integer)
    Payment = db.Column(db.Float)
    idPayments = db.Column(db.Integer)
    Receipts = db.Column(db.Float)
    idReceipts = db.Column(db.Integer)


class Cash_registerSchema(ma.Schema):
    idCash_register = fields.Int()
    Date_cash_register = fields.Str()
    Cash_value = fields.Float()
    Withdraw = fields.Float()
    Deposit = fields.Float()
    Expense = fields.Float()
    idExpenses = fields.Int()
    Payment = fields.Float()
    idPayments = fields.Int()
    Receipts = fields.Float()
    idReceipts = fields.Int()

    @post_load
    def make_sale(self, data):
        return Cash_register(**data)


class Roles(db.Model):
    __tablename__ = "Roles"
    idRoles = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Buy = db.Column(db.Boolean, nullable=False)
    Sale = db.Column(db.Boolean, nullable=False)
    Delivery = db.Column(db.Boolean, nullable=False)
    Receive = db.Column(db.Boolean, nullable=False)


class RolesSchema(ma.Schema):
    idRoles = fields.Int()
    Name = fields.Str()
    Buy = fields.Boolean()
    Sale = fields.Boolean()
    Delivery = fields.Boolean()
    Receive = fields.Boolean()

    @post_load
    def make_sale(self, data):
        return Roles(**data)


class Customers(db.Model):
    __tablename__ = "Customers"
    idCustomers = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Telephone = db.Column(db.String(15))
    Address = db.Column(db.Integer)


class CustomersSchema(ma.Schema):
    idCustomers = fields.Int()
    Name = fields.Str()
    Telephone = fields.Str()
    Address = fields.Int()

    @post_load
    def make_sale(self, data):
        return Customers(**data)


class Purchases(db.Model):
    __tablename__ = "Purchases"
    idPurchases = db.Column(db.Integer, primary_key=True)
    CodPurchase = db.Column(db.Integer, nullable=False)
    Date_purchases = db.Column(db.String(32), nullable=False)
    Date_delivery = db.Column(db.String(32))
    Employee = db.Column(db.String(100), nullable=False)
    idEmployees = db.Column(db.Integer, primary_key=True, nullable=False)
    Supplier = db.Column(db.String(100), nullable=False)
    idSuppliers = db.Column(db.Integer, primary_key=True, nullable=False)
    Product = db.Column(db.String(100), nullable=False)
    idProducts = db.Column(db.Integer, nullable=False)
    Payment = db.Column(db.Float, nullable=False)
    idPayments = db.Column(db.Integer, primary_key=True, nullable=False)
    idAppointments = db.Column(db.Integer)


class PurchasesSchema(ma.Schema):
    idPurchases = fields.Int()
    CodPurchase = fields.Int()
    Date_purchases = fields.Str()
    Date_delivery = fields.Str()
    Employee = fields.Str()
    idEmployees = fields.Int()
    Supplier = fields.Str()
    idSuppliers = fields.Int()
    Product = fields.Str()
    idProducts = fields.Int()
    Payment = fields.Float()
    idPayments = fields.Int()
    idAppointments = fields.Int()

    @post_load
    def make_sale(self, data):
        return Purchases(**data)


class Expenses(db.Model):
    __tablename__ = "Expenses"
    idExpenses = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date_expenses = db.Column(db.String(32), nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Value = db.Column(db.Float, nullable=False)


class ExpensesSchema(ma.Schema):
    idExpenses = fields.Int()
    Date_expenses = fields.Str()
    Name = fields.Str()
    Value = fields.Float()

    @post_load
    def make_sale(self, data):
        return Expenses(**data)


class Address(db.Model):
    __tablename__ = "Address"
    idAddress = db.Column(db.Integer, primary_key=True, autoincrement=True)
    State = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    District = db.Column(db.String(100), nullable=False)
    Street = db.Column(db.String(100), nullable=False)
    Number = db.Column(db.String(10), nullable=False)
    CEP = db.Column(db.String(9), nullable=False)


class AddressSchema(ma.Schema):
    idAddress = fields.Int()
    State = fields.Str()
    City = fields.Str()
    District = fields.Str()
    Street = fields.Str()
    Number = fields.Str()
    CEP = fields.Str()

    @post_load
    def make_sale(self, data):
        return Address(**data)


class Deliveries(db.Model):
    __tablename__ = "Deliveries"
    idDeliveries = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSales = db.Column(db.Integer, nullable=False)
    CodSales = db.Column(db.Integer, nullable=False)
    Date_delivery = db.Column(db.String(32), nullable=False)
    Address = db.Column(db.Integer, nullable=False)


class DeliveriesSchema(ma.Schema):
    idDeliveries = fields.Int()
    idSales = fields.Int()
    CodSales = fields.Int()
    Date_delivery = fields.Str()
    Address = fields.Int()

    @post_load
    def make_sale(self, data):
        return Deliveries(**data)


class Inventories(db.Model):
    __tablename__ = "Inventories"
    idInventories = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Product = db.Column(db.String(100), nullable=False)
    idProducts = db.Column(db.Integer, primary_key=True, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)


class InventoriesSchema(ma.Schema):
    idInventories = fields.Int()
    Product = fields.Str()
    idProducts = fields.Int()
    Quantity = fields.Int()

    @post_load
    def make_sale(self, data):
        return Inventories(**data)


class Suppliers(db.Model):
    __tablename__ = "Suppliers"
    idSuppliers = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Telephone = db.Column(db.String(15))
    Address = db.Column(db.Integer)


class SuppliersSchema(ma.Schema):
    idSuppliers = fields.Int()
    Name = fields.Str()
    Telephone = fields.Str()
    Address = fields.Int()

    @post_load
    def make_sale(self, data):
        return Suppliers(**data)


class Employees(db.Model):
    __tablename__ = "Employees"
    idEmployees = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Telephone = db.Column(db.String(15))
    Address = db.Column(db.Integer)
    Role = db.Column(db.String(100), nullable=False)
    idRoles = db.Column(db.Integer, primary_key=True, nullable=False)


class EmployeesSchema(ma.Schema):
    idEmployees = fields.Int()
    Name = fields.Str()
    Telephone = fields.Str()
    Address = fields.Int()
    Role = fields.Str()
    idRoles = fields.Int()

    @post_load
    def make_sale(self, data):
        return Employees(**data)


class Payments(db.Model):
    __tablename__ = "Payments"
    idPayments = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPurchases = db.Column(db.Integer, nullable=False)
    CodPurchase = db.Column(db.Integer, nullable=False)
    Date_payments = db.Column(db.String(32), nullable=False)
    Value = db.Column(db.Float, nullable=False)


class PaymentsSchema(ma.Schema):
    idPayments = fields.Int()
    idPurchases = fields.Int()
    CodPurchase = fields.Int()
    Date_payments = fields.Str()
    Value = fields.Float()

    @post_load
    def make_sale(self, data):
        return Payments(**data)


class Receipts(db.Model):
    __tablename__ = "Receipts"
    idReceipts = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSales = db.Column(db.Integer, nullable=False)
    CodSales = db.Column(db.Integer, nullable=False)
    Date_receipts = db.Column(db.String(32), nullable=False)
    Value = db.Column(db.Float, nullable=False)


class ReceiptsSchema(ma.Schema):
    idReceipts = fields.Int()
    idSales = fields.Int()
    CodSales = fields.Int()
    Date_receipts = fields.Str()
    Value = fields.Float()

    @post_load
    def make_sale(self, data):
        return Receipts(**data)


class Services(db.Model):
    __tablename__ = "Services"
    idServices = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Cost = db.Column(db.Float, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Time = db.Column(db.Integer)
    Description = db.Column(db.String(500))


class ServicesSchema(ma.Schema):
    idServices = fields.Int()
    Name = fields.Str()
    Cost = fields.Float()
    Price = fields.Float()
    Time = fields.Int()
    Description = fields.Str()

    @post_load
    def make_sale(self, data):
        return Services(**data)


class Sales(db.Model):
    __tablename__ = "Sales"
    idSales = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date_sales = db.Column(db.String(32), nullable=False)
    CodSales = db.Column(db.Integer, nullable=False)
    Employee = db.Column(db.String(100), nullable=False)
    idEmployees = db.Column(db.Integer, primary_key=True, nullable=False)
    Customer = db.Column(db.String(100), nullable=False)
    idCustomers = db.Column(db.Integer, primary_key=True, nullable=False)
    Product = db.Column(db.String(100))
    idProducts = db.Column(db.Integer)
    Service = db.Column(db.String(100))
    idServices = db.Column(db.Integer)
    Receipt = db.Column(db.Float, nullable=False)
    idReceipts = db.Column(db.Integer, primary_key=True, nullable=False)
    idDeliveries = db.Column(db.Integer)
    idAppointments = db.Column(db.Integer)


class SalesSchema(ma.Schema):
    idSales = fields.Int()
    Date_sales = fields.Str()
    CodSales = fields.Int()
    Employee = fields.Str()
    idEmployees = fields.Int()
    Customer = fields.Str()
    idCustomers = fields.Int()
    Product = fields.Str()
    idProducts = fields.Int()
    Service = fields.Str()
    idServices = fields.Int()
    Receipt = fields.Float()
    idReceipts = fields.Int()
    idDeliveries = fields.Int()
    idAppointments = fields.Int()

    @post_load
    def make_sale(self, data):
        return Sales(**data)
