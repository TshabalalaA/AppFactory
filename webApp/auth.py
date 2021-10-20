from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from sqlalchemy import func




auth = Blueprint('auth', __name__)

@auth.route('/screen2' , methods=['GET' , 'POST'])
def screen2():

    if request.method == 'POST':
        surname = request.form.get('surname')
        firstname = request.form.get('firstname')
        contactNo = request.form.get('contactNo')
        date = request.form.get('date')
        age = request.form.get('age')

        check = request.form.getlist('check')
        check = ','.join(check)


        out = request.form.get('out')
        movies = request.form.get('movies')
        tv = request.form.get('tv')
        radio = request.form.get('radio')


        new_user = User(surname=surname, firstname=firstname, contactNo=contactNo,
         age=age, check=check, out=out,movies=movies,tv=tv,radio=radio)
        db.session.add(new_user)
        db.session.commit()

        flash('Details are stored', category='success')

    return render_template("screen2.html")



@auth.route('/screen3')
def screen3():
    myUser = User.query.all()
    no = len(User.query.all())
    agesum = User.query.with_entities(func.sum(User.age).label('total')).first().total
    agemax = User.query.with_entities(func.max(User.age).label('total')).first().total
    agemin = User.query.with_entities(func.min(User.age).label('result2')).first().result2
    aveAge = round((agesum/no),2)

    o = User.query.with_entities(User.out, User.id).all()
    m = User.query.with_entities(User.movies, User.id).all()
    t = User.query.with_entities(User.tv, User.id).all()
    r = User.query.with_entities(User.radio, User.id).all()
    c = User.query.with_entities(User.check, User.id).all()

    count_out = 0
    count = 0
    for i in range(no):
        count = count + 1
        if o[i][0] < 4:
            count_out = count_out + 1

        else:
            continue

    count_movies = 0
    for i in range(no):
        count = count + 1
        if m[i][0] < 4:
            count_movies = count_movies + 1

        else:
            continue

    count_tv = 0

    for i in range(no):
        count = count + 1
        if t[i][0] < 4:
            count_tv = count_tv + 1

        else:
            continue

    count_radio = 0
    for i in range(no):
        count = count + 1
        if r[i][0] < 4:
            count_radio = count_radio + 1

        else:
            continue

    ans = count
    like_tv = round((count_tv/ans),2)
    like_out = round((count_out/ans),2)
    like_radio = round((count_radio/ans),2)
    like_movies = round((count_movies/ans),2)

    food_checked = []

    for i in range(no):
        temp = c[i][0].split(",")
        for j in range(len(temp)):
            food_checked.append(temp[j])


    count_pizza = 0
    count_pasta = 0
    count_other = 0
    count_beef= 0
    count_chicken = 0
    count_pap = 0

    for i in food_checked:
        if i == 'pizza':
            count_pizza = count_pizza + 1

        elif i == 'pasta':
            count_pasta = count_pasta + 1

        elif i == 'other':
            count_other = count_other + 1

        elif i == 'beef_stir_fry':
            count_beef = count_beef + 1

        elif i == 'chicken_stir_fry':
            count_chicken = count_chicken + 1

        elif i == 'pap_wors':
            count_pap = count_pap + 1

    like_pizza = round(((count_pizza/no)*100),2)
    like_pasta = round(((count_pasta/no)*100),2)
    like_beef = round(((count_beef/no)*100),2)
    like_other = round(((count_other/no)*100),2)
    like_chicken = round(((count_chicken/no)*100),2)
    like_pap = round(((count_pap/no)*100),2)


    return render_template("screen3.html", myUser=myUser, no=no, aveAge=aveAge, agemax=agemax,
    agemin=agemin,like_out=like_out,like_movies=like_movies,
    like_tv=like_tv,like_radio=like_radio,
    like_pap=like_pap, like_pasta=like_pasta,like_pizza=like_pizza)
