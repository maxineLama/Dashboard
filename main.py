import dash
from dash import dcc
from dash import dash_table
from dash import html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pf = pd.read_csv('population-francaise.csv',delimiter=";")
Medecins= pd.read_csv('Medecin_par_departement_par_annee.csv')
pf=pf.sort_values(by = 'Code Departement')
pf=pf.drop(columns=['geom'])
pf[['Lat','Lon']] = pf.coords.str.split(",",expand=True,)
#Coordonnée gps du centre de la France#
LAT_FOCUS=46.227638
LON_FOCUS=2.2137499


"""
Création de la premièrecarte 
"""

fig = go.Figure(data=go.Scattergeo(
		
	text = pf[['Departement','Population']] ,
	lat=pf['Lat'],
	lon=pf['Lon'],
	textfont = {"color": 'black',
				"family":'Times New Roman',
				"size":18},
	textposition="top center",
	mode ='markers',
	marker = dict(
		size = 9,
		opacity = 0.8,
		reversescale = True,
		autocolorscale = False,
		symbol = 'square',
		line = dict(
			width=1,
			color='rgba(0, 0, 0)'
		)

	 )
))



fig.update_layout(

	height=650,
	width=900,
	margin={"r":300,"t":0,"l":0,"b":100},
	geo = dict(
		scope='europe',
		center=dict(lat=LAT_FOCUS,lon=LON_FOCUS ),
		showland = True,
		projection_scale=6.6
	)
)

"""
Création dela seconde carte 
"""
fig2 = go.Figure(data=go.Scattergeo(
		
	text = Medecins[['dep_insc','2020']] ,
	lat=pf['Lat'],
	lon=pf['Lon'],
	textfont = {"color": 'black',
				"family":'Times New Roman',
				"size":18},
	textposition="top center",
	mode ='markers',
	marker = dict(
		size = 9,
		opacity = 0.8,
		reversescale = True,
		autocolorscale = False,
		symbol = 'circle',
		line = dict(
			width=1,
			color='rgba(0, 0, 0)'
		)
	)
))

fig2.update_layout(

	height=650,
	width=900,
	margin={"r":300,"t":0,"l":0,"b":100},
	geo = dict(
		scope='europe',
		center=dict(lat=LAT_FOCUS,lon=LON_FOCUS ),
		showland = True,
		projection_scale=6.6
	)
)

"""
Main 
"""
head_data1= pf.head()
head_data2 = Medecins.head()

"""
Creation d'un tableau afin de reutiliser les données dans l'histogramme
"""
d = {'Années': ["2012","2013","2014","2015","2016","2017","2018","2019","2020"] , 'Medical Workforce': [215930,217598,219566,221001,222453,223739,225046,225064,227298] }
effectifs_tab = pd.DataFrame(data=d,columns=['Années', 'Medical Workforce'])

"""
Création de l'histogramme
"""
fig3 = px.histogram(effectifs_tab,x="Années",y="Medical Workforce") 


"""
Main 
"""
if __name__ == '__main__':
	
	app = dash.Dash(__name__)
	
	app.layout = html.Div(children=[
		
  
		
		html.H1(children='Etude de sur la répartition des médecins sur le département Français\n'),
		html.H2(children='Pour ce faire, nous avons choisis deux jeux de données disponible sur des sites publics et libre d\'accès afin de pouvoir comparer les disparités des effectifs médicales entre les département français \n'),
		html.H3(children='Jeu de données contenant les coordonnées et le nombre d\'habitant de chaque département français'),
		dash_table.DataTable(
        	id='table',
        	columns=[{"name": i, "id": i} for i in head_data1.columns],
        	data=head_data1.to_dict('records')),
		html.H3(children='Jeu de données contenant les coordonnées et le nombre de médecins par département français\n'),
		dash_table.DataTable(
        	id='table2',
        	columns=[{"name": i, "id": i} for i in head_data2.columns],
        	data=head_data2.to_dict('records')),

		html.H4(children='Le but de ce dashboard est d\'exposer et de comparer la variation et les disparités de l\'effectif médical en France\n'),
		html.Div(children=[
			html.Div(children=[
				html.H3(children='Ci-dessous une carte représantant les differents départements français, en survolant à l\'aide de votre souris les différents carrés, vous trouverez les coordonnées, le nom et la population totale du département\n'),
				dcc.Graph(
					id='Map',
					figure=fig
				),
			]),

			html.Div(children=[
				html.H3(children='Vous trouverez à présent une deuxieme carte, en survolant à l\'aide de votre souris les différents points, vous trouverez les coordonnées, le nom du département et le nombre total de médecins '),
				dcc.Graph(
					id='Map2',
					figure=fig2
				)
			])
		],style={'color': 'blue'}),
		html.Div(children=[
			html.H3(children='Voici un histogramme comparant le nombre total de médecins exerçant en France de 2012 à 2020 \n'),
			dcc.Graph(
				id='histo',
				figure=fig3
				),
			html.H4(children='On peut observer une légère augmentation global de l\'effectif médical en France, cependant, Certains départements appartenant à ce que l\'on appelle \"La diagonale du vide\" on quant à eux un effectif qui a tendance a diminué'),
		]),
		html.H5(children='Maxine LAMA & Valentin DUMAS'),
	],style={'text-align':'center'})

app.run_server(debug=True)
