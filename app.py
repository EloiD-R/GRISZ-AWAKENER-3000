"""IMPORTS"""
import time
import flask
from flask import Response
from flask import render_template
import time_management.time_getter


"""CODE"""
app = flask.Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/day_month')
def day_month():
    day_number, day_name, month_number, month_name = time_management.time_getter.get_specific_data_from_worldtimeapi()

@app.route('/time-stream')
def time_stream():
    def generate():
        while True:
            hour, minutes, seconds = time_management.time_getter.get_specific_data_from_worldtimeapi(4, 5, 6)
            formatted_time = f"data: {hour}:{minutes}:{seconds}\n\n"
            yield formatted_time
            time.sleep(1)  # Wait for 1 second before sending the next update

    return Response(generate(), mimetype='text/event-stream')


"""RUNNING"""
if __name__ == '__main__':
    app.run()