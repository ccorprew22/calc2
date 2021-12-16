""" OOP controller """

from flask import render_template
from app.controllers.controller import ControllerBase

class OOPController(ControllerBase):
    """ Index response controller """
    @staticmethod
    def get():
        """ Index Route Response """
        return render_template('oop_principles.html')
