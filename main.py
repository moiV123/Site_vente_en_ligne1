from flask import Flask, render_template, request, redirect, url_for, session  # type: ignore
import pymongo  # type: ignore
import os
import certifi

app = Flask(__name__)

mongo_uri = "mongodb+srv://valentinblp_db_user:MOtX6wfcNPOqw76Z@cluster0.61gvza5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
            if request.form["password"] == user["user_password"]:
                session["user_id"] = request.form["username"]
                return redirect(url_for("index"))
            else:
                return render_template("login.html", erreur="Mot de passe incorrect.")
        else:
            return render_template("login.html", erreur="Utilisateur non trouvé.")
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)