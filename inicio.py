# -*- coding: utf-8 -*-
from listas import *

class Inicio:

    """ ABRIR ARCHIVO CON EJEMPLOS POSITIVOS"""
    def archivo_ejemplos_pos(self):
        #Abrir .txt con Ejemplos Positivos
        expresiones = open("EjemplosPositivos.txt")
        linea = [" "]
        #Objeto de listas
        self.listas = listas()
        #Valores Base
        ejemplo = expresiones.readline().split(' ')
        self.listas.insertar(1, ejemplo[0])
        self.listas.insertar(2, ejemplo[1])
        self.listas.insertar(3, ejemplo[2])
        self.listas.insertar(4, ejemplo[3])
        
        while linea != '':
            #Leer linea a linea del .txt
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
            #Evaluar ejemplo base con cada ejemplo (positivo o negativo)
                #linea[:-1] todos menos el ultimo elemento
            self.evaluar_ejemplo(True, ejemplo[:-1], linea[:-1], listas)
        return (listas)

        """ ABRIR ARCHIVO CON EJEMPLOS NEGATIVOS"""
    def archivo_ejemplos_neg(self, listas):
        #Abrir .txt con Ejemplos Negativos
        expresiones = open("EjemplosNegativos.txt")
        linea = [" "]
        ejemplo = expresiones.readline().split(' ')
        
        while linea != '':
            #Leer linea a linea del .txt
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
            self.evaluar_ejemplo(False, ejemplo[:-1], linea[:-1], listas)
        return (self.listas.recuperar())

    """ ABRIR ARCHIVO CON EJEMPLOS """
    def abrir_archivo_descripcion(self):
        descripcion = open("Descripcion.txt")
        desc1 = descripcion.readline().split(' ')
        desc2 = descripcion.readline().split(' ')
        return (desc1,desc2)
    
    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("Resultados.txt", "w")       
        busquedas.write(str(resultado))
        busquedas.close()

    """ EVALUA LOS EJEMPLOS POSITIVOS Y NEGATIVOS """
    def evaluar_ejemplo(self, ejemplo, base, valores, listas):
        #Si es un Ejemplo Positivo
        if ejemplo:
            #Variables auxiliares
            i = 0
            #Mientras hayan valores
            while i < len(valores):
                if base[i] != valores[i]:
                    #Valor en diferencia    
                    self.listas.insertar((i+1), valores[i])
                i += 1
        #Si es un Ejemplo Negativo
        else:
            #Variables auxiliares
            i = 0
            #Mientras hayan valores
            while i < len(valores):
                if base[i] != valores[i]:
                    #Valor en diferencia    
                    self.listas.insertar((i+1),'NO '+valores[i])
                i += 1

    """ IMPRESION DE EJEMPLOS EN DIFERENCIA """
    def impresion (self, resultado, descripcion):
        #Variables auxiliares
        i = 0
        impresion = ''
        impresion += ' '.join(descripcion[0])+'\n'
        #Mientras hayan elementos
        while i < len(resultado):
            impresion += str(descripcion[1][i])+' : '+' / '.join(resultado[i])+'\n'
            i += 1
        return impresion

inicio = Inicio()
#Obtiene diferencias con ejemplos positivos
listas = inicio.archivo_ejemplos_pos()
#Obtiene diferencias con ejemplos negativos
salida2 = inicio.impresion(inicio.archivo_ejemplos_neg(listas), inicio.abrir_archivo_descripcion())
#Diferencias Finales
inicio.escribir_archivo(salida2)
