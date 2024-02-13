""" This program is used to host and render a simple portfolio website, 
    and to experiment with a rudimentary CMS"""

from factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=3001)
