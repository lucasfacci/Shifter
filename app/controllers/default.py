import os
from app import app, db, login_manager
from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timezone, timedelta
from app.models.forms import LoginForm, UsernameForm, PasswordForm, NameForm, EmailForm, NewsletterForm, NewForm
from app.models.tables import Admin, Subscriber, New

@login_manager.user_loader
def load_user(id):
    return Admin.query.filter_by(id=id).first()


@app.route("/")
def index():
    newsletter_form = NewsletterForm()
    newsAux = New.query.order_by(New.id.desc()).limit(8).all()
    banner = New.query.filter_by(top="1").order_by(New.id.desc()).first()
    for new in newsAux:
        try:
            if new.id == banner.id:
                news = New.query.order_by(New.id.desc()).limit(9).all()
                counter = len(news)
                return render_template("index.html", newsletter_form=newsletter_form, news=news, banner=banner, counter=counter)
            else:
                news = New.query.order_by(New.id.desc()).limit(8).all()
                counter = len(news)
        except:
            news = New.query.order_by(New.id.desc()).limit(8).all()
            counter = len(news)
    try:
        return render_template("index.html", newsletter_form=newsletter_form, news=news, banner=banner, counter=counter)
    except:
        counter = 0
        return render_template("index.html", newsletter_form=newsletter_form, banner=banner, counter=counter)


@app.route("/page/<int:counter>/<int:number>")
def page(counter, number):
    allNews = []
    label = 0
    checkpoint = 0
    newsPage = {}
    new0, new1, new2, new3, new4, new5, new6, new7 = None, None, None, None, None, None, None, None
    newsletter_form = NewsletterForm()
    if counter < 8 or counter > 9:
        return redirect(url_for("index"))
    if number <= 0:
        return redirect(url_for("index"))
    if number >= 1:
        newsAux = New.query.order_by(New.id.desc()).all()
        banner = New.query.filter_by(top="1").order_by(New.id.desc()).first()
        for new in newsAux:
            try:
                if banner.id != new.id:
                    allNews.append(new)
            except:
                allNews.append(new)
        lenAllNews = len(allNews)
        if counter == 8 or counter == 9:
            separator = lenAllNews / 8
            if separator > int(separator):
                pages = int(separator + 1)
            else:
                pages = int(separator)
            if number >= pages:
                return redirect(url_for("index"))
            i = number
            for i in range(int(pages)):
                for j in range(lenAllNews):
                    if j == 0:
                        try:
                            if checkpoint >= lenAllNews:
                                new0 = None
                            else:
                                new0 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 1:
                        try:
                            if checkpoint >= lenAllNews:
                                new1 = None
                            else:
                                new1 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 2:
                        try:
                            if checkpoint >= lenAllNews:
                                new2 = None
                            else:
                                new2 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 3:
                        try:
                            if checkpoint >= lenAllNews:
                                new3 = None
                            else:
                                new3 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 4:
                        try:
                            if checkpoint >= lenAllNews:
                                new4 = None
                            else:
                                new4 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 5:
                        try:
                            if checkpoint >= lenAllNews:
                                new5 = None
                            else:
                                new5 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 6:
                        try:
                            if checkpoint >= lenAllNews:
                                new6 = None
                            else:
                                new6 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                    elif j == 7:
                        try:
                            if checkpoint >= lenAllNews:
                                new7 = None
                            else:
                                new7 = allNews[checkpoint]
                                checkpoint += 1
                        except:
                            pass
                news = {"0":new0, "1":new1, "2":new2, "3":new3, "4":new4, "5":new5, "6":new6, "7":new7}
                newsPage["{0}".format(label)] = news
                label += 1
            totalPages = len(newsPage)
            thisPageAux = newsPage.pop("{0}".format(number))
            thisPage = list(thisPageAux.values())
            thisPage = filter(None, thisPage)
    return render_template("page.html", newsletter_form=newsletter_form, counter=counter, number=number, totalPages=totalPages, thisPage=thisPage)


@app.route("/newsletter", methods=["POST"])
def newsletter():
    newsletter_form = NewsletterForm()
    if newsletter_form.validate_on_submit():
        try:
            name = newsletter_form.name.data
            email = newsletter_form.email.data
            subscriber = Subscriber(name, email)
            db.session.add(subscriber)
            db.session.commit()
            flash("Inscrito com sucesso.")
        except:
            flash("Você já foi inscrito anteriormente.")
    else:
        print(newsletter_form.errors)
    return redirect(url_for("index"))


