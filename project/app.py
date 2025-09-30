from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key"

# صفحة تسجيل الدخول + التسجيل
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/packages')
def packages():
    return render_template("packages.html")
@app.route('/sign')
def sign():
    return render_template("login.html")
@app.route('/cancun')
def cancun():
    return render_template("cancun.html")
@app.route('/capetown')
def capetown():
    return render_template("capetown.html")
@app.route('/dubai')
def dubai():
    return render_template("dubai.html")
@app.route('/egypt')
def egypt():
    return render_template("egypt.html")
@app.route('/london')
def london():
    return render_template("london.html")
@app.route('/maldive')
def maldive():
    return render_template("maldive.html")
@app.route('/marrakech')
def marrakech():
    return render_template("marrakech.html")
@app.route('/newyourk')
def newyourk():
    return render_template("newyourk.html")
@app.route('/niagarafalls')
def niagarafalls():
    return render_template("niagarafalls.html")
@app.route('/paris')
def paris():
    return render_template("paris.html")
@app.route('/riodejaneiro')
def riodejaneiro():
    return render_template("riodejaneiro.html")
@app.route('/rome')
def rome():
    return render_template("rome.html")
@app.route('/spain')
def spain():
    return render_template("spain.html")
@app.route('/thailand')
def thailand():
    return render_template("thailand.html")
@app.route('/tokyo')
def tokyo():
    return render_template("tokyo.html")
@app.route('/zanzibarisland')
def zanzibarisland():
    return render_template("zanzibarisland.html")
@app.route('/Reservetion')
def Reservetion():
    return render_template("Reservetion.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("login-email")
        password = request.form.get("login-password")

        # تحقق من البيانات (ده مثال فقط)
        if email == "test@test.com" and password == "123":
            session["logged_in"] = True
            session["user"] = email
            return redirect(url_for("home"))
        else:
            return "Invalid credentials, try again."

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()  # يمسح كل حاجة من السيشن
    return redirect(url_for("home"))

@app.route("/register", methods=["POST"])
def register():
    # هنا ممكن تخزن بيانات المستخدم في DB
    name = request.form.get("register-name")
    email = request.form.get("register-email")
    password = request.form.get("register-password")

    # لسه مش مربوط بقاعدة بيانات، هنرجعه عادي على الهوم
    session["logged_in"] = True
    session["user"] = email
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
