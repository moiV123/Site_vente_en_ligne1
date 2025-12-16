from flask import Flask, render_template, request, redirect, url_for, session  # type: ignore
import pymongo  # type: ignore
import os
import certifi
#from urllib.parse import quote_plus

#uri = os.environ.get("MONGO_URI")

#try:
#    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
#    print("connected, server_info:", client.server_info())  # will raise on auth/network errors
#except Exception as e:
#    print("Connection failed:", type(e).__name__, e)

app = Flask(__name__)
app.secret_key = "j'ad0re_le_c0de"  # Clé secrète pour les sessions

mongo_uri = "mongodb+srv://valentinblp_db_user:MOtX6wfcNPOqw76Z@cluster0.gukwdqe.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client["Site_vente"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if "username" not in request.form or "password" not in request.form:
            return render_template("login.html", erreur="Veuillez remplir tous les champs.")
        
        db_users = db["users"]
        print("Données reçues :", request.form)  # Debug
        user = db_users.find_one({"username": {"$regex": f"^{request.form['username']}$", "$options": "i"}})
        
        if user:
            print("Utilisateur trouvé :", user)  # Debug
            # Vérification du mot de passe (en clair)
            if request.form["password"] == user["password"]:
                session["user_id"] = request.form["username"]
                return redirect(url_for("index"))
            else:
                return render_template("login.html", erreur="Mot de passe incorrect.")
        else:
            return render_template("login.html", erreur="Utilisateur non trouvé.")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if "username" not in request.form or "password" not in request.form or "confirm_password" not in request.form:
            return render_template("register.html", erreur="Veuillez remplir tous les champs.")
        
        db_user = db["users"]
        new_user = db_user.find_one({"username": request.form["username"]})
        if new_user:
            return render_template("register.html", erreur="Nom d'utilisateur déjà pris.")
        else:
            if request.form["password"] == request.form["confirm_password"]:
                db_user.insert_one({
                    "username": request.form["username"],
                    "password": request.form["password"]
                })
                session["user_id"] = request.form["username"]
                return redirect(url_for("index"))
            else:
                return render_template("register.html", erreur="Les mots de passe ne correspondent pas.")
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)