@app.route("/categoria/<string:new_type>/<int:number>")
def category(new_type, number):
    newsletter_form = NewsletterForm()
    allNews = []
    label = 0
    checkpoint = 0
    newsPage = {}
    new0, new1, new2, new3, new4, new5, new6, new7, new8, new9 = None, None, None, None, None, None, None, None, None, None
    if new_type == "bigtech":
        news = New.query.filter_by(new_type="Big Tech").order_by(New.id.desc()).all()
        aux = "Big Tech"
    elif new_type == "opiniao":
        news = New.query.filter_by(new_type="Opinião").order_by(New.id.desc()).all()
        aux = "Opinião"
    elif new_type == "mobilidade":
        news = New.query.filter_by(new_type="Mobilidade").order_by(New.id.desc()).all()
        aux = "Mobilidade"
    elif new_type == "avgames":
        news = New.query.filter_by(new_type="AV/Games").order_by(New.id.desc()).all()
        aux = "AV/Games"
    elif new_type == "inovacao":
        news = New.query.filter_by(new_type="Inovação").order_by(New.id.desc()).all()
        aux = "Inovação"
    elif new_type == "ciencia":
        news = New.query.filter_by(new_type="Ciência").order_by(New.id.desc()).all()
        aux = "Ciência"
    elif new_type == "seguranca":
        news = New.query.filter_by(new_type="Segurança").order_by(New.id.desc()).all()
        aux = "Segurança"
    if news == []:
        totalPages = 0
        thisPage = []
        return render_template("category.html", newsletter_form=newsletter_form, news=news, aux=aux, new_type=new_type, number=number, totalPages=totalPages, thisPage=thisPage)
    if number <= 0:
        return redirect(url_for("index"))
    if number >= 1:
        lenAllNews = len(news)
        separator = lenAllNews / 10
        if separator > int(separator):
            pages = int(separator + 1)
        else:
            pages = int(separator)
        for i in range(int(pages)):
            for j in range(lenAllNews):
                if j == 0:
                    try:
                        if checkpoint >= lenAllNews:
                            new0 = None
                        else:
                            new0 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 1:
                    try:
                        new1 = None
                        if checkpoint >= lenAllNews:
                            new1 = None
                        else:
                            new1 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 2:
                    try:
                        new2 = None
                        if checkpoint >= lenAllNews:
                            new2 = None
                        else:
                            new2 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 3:
                    try:
                        if checkpoint >= lenAllNews:
                            new3 = None
                        else:
                            new3 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 4:
                    try:
                        if checkpoint >= lenAllNews:
                            new4 = None
                        else:
                            new4 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 5:
                    try:
                        if checkpoint >= lenAllNews:
                            new5 = None
                        else:
                            new5 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 6:
                    try:
                        if checkpoint >= lenAllNews:
                            new6 = None
                        else:
                            new6 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 7:
                    try:
                        if checkpoint >= lenAllNews:
                            new7 = None
                        else:
                            new7 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 8:
                    try:
                        if checkpoint >= lenAllNews:
                            new8 = None
                        else:
                            new8 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
                elif j == 9:
                    try:
                        if checkpoint >= lenAllNews:
                            new9 = None
                        else:
                            new9 = news[checkpoint]
                            checkpoint += 1
                    except:
                        pass
            allNews = {"0":new0, "1":new1, "2":new2, "3":new3, "4":new4, "5":new5, "6":new6, "7":new7, "8":new8, "9":new9}
            newsPage["{0}".format(label)] = allNews
            label += 1
        totalPages = len(newsPage)
        thisPageAux = newsPage.pop("{0}".format(number - 1))
        thisPage = list(thisPageAux.values())
        thisPage = filter(None, thisPage)
    return render_template("category.html", newsletter_form=newsletter_form, news=news, aux=aux, new_type=new_type, number=number, totalPages=totalPages, thisPage=thisPage)


@app.route("/noticia/<int:id>")
def display(id):
    try:
        newsletter_form = NewsletterForm()
        new = New.query.get(id)
        paragraphs = new.content.splitlines()
    except:
        return redirect(url_for("index"))
    return render_template("display.html", newsletter_form=newsletter_form, new=new, paragraphs=paragraphs)


@app.route("/login", methods=["GET", "POST"])
def login():
    logout_user()
    newsletter_form = NewsletterForm()
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        try:
            if admin.username == form.username.data and check_password_hash(admin.password, form.password.data):
                login_user(admin)
                flash("Acesso Permitido.")
                return redirect(url_for("index"))
            else:
                flash("Acesso Negado.")
        except:
            flash("Acesso Negado.")
    else:
        print(form.errors)
    return render_template("login.html", newsletter_form=newsletter_form, form=form)


