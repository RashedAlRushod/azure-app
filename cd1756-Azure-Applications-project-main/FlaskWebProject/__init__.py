"""
Flask application package initialization.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# ────────── Flask app setup ──────────
app = Flask(__name__)
app.config.from_object(Config)

# ────────── Logging ──────────
logging.basicConfig(level=logging.INFO)      # root logger
app.logger.setLevel(logging.INFO)            # app-specific logger

# ────────── Extensions ──────────
Session(app)                     # server-side session store
db = SQLAlchemy(app)             # SQLAlchemy ORM
login = LoginManager(app)        # Flask-Login
login.login_view = "login"       # redirect endpoint for @login_required

# ────────── Import routes last ──────────
import FlaskWebProject.views      # noqa: E402  (kept at end to avoid circular import)
