import numpy as np
import pandas as pd
import os

class Tabla:
    def __init__(self):
        self.df={}

    def crear_df(self,n):
        print('Ahora debera ingresar los nombres de cada columna\n')
        for i in range(n):
            col_name=input(f'Nombre de la columna \'{i+1}\': ')
            if col_name in self.df:
                pass
            else:
                self.df[col_name]=[]
        df_final=pd.DataFrame(self.df)
        # Verifico la existencia del archivo
        # si no existe lo creo
        while True:
            name_df=input('\nIngrese el nombre de su Dataframe: ')
            name_df= '_'.join(name_df.split()) if ' ' in name_df else name_df
            try:
                pd.read_csv(f'./Datasets/{name_df}.csv')
                print('Ya existe un archivo con este nombre.')
            except FileNotFoundError:
                df_final.to_csv(f'./Datasets/{name_df}.csv',index=False)
                break
                
            


    def add_register(self):
        ver_dfs=input('Visualizar los Dataframes existentes? (SI/NO): ').upper()
        if ver_dfs=='SI':
            self.listar_df()
        while True:
            try:
                name=input('Ingrese el nombre, textual, del Dataframe: ')
                df=pd.read_csv(f'./Datasets/{name}.csv')
                break
            except:
                print('ERROR. El Dataframe no existe\n')
            
        validacion=True

        opt_impresion=input('Visualizar Dataframe? (SI/NO): ').upper()
        if opt_impresion=='SI':
            self.imprimir(name)
        
        while validacion:
            row=[]

            col_df=list(df.columns)
            for col in col_df:
                dato=input(f'Ingrese un dato para la columna {col}: ')
                if dato.isdigit():
                    row.append(int(dato))
                else:
                    row.append(dato)

            df_add=pd.DataFrame([row],columns=col_df)
            df=pd.concat((df,df_add),ignore_index=True)
            df.to_csv(f'./Datasets/{name}.csv',index=False)
            
            opt_impresion=input('Visualizar Dataframe? (SI/NO): ').upper()
            if opt_impresion=='SI':
                self.imprimir(name)

            opt=input('Seguir agregando registros? (SI/NO): ').upper()
            if opt!='SI':
                validacion=False


    def buscar(self):
        ver_dfs=input('Visualizar los Dataframes existentes? (SI/NO): ').upper()
        if ver_dfs=='SI':
            self.listar_df()
        while True:
            try:
                name=input('Ingrese el nombre, textual, del Dataframe: ')
                df=pd.read_csv(f'./Datasets/{name}.csv')
                break
            except:
                print('ERROR. El Dataframe no existe\n')
        
        validacion=True

        ver_df=input('Ver Dataframe? (SI/NO): ').upper()
        if ver_df=='SI':
            self.imprimir(name)
        

        while validacion:
            features=list(df.columns)
            feature=input('Ingrese el nombre de la columna por cual buscar: ')
            if feature in features:
                try:
                    dato=input('Ingrese el dato a buscar?: ')
                    if dato.isdigit():
                        mask=df[feature].apply(lambda row: True if int(dato)==row else False)
                    else:
                        mask=df[feature].apply(lambda row: True if dato in row else False)
                except:
                    print('ERROR. Verifique el dato ingresado.')   
                     
                df_temp=df[mask]
                print(df_temp) if len(df_temp)>0 else print('\nEl dato ingrsado no coincide con ningun registro')
            else:
                print('\nERROR. El nombre de la columna que ingreso no exite.')

            opt=input('\nContinuar buscando con el mismo Dataframe? (SI/NO): ').upper()
            if opt=='SI':
                validacion=True
                ver_df=input('Ver Dataframe? (SI/NO): ').upper()
                if ver_df=='SI':
                    self.imprimir(name)
            else:
                validacion=False
            


    def imprimir(self,name=None):
        ver_dfs=input('Visualizar los Dataframes existentes? (SI/NO): ').upper()
        if ver_dfs=='SI':
            self.listar_df()

        if name==None:
            while True:
                try:
                    name=input('\nIngrese el nombre, textual, del Dataframe: ')
                    df=pd.read_csv(f'./Datasets/{name}.csv')
                    break
                except:
                    print('ERROR. El nombre no pertenece a un Dataframe.')
            print(df) if len(df)>0 else print('No hay registros')
        else:
            df=pd.read_csv(f'./Datasets/{name}.csv')

            print(df) if len(df)>0 else print('No hay registros')

    def listar_df(self):
        lista_dfs= os.listdir('./Datasets')
        for dfs in lista_dfs:
            print(dfs)
                

def menu():
    print('\n'+'-'*10+'MENU'+'-'*10)
    print('1. Crear mi Dataframe\n2. Agregar registros a un Dataframe\n3. Visualizar Dataframe\n4. Buscar Registro\\s en un Dataframe\n5. Visualizar los Dataframes\n0. Finalizar App')

def opciones(val):
    mi_df=Tabla()
    if val == 1:
        while True:
            try:
                n=int(input('Ingrese la cantidad de columnas de su Dataframe: '))
                break
            except ValueError:
                print('ERROR. Ingrese un valor numerico.')

        mi_df.crear_df(n)

    elif val == 2:
        #name_df=input('Ingrese el nombre, textual, del Dataframe: ')
        mi_df.add_register()
    elif val == 3:
        #name_df=input('Ingrese el nombre, textual, del Dataframe: ')
        mi_df.imprimir()
    elif val==4:
        #name_df=input('Ingrese el nombre, textual, del Dataframe: ')
        mi_df.buscar()
    elif val==5:
        mi_df.listar_df()