@app.route("/conta", methods=["GET", "POST"])
@login_required
def account():
    newsletter_form = NewsletterForm()
    username_form = UsernameForm()
    password_form = PasswordForm()
    name_form = NameForm()
    email_form = EmailForm()
    if username_form.validate_on_submit():
        admin_id = current_user.get_id()
        username = username_form.username.data
        admin = Admin.query.filter_by(id=admin_id).first()
        admin.username = username_form.username.data
        db.session.commit()
        flash("Nome de usuário alterado com sucesso.")
        return redirect(url_for("index"))
    else:
        print(username_form.errors)
    if password_form.validate_on_submit():
        admin_id = current_user.get_id()
        password = password_form.password.data
        confirmation = password_form.confirmation.data
        if password == confirmation:
            admin = Admin.query.filter_by(id=admin_id).first()
            admin.password = generate_password_hash(password_form.password.data)
            db.session.commit()
            flash("Senha alterada com sucesso.")
            return redirect(url_for("index"))
        else:
            flash("As senhas não são iguais.")
    else:
        print(password_form.errors)
    if name_form.validate_on_submit():
        admin_id = current_user.get_id()
        name = name_form.name.data
        admin = Admin.query.filter_by(id=admin_id).first()
        admin.name = name_form.name.data
        db.session.commit()
        flash("Nome alterado com sucesso.")
        return redirect(url_for("index"))
    else:
        print(name_form.errors)
    if email_form.validate_on_submit():
        admin_id = current_user.get_id()
        email = email_form.email.data
        admin = Admin.query.filter_by(id=admin_id).first()
        admin.email = email_form.email.data
        db.session.commit()
        flash("E-mail alterado com sucesso.")
        return redirect(url_for("index"))
    else:
        print(email_form.errors)
    return render_template("account.html", newsletter_form=newsletter_form, username_form=username_form, password_form=password_form, name_form=name_form, email_form=email_form)


@app.route("/notícia", methods=["GET", "POST"])
@login_required
def new():
    newsletter_form = NewsletterForm()
    form = NewForm()
    if form.validate_on_submit():
        admin_id = current_user.get_id()
        admin = Admin.query.filter_by(id=admin_id).first()
        admin_name = admin.name
        title = form.title.data
        content = form.content.data
        new_type = form.new_type.data
        image = request.files["image_path"]
        try:
            new = New.query.order_by(New.id.desc()).first()
            number = int(new.id) + 1
        except:
            number = 1
        save_image = os.path.join(app.root_path, "static", "images", "img{0}.png".format(number))
        image_path = os.path.join("..", "static", "images", "img{0}.png".format(number))
        image.save(save_image)
        dateTimeFunc = datetime.now()
        difference = timedelta(hours = -3)
        timeZoneSP = timezone(difference)
        dateTimeSP = dateTimeFunc.astimezone(timeZoneSP)
        date_time = dateTimeSP.strftime("%d/%m/%Y %H:%M")
        top = form.top.data
        newImage = New(admin_id, admin_name, title, content, new_type, image_path, date_time, top)
        db.session.add(newImage)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        print(form.errors)
    return render_template("new.html", newsletter_form=newsletter_form, form=form)


@app.route("/lista")
@login_required
def subscribers():
    allCharacters = []
    newsletter_form = NewsletterForm()
    emails = Subscriber.query.order_by(Subscriber.id.desc()).all()
    for email in emails:
        aux = str(email).replace("'", " ")
        allCharacters += aux
    allEmails = ''.join(map(str, allCharacters))
    return render_template("subscribers.html", newsletter_form=newsletter_form, allEmails=allEmails)


@app.route("/sobre")
def about():
    newsletter_form = NewsletterForm()
    return render_template("about.html", newsletter_form=newsletter_form)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    if request.method == "POST":
        new_type = request.form.get("new_type")
        image = request.files["image_path"]
        title = request.form.get("title")
        content = request.form.get("content")
        top = request.form.get("top")
        save_image = os.path.join(app.root_path, "static", "images", "img{0}.png".format(id))
        image_path = os.path.join("..", "static", "images", "img{0}.png".format(id))
        image.save(save_image)
        if top == "on":
            top = 1
        elif top == None:
            top = 0
        new = New.query.get(id)
        new.new_type = new_type
        new.image_path = image_path
        new.title = title
        new.content = content
        new.top = top
        db.session.commit()
        flash("Editado com sucesso.")
        return redirect(url_for("index"))
    else:
        newsletter_form = NewsletterForm()
        new = New.query.get(id)
        return render_template("edit.html", newsletter_form=newsletter_form, new=new)


@app.route("/excluir/<int:id>")
@login_required
def delete(id):
    new = New.query.get(id)
    db.session.delete(new)
    db.session.commit()
    image = os.path.join(app.root_path, "static", "images", "img{0}.png".format(id))
    os.remove(image)
    flash("Excluído com sucesso.")
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Desconectado.")
    return redirect(url_for("index"))


@app.route("/gerador/<info>")
@app.route("/gerador", defaults={"info": None})
@login_required
def gerador(info):
    i = Admin("admin", generate_password_hash("1234"), "Administrador", "admin@admin.com")
    db.session.add(i)
    db.session.commit()
    return "OK"