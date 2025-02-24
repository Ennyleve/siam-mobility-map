from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map_view():
    return render_template('siam_square_map.html')  # แสดงแผนที่ที่คุณสร้าง

if __name__ == "__main__":
    app.run(debug=True)