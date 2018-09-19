import os
import app
from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .forms import CommentsForm, UpdateProfile, TalentForm
from ..models import Comment, Talent, User 
from flask_login import login_required, current_user
from .. import db , videos ,photos
from config import config_options , Config



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Talanta - Show Case Talent !'

    search_talent = request.args.get('talent_query')


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



@main.route('/talanta/<username>/new/', methods = ['GET','POST'])
@login_required
def new_talent(username):
    '''
    Function that enables one to post new talents
    '''
    user = User.query.filter_by(username = username).first()
    form = TalentForm()


    if user is None:
        abort( 404 )

    if form.validate_on_submit():
        title = form.title.data
        category= form.category.data
        description = form.description.data

        file = form.video_file.data.filename
        path = f'{app.Config.UPLOADED_VIDEOS_DEST}{form.video_file.data.filename}'
        form.video_file.data.save(os.path.join(app.Config.UPLOADED_VIDEOS_DEST, file))


        new_talent= Talent(category= category,title=title,talent_video_path=path, description =description, user=current_user)

        new_talent.save_talent()

        return redirect(url_for('main.profile',username=username))

    return render_template('new_video.html',user=user, form=form)




@main.route('/user/<username>')
def profile(username):
    the_user = current_user.id
    user = User.query.filter_by(username = username).first()
    talents = Talent.query.filter_by(user_id=the_user).all()
    # talents = User.vlogs

    if user is None:
        abort(404)

    return render_template("profile/profile.html" , talents =talents)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

'''
This route will be taken whenever uploading a new video to the db
'''
# @main.route('/talanta/<username>/new/video',methods= ['POST'])
# @login_required
# def upload_video(username):
#     talanta = Talent.query.filter_by(user = username).first()


#     image = 'uploads/' + form.image_file.data.filename
#     form.image_file.data.save(os.path.join(app.static_folder, image))


#     if 'video' in request.files:
#         filename = videos.save(request.files['video'])
#         path = f'videos/{filename}'
#         talanta.talent_video_path = path 
#         db.session.commit()


#     return redirect(url_for('main.profile',username = username))


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

