from app import db

class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Admin %r>" % self.username

class New(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admins.id"))
    admin_name = db.Column(db.String, db.ForeignKey("admins.name"))
    title = db.Column(db.String)
    content = db.Column(db.Text)
    new_type = db.Column(db.String)
    image_path = db.Column(db.String)
    date_time = db.Column(db.String)
    top = db.Column(db.Boolean)

    adminId = db.relationship("Admin", foreign_keys=admin_id)
    adminName = db.relationship("Admin", foreign_keys=admin_name)
    
    def __init__(self, admin_id, admin_name, title, content, new_type, image_path, date_time, top):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.title = title
        self.content = content
        self.new_type = new_type
        self.image_path = image_path
        self.date_time = date_time
        self.top = top


    def __repr__(self):
        return "<New %r>" % self.id

class Subscriber(db.Model):
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "%r;" % self.email