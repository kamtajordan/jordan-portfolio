from flask import Flask, render_template, redirect, url_for, abort
import json
import os

app = Flask(__name__)

SUPPORTED_LANGUAGES = ["en", "fr"]
DEFAULT_LANGUAGE = "en"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_content(language):
    if language not in SUPPORTED_LANGUAGES:
        language = DEFAULT_LANGUAGE
    path = os.path.join(DATA_DIR, f"{language}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# ROUTES — HOME
# ============================================================

@app.route("/")
def home():
    return render_template("index.html", lang="en", content=load_content("en"))


@app.route("/fr")
def home_fr():
    return render_template("index.html", lang="fr", content=load_content("fr"))


# ============================================================
# ROUTES — PAGES (EN)
# ============================================================

@app.route("/en/about")
def about_en():
    return render_template("about.html", lang="en", content=load_content("en"))

@app.route("/en/research")
def research_en():
    return render_template("research.html", lang="en", content=load_content("en"))

@app.route("/en/publications")
def publications_en():
    return render_template("publications.html", lang="en", content=load_content("en"))

@app.route("/en/projects")
def projects_en():
    return render_template("projects.html", lang="en", content=load_content("en"))

@app.route("/en/education")
def education_en():
    return render_template("education.html", lang="en", content=load_content("en"))

@app.route("/en/trainings")
def trainings_en():
    return render_template("trainings.html", lang="en", content=load_content("en"))

@app.route("/en/documents")
def documents_en():
    return render_template("documents.html", lang="en", content=load_content("en"))

@app.route("/en/contact")
def contact_en():
    return render_template("contact.html", lang="en", content=load_content("en"))


# ============================================================
# ROUTES — PAGES (FR)
# ============================================================

@app.route("/fr/about")
def about_fr():
    return render_template("about.html", lang="fr", content=load_content("fr"))

@app.route("/fr/research")
def research_fr():
    return render_template("research.html", lang="fr", content=load_content("fr"))

@app.route("/fr/publications")
def publications_fr():
    return render_template("publications.html", lang="fr", content=load_content("fr"))

@app.route("/fr/projects")
def projects_fr():
    return render_template("projects.html", lang="fr", content=load_content("fr"))

@app.route("/fr/education")
def education_fr():
    return render_template("education.html", lang="fr", content=load_content("fr"))

@app.route("/fr/trainings")
def trainings_fr():
    return render_template("trainings.html", lang="fr", content=load_content("fr"))

@app.route("/fr/documents")
def documents_fr():
    return render_template("documents.html", lang="fr", content=load_content("fr"))

@app.route("/fr/contact")
def contact_fr():
    return render_template("contact.html", lang="fr", content=load_content("fr"))


if __name__ == "__main__":
    app.run(debug=True)
