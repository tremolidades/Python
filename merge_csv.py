import os
from os import listdir
import pandas as pd, numpy as np

if __name__ == '__main__':
	path = input("Ingrese la Ruta donde están los CSV's a Fusionar: ")
	
	def merge_csv(path):
		i = 0
		dataframe = pd.DataFrame
		os.path.islink(path) # Valida si existe ruta especificada.	
		files = listdir(path) # Obtiene nombre de archivos en directorio
		if not(path[-1] =='/' or path[-1] == '\\'):
			path = path + '\\' # Se agrega hash slash punto doble xd si no lo tiene

		np_array_list = []
		destiny_path = input('Ingrese la ruta de destino: ')
		if not os.path.exists(destiny_path):
				os.makedirs(destiny_path) # Crea directorio sólo si no existe
				if(os.path.islink(destiny_path) == False):
					raise

		if(destiny_path[-1] != '/' or destiny_path[-1] != '\\'):
			destiny_path = destiny_path + '\\'

		f=open(destiny_path+'\\merge.csv',"w")
		for file in files:
			i +=1 # Agrega Headers sólo en la primera iteración
			if(i == 1):
				on_file = open(path+file,'r',encoding="utf-8")
				df = pd.read_csv(path+file, header=None,encoding='utf-8',)
				np_array_list.append(df.as_matrix())
			else:
				on_file = open(path+file,'r',encoding="utf-8")
				df = pd.read_csv(path+file, header=0,encoding='utf-8')
				np_array_list.append(df.as_matrix())

		comb_np_array = np.vstack(np_array_list) # La magia de pandas y numpy ~
		big_frame = pd.DataFrame(comb_np_array)
		big_frame.to_csv(destiny_path+'merge.csv',encoding='utf-8-sig',index=False, sep=',',header=False)
		print('Se ha fusionado exitosamente el archivo!')

	try :
		merge_csv(path)
	except:
		print('La ruta especificada no existe o no es válida.')