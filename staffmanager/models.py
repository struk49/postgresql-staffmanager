from staffmanager import db


class Department(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(15), unique=True, nullable=False)
    employee = db.relationship("Employee", backref="department", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.department_name


class Employee(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(20), unique=True, nullable=False)
    employee_description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Employee: {1} | Start: {2}".format(
            self.id, self.employee_name, self.start_date
        )