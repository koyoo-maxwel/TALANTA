import os
from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .forms import CommentsForm, UpdateProfile, TalentForm,UploadForm
from ..models import Comment, Talent, User 
from flask_login import login_required, current_user
from .. import db , videos

# import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Talanta - Show Case Talent !'

    # search_talent = request.args.get('talent_query')
    talents= Talent.fetch_videos()  

    return render_template('index.html', title = title, talents= talents)

#this section consist of the category root functions

@main.route('/sports/talents/')
def sports():
    '''
    View root page function that returns the index page and its data
    '''
    talents= talent.get_all_talents()
    title = 'Home - Welcome to The best talent showcasing  Website Online'  
    return render_template('posts.html', title = title, talents= talents )



@main.route('/music/talents/')
def music():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Music'

    talents= talent.get_all_talents()

    return render_template('posts.html', title = title, talents= talents )



@main.route('/entertainment/talents/')
def entertainment():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Entertainment'

    talents= talent.get_all_talents()

    return render_template('posts.html', title = title, talents= talents )


@main.route('/others/talents/')
def others():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'others'
    talents= talent.get_all_talents()
    return render_template('posts.html', title = title, talents= talents )
 
#  end of category root functions



@main.route('/talent/<int:talent_id>')
def talent(talent_id):

    '''
    View talent page function that returns the talent details page and its data
    '''
    found_talent= Talent.get_talent(talent_id)
    title = talent_id
    talent_comments = Comment.get_comments(talent_id)

    return render_template('posts.html',title= title ,found_talent= found_talent, talent_comments= talent_comments)

'''
A route to videos searched from the database
'''
@main.route('/search/<talent_name>')
def search(talent_name):
    '''
    View function to display the search results
    '''
    searched_talents = Talent.search_talent(talent_name)
    title = f'search results for {talent_name}'

    return render_template('posts.html',talents = searched_talents)



@main.route('/talent/new/', methods = ['GET','POST'])
@login_required
def new_talent():
    '''
    Function that enables one to post new talents
    '''
    form = TalentForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        talent= form.content.data
        category_id = form.category_id.data
        new_talent= talent(talent= talent, category_id= category_id)

        new_talent.save_talent()
        return redirect(url_for('main.index'))

    return render_template('new_talent.html', new_talent_form= form, category= category)

@main.route('/category/<int:id>')
def category(id):
    '''
    function that returns talents based on the entered category id
    '''
    category = Category.query.get(id)

    if category is None:
        abort(404)

    talents_in_category = Talents.get_talent(id)
    return render_template('category.html' ,category= category, talents= talents_in_category)


@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

