{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["","import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return \"Hello World\"","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":2}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":24},"action":"remove","lines":["return \"Hello World\""],"id":3},{"start":{"row":8,"column":4},"end":{"row":8,"column":40},"action":"insert","lines":["return render_template(\"index.html\")"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":9},"action":"remove","lines":["hello"],"id":4},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["n"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["d"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["e"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["x"]}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":5},{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return render_template(\"index.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":8,"column":40},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":12,"column":40},"action":"insert","lines":["@app.route('/about')","def about():","    return render_template(\"about.html\")"],"id":8}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":10},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return render_template(\"index.html\")","    ","@app.route('/about')","def about():","    return render_template(\"about.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":13},{"start":{"row":0,"column":0},"end":{"row":23,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":14},{"start":{"row":0,"column":0},"end":{"row":28,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":15},{"start":{"row":0,"column":0},"end":{"row":28,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\", page_title=\"About\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":28,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\", page_title=\"About\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":16},{"start":{"row":0,"column":0},"end":{"row":32,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company_data=data)","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":32,"column":23},"action":"remove","lines":["import os","import json","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company_data=data)","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":17},{"start":{"row":0,"column":0},"end":{"row":32,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":32,"column":23},"end":{"row":32,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1569426023561,"hash":"33818caa765e510c6588ebb77f72d865665da507"}