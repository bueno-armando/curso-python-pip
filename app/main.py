import csv_utils
import utils
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  countries = list(map(lambda x : x['Country/Territory'], data))
  percents = list(map(lambda x : x['World Population Percentage'], data))
  '''

  dataFrames = pd.read_csv("data.csv")
  # taking only south america countries with list comprehension
  dataFrames = dataFrames[dataFrames['Continent'] == 'Africa']

  countries = dataFrames['Country/Territory'].values
  percents = dataFrames['World Population Percentage'].values

  charts.generate_pie_chart(countries, percents) 
  

  data = csv_utils.read_csv('data.csv')

  country = input("Country => ")

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()