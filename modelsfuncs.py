# The 'core' functions of the application are defined here
# The views call the 'core' functions with different parameters

from config import db
from flask import jsonify, make_response
from models import ActivitiesSchema, AddressSchema, AgendaSchema, AppointmentsSchema, Cash_registerSchema, \
    CustomersSchema, DeliveriesSchema, EmployeesSchema, ExpensesSchema, InventoriesSchema, PaymentsSchema, \
    ProductsSchema, PurchasesSchema, ReceiptsSchema, RolesSchema, SalesSchema, ServicesSchema, SuppliersSchema

tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}
schemas_dict = {
    "Activities": ActivitiesSchema(many=True),
    "Address": AddressSchema(many=True),
    "Agenda": AgendaSchema(many=True),
    "Appointments": AppointmentsSchema(many=True),
    "Cash_register": Cash_registerSchema(many=True),
    "Customers": CustomersSchema(many=True),
    "Deliveries": DeliveriesSchema(many=True),
    "Employees": EmployeesSchema(many=True),
    "Expenses": ExpensesSchema(many=True),
    "Inventories": InventoriesSchema(many=True),
    "Payments": PaymentsSchema(many=True),
    "Products": ProductsSchema(many=True),
    "Purchases": PurchasesSchema(many=True),
    "Receipts": ReceiptsSchema(many=True),
    "Roles": RolesSchema(many=True),
    "Sales": SalesSchema(many=True),
    "Services": ServicesSchema(many=True),
    "Suppliers": SuppliersSchema(many=True)
}


def table_object(table_name):
    return tables_dict.get(table_name)


def schema_object(schema_name):
    return schemas_dict.get(schema_name)


def get_table_rows(table, column, values):
    obj_table = table_object(table)
    q = db.session.query(obj_table).filter(getattr(obj_table, column).in_(values))
    return q.all()


def serialize_table_rows(res, table):
    schema = schema_object(table)
    data = schema.dump(res)
    return jsonify(data)


def get_json_table_rows(table, values):
    column = 'id' + str(table)
    rows = get_table_rows(table, column, values)
    data = serialize_table_rows(rows, table)
    return data


def save_table_rows(values, table):
    obj_table = table_object(table)
    id_obj_table = "id" + str(table)
    id_values = [getattr(d, id_obj_table) for d in values]
    q = db.session.query(obj_table)
    q = q.filter(getattr(obj_table, id_obj_table).in_(id_values))
    print(q)
    exist = q.one_or_none()

    if exist is None:
        db.session.add_all(values)
        db.session.commit()
        return make_response('{} saved'.format(table), 201)
    else:
        return make_response('{} exists already'.format(table), 409)


def deserialize_table_rows(values, table):
    schema = schema_object(table)
    new_rows = schema.load(values[table.lower()]).data
    return new_rows


def save_json_table_rows(values, table):
    new_rows = deserialize_table_rows(values, table)
    res = save_table_rows(new_rows, table)
    return res


def update_table_rows(values, table):
    obj_table = table_object(table)
    id_obj_table = "id" + str(table)

    while values[str(table.lower())]:
        item = values[table.lower()].pop()
        res = db.session.query(obj_table).filter(getattr(obj_table, id_obj_table) == item[id_obj_table]).\
            update(item, synchronize_session='fetch')
        if res == 0:
            return make_response('{}: {} not found'.format(id_obj_table, item[id_obj_table]))

    db.session.commit()
    return make_response('{} updated'.format(table), 201)


def update_json_tables_rows(values, table):
    res = update_table_rows(values, table)
    return res


def delete_table_rows(values, table):
    obj_table = table_object(table)
    id_obj_table = "id" + str(table)
    db.session.query(obj_table).filter(getattr(obj_table, id_obj_table).in_(values)).delete(synchronize_session="fetch")
    db.session.commit()
    return make_response('{} rows deleted'.format(table), 201)


def delete_json_table_rows(values, table):
    res = delete_table_rows(values, table)
    return res


def get_json_table_by_date(interval, dates, table):
    obj_table = table_object(table)

    if interval:
        rows = db.session.query(obj_table).filter(getattr(obj_table, 'Date' + "_" + table.lower()).between(dates[0], dates[1]))
    else:
        rows = get_table_rows(table, 'Date' + "_" + table.lower(), dates)

    data = serialize_table_rows(rows, table)
    return data
