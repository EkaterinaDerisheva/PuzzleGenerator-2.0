from flask import Flask, request, Response

import PuzzleManager
from Generator import generate

app = Flask(__name__)

@app.route('/generate-puzzles', methods=['POST'])
def generate_puzzles():
    data = request.get_json()
    id = data['id']

    puzzle_manager = PuzzleManager.Puzzle(id)
    puzzle = puzzle_manager.parse()
    df_generated = generate(puzzle)
    print(df_generated.info())
    return Response(df_generated.to_json(orient="records"), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
