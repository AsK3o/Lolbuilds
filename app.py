from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    build = None
    if request.method == 'POST':
        champion = request.form['champion']
        enemy = request.form['enemy']
        role = request.form['role']

        # Simule un build (à remplacer plus tard par des appels API)
        sample_builds = [
            {
                'title': f"Build standard pour {champion} ({role}) vs {enemy}",
                'items': ['Éclipse', 'Griffe du rôdeur', 'Youmuu'],
                'runes': ['Conquérant', 'Présence d'esprit', 'Coup de grâce'],
                'skills': 'Q > E > W'
            },
            {
                'title': "Build alternatif",
                'items': ['Draktar', 'Collecteur', 'Serylda'],
                'runes': ['Électrocution', 'Ruée offensive', 'Chasseur ultime'],
                'skills': 'Q > W > E'
            }
        ]
        build = random.choice(sample_builds)
    return render_template('index.html', build=build)