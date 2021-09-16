from flask import Flask, render_template, request, redirect
from flask import Blueprint




transactions_blueprint = Blueprint("transactions", __name__)