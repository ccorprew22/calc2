""" Pylint controller """

from flask import render_template
from app.controllers.controller import ControllerBase

class PylintController(ControllerBase):
    """ Index response controller """
    @staticmethod
    def get():
        """ Index Route Response """
        return render_template('pylint.html')
