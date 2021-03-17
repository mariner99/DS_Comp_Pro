import scrapper as sc
import pandas as pd

path = '/Users/SarthakPratik/Desktop/ds_comp_pro/chromedriver'

df = sc.get_jobs('data scientist',15,False,path,15)

df