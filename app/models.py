from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import UserMixin 
from . import login_manager

class User(UserMixin , db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255) , unique = True , index = True )
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    vlogs = db.relationship('Talent',backref = 'user',lazy="dynamic")
    

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
        
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))


'''
Talent model . Defines our talents' table . Creates a relationship between the table and our users table . 

We need a way to query users' details . 
'''
class Talent (db.Model):
    __tablename__ = 'talents'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    talent_video_path = db.Column(db.String())
    posted = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    category = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'talent',lazy="dynamic")

    def save_article(self):
        db.session.add(self)
        db.session.commit()


    def delete_article(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def fetch_videos(cls):
        talents = Talent.query.all()

        return talents

    @classmethod
    def fetch_by_category(cls,cat):
        talents = Talent.query.filter_by(category = cat).all()

        return talents
 
'''
Comment model . Defining our comments' table . Linking comments table with talents, table . 
'''
class Comment (db.Model):
    __tablename__ = 'comments'

    id = db.Column (db.Integer , primary_key = True)
    comment = db.Column(db.String)
    talent_id =  db.Column(db.Integer,db.ForeignKey("talents.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()



# class TalentCategory(db.Model):
#     '''
#     Function that defines different categories of talents
#     '''
#     __tablename__ ='categories'


#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     category_description = db.Column(db.String(255))
#     talent_id =  db.Column(db.Integer,db.ForeignKey("talents.id"))


    # @classmethod
    # def get_categories(cls):
    #         '''
    #         This function fetches all the categories from the database
    #         '''
    #         categories = TalentCategory.query.all()
    #         return categories