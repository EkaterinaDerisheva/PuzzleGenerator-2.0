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
    df_MateIn2_Generated = generate(puzzle)

    return Response(df_MateIn2_Generated.to_json(orient="records"), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
