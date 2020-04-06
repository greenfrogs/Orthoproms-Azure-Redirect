from flask import Flask, redirect

app = Flask(__name__)
new_url = 'http://orthoproms.uksouth.cloudapp.azure.com'


@app.route('/')
def root():
    return redirect(new_url, code=302)


@app.route('/<path:page>')
def anypage(page):
    return redirect('{new_url}/{page}'.format(page=page, new_url=new_url), code=302)


if __name__ == '__main__':
    app.run()
