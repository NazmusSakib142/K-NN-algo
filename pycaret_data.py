from pycaret.datasets import get_data
iris=get_data('iris')
from pycaret.classification import *
exp=setup(iris,target='species')
compare_models()
//
from pycaret.datasets import get_data
a=get_data('index')
