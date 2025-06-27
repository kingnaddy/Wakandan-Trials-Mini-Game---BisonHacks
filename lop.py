from flask import Flask, render_template, request, redirect, url_for, session
import random, time

app = Flask(__name__)
app.secret_key = 'wakanda_secret_key'

vibranium_options = ["Type A: Resonant Isotope", "Type B: Neural Conductive", "Type C: Kinetic Absorptive"]
vibranium_clues = [
    "Used in Black Panther suit, absorbs impact energy",
    "Powers Wakandan neural networks",
    "Found in deeper mines, glows under UV light"
]
correct_matches = {0: 2, 1: 1, 2: 0}

@app.route('/')
def intro():
    session.clear()
    session['game_state'] = 'mission1'
    session['start_time'] = time.time()
    session['intrusion_count'] = 0
    session['scanned_vibranium'] = 0
    session['current_clue'] = 0
    return render_template('intro.html')

@app.route('/mission1', methods=['GET', 'POST'])
def mission1():
    if 'game_state' not in session or session['game_state'] != 'mission1':
        return redirect(url_for('intro'))

    clue_index = session.get('current_clue', 0)
    if request.method == 'POST':
        selected = int(request.form.get('vibranium_option'))
        if selected == correct_matches[clue_index]:
            session['scanned_vibranium'] += 1
        else:
            session['intrusion_count'] += 1

        session['current_clue'] += 1
        if session['current_clue'] >= len(vibranium_clues):
            if session['scanned_vibranium'] >= 2 and session['intrusion_count'] < 3:
                session['game_state'] = 'win'
                return redirect(url_for('win'))
            else:
                session['game_state'] = 'lose'
                return redirect(url_for('lose'))

        return redirect(url_for('mission1'))

    return render_template(
        'mission1.html',
        clue=vibranium_clues[clue_index],
        options=vibranium_options,
        scanned=session.get('scanned_vibranium', 0),
        intrusions=session.get('intrusion_count', 0),
    )

@app.route('/win')
def win():
    return render_template('win.html', scanned=session['scanned_vibranium'], intrusions=session['intrusion_count'])

@app.route('/lose')
def lose():
    return render_template('lose.html', scanned=session['scanned_vibranium'], intrusions=session['intrusion_count'])

if __name__ == '__main__':
    app.run(debug=True)
