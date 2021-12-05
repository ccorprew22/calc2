""" Index controller """

from flask import render_template
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """ Index response controller """
    @staticmethod
    def get():
        """ Index Route Response """
        return render_template('index.html')
