from flask import (
    render_template, url_for, flash, redirect, request, abort)
# from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, app
from flaskblog.models import PerfumeInfo, Scents
from flaskblog.forms import (
    QuestionnaireForm, AddToFavourites)
# from flaskblog.users.utils import save_picture, send_reset_email
from flaskblog.recommendations import (
    QuestionnaireRecommendation as qr, UserRecommendation as us)
from flaskblog.utils import is_valid


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/questionnaire", methods=['GET', 'POST'])
def fill_questionnaire():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        gender = form.genders.data
        age = form.ages.data
        group = form.groups.data
        scent = form.scents.data
        key = str(gender+age+group+scent)
        return redirect(url_for('questionnaire_results', key=key))

    return render_template('questionnaire.html', title='Scents Questionnaire', form=form)


@app.route("/questionnaire/results/<string:key>", methods=['GET'])
def questionnaire_results(key):
    if is_valid(key):
        results = qr(key)
    else:
        abort(403)

    return render_template('questionnaire_results.html', title='Twoje wyniki', results=results)


# def record_exists(perfume_id):
#     query = UserPreferences.query.filter(
#         (UserPreferences.perfume_id.like(perfume_id))).all()
#     print(query)
#     if query:
#         return True
#     else:
#         return False


# @app.route("/add_favourites", methods=['GET', 'POST'])
# def favourites():
#     form = AddToFavourites()
#     form.perfume.choices = [(str(p.id), str(p.name+' by '+p.brand))
#                             for p in PerfumeInfo.query.order_by('name')]
#     # username = current_user.username
#     # user_id = (User.query.filter_by(username=username).first()).id
#     choices = []
#     tmp_choices = get_perfume_names(choices)
#     your_choices = []
#     for tmp in tmp_choices:
#         your_choices.append(str(tmp[0].name+' by '+tmp[0].brand))
#     if form.validate_on_submit():
#         perfume = form.perfume.data
#         # user_preference = UserPreferences(user_id=user_id, perfume_id=perfume)
#         # if not record_exists(user_id, perfume):
#         #     db.session.add(user_preference)
#         #     db.session.commit()
#         # else:
#         #     flash('record already exists in database', 'danger')
#         # return redirect(url_for('users.favourites'))

#     return render_template('add_favourite_perfumes.html', title='Favs', form=form, tmp_choices=tmp_choices)


def get_perfume_names(id_list):
    perfumes = []
    for p_id in id_list:
        print(p_id.perfume_id)
        query = PerfumeInfo.query.filter(
            PerfumeInfo.id.like(p_id.perfume_id)).all()
        perfumes.append(query)
    return perfumes


# @app.route("/delete_preference/", methods=['POST'])
# def delete_preference():
#     # user = current_user.id
#     # query = UserPreferences.query.filter(
#     #     UserPreferences.user_id.like(user)).all()
#     # preference = query
#     # if preference:
#     #     for each_one in preference:
#     #         db.session.delete(each_one)
#     #         db.session.commit()
#     #     flash('Perfumes has been removed', 'success')
#     # else:
#     #     flash('No such record in db, please reload the page')
#     return redirect(url_for('users.favourites'))

recomendations = [
    {
        'name': 'Perfumy 1',
        'brand': 'Brand 1'
    },
    {
        'name': 'Perfumy 3',
        'brand': 'Brand 4'
    },
    {
        'name': 'Perfumy 2',
        'brand': 'Brand 5'
    }
]
@app.route("/recommendations", methods=['GET', 'POST'])
def recommend_perfumes():
    # # user = current_user.id
    # # query = UserPreferences.query.filter(
    # #     UserPreferences.user_id.like(user)).all()
    # # print(query)
    # # print(len(query))
    # user_perfumes = []
    # # if len(query) < 3:
    # # flash('You have to have added at least 3 perfumes to your favourites', 'info')
    # # return redirect(url_for('users.favourites'))

    # # for p in query:
    # #     user_perfumes.append(p.perfume_id)
    # # print(user_perfumes)
    # # recommendations = us(user_perfumes)
    # return render_template('recommended.html', title='Scents Recommended Just For You', recommendations=[])
    return render_template('recommended.html', recomendations=recomendations)
