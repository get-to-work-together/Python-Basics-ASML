import os
import json
import re

from ..persistence.store_in_sqlite import load, update_status, purge
from ..models.monitor import monitor
from ..models.utils.query_parser import query_parser, query_matcher

from flask import Flask, render_template, request, redirect

app = Flask(__name__,
            template_folder = 'templates',
            static_url_path = '',
            static_folder = 'static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sites")
def sites():
    dirname = 'data'
    filename = 'sites_to_monitor.json'
    try:
        with open(os.path.join(dirname, filename)) as f:
            sites_to_monitor = json.load(f)
            sites = [site['url'] for site in sites_to_monitor]
    except:
        sites = []
    return render_template('sites.html', sites = sites)


@app.route("/results", methods = ['GET', 'POST'])
def get_results():

    if request.method == 'POST':
        title = request.form['title']
        if 'watch_line' in request.form:
            new_status = 'watch'
        elif 'ignore_line' in request.form:
            new_status = 'ignore'
        update_status(title, new_status)

    query = ''
    try:
        query = request.args.get('keywords').strip()
        if not query:
            query = ''
        keywords = query_parser(query)
    except:
        keywords = []

    results = load()

    if keywords:
        results = [r for r in results if query_matcher(keywords, r['html'])]

    results = [r for r in results if r['status'] != 'ignore'] + \
              [r for r in results if r['status'] == 'ignore']
    return render_template('results.html', results = results, keywords = query)


@app.route("/update_sites", methods = ['GET', 'POST'])
def update_sites():
    monitor()
    return redirect("/results")


def main():
    purge()
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()