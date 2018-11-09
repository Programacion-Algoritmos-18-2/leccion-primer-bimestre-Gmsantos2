package Ejercicio_1;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Usuario
 */
public class Empleado {

    String nombre = "";           // inicializacion de variables 
    String apellido = "";
    String cedula = "";
    int comision_fija = 0;
    //funciones para agregar y obtenerlas 

    
    
    public void agregar_comision_fija(int comision) {
        comision_fija = comision;
    }

    public int obtener_comision_fija() {
        return comision_fija;
    }

    public void agregar_nombre(String n) {
        nombre = n;
    }

    public String obtener_nombre() {
        return nombre;
    }

    public void agregar_apellido(String a) {
        apellido = a;
    }

    public String obtener_apellido() {
        return apellido;
    }

    public void agregar_cedula(String c) {
        cedula = c;
    }

    public String obtener_cedula() {
        return cedula;
    }
    //funcion para presentar los datos

		
    @Override //decorador
    public String toString() { // metodo sobreescribir

        return String.format("Información de %s %s\n  cedula:%s",obtener_nombre() ,obtener_apellido(), obtener_cedula()); //presenta la salida
    }
}
