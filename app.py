from flask import Flask, render_template, url_for
import markdown
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<page>')
def show_page(page='index'):
    md_file_path = os.path.join('pages', page + '.md')
    if not os.path.isfile(md_file_path):
        return "Page not found", 404

    with open(md_file_path, 'r') as file:
        content = markdown.markdown(file.read())
    
    return render_template('page_template.html', content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
