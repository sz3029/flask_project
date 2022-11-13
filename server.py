import os
from flask import Flask, request, render_template, g, redirect, Response, \
    redirect, url_for, flash, get_flashed_messages

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir, instance_relative_config=True)

DB_USER = "sz3029"
DB_PASSWORD = "dbuserdbuser"
DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"
DATABASEURI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_SERVER+"/proj1part2"

app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY="ABC",
    # store the database in the instance folder
    DATABASE=DATABASEURI
)

import auth
#import routine
#import event
import core
#import error_handler
#import appointment
#import userprofile
import post
#import admin
#import QA
import about

app.register_blueprint(auth.bp)
#app.register_blueprint(routine.bp)
app.register_blueprint(core.bp)
#app.register_blueprint(error_handler.bp)
#app.register_blueprint(event.bp)
#app.register_blueprint(appointment.bp)
#app.register_blueprint(userprofile.bp)
app.register_blueprint(post.bp)
#app.register_blueprint(admin.bp)
#app.register_blueprint(QA.bp)
app.register_blueprint(about.bp)


if __name__ == "__main__":
    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):

        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.run(host=HOST, port=PORT, debug=True, threaded=True)

    run()