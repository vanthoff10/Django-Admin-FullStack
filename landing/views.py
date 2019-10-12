from django.shortcuts import render
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

from django.http import HttpResponse


def index(request):
    return render(request)

