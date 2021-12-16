""" Separation controller """

from flask import render_template
from app.controllers.controller import ControllerBase

class SeparationController(ControllerBase):
    """ Index response controller """
    @staticmethod
    def get():
        """ Index Route Response """
        return render_template('separation.html')
