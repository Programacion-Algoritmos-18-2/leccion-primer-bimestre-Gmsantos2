/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio_1;

/**
 *
 * @author Gerson
 */
public class EmpleadoPorHoras extends Empleado {

    private double numero_horas = 0.0;  // inicializacion de variables 
    private double valor_hora = 0.0;

    //FUNCIONES DONDE VAMOS A AGREGAR EL VALOR QUE SE INGRESA POR EL  MAIN Y LO OBTENEMOS PARA PODER PRESENTARLO AL FINAL
    public void agregar_numero_horas(double q) {
        numero_horas = q;
    }

    public double obtener_numero_horas() {
        return numero_horas;
    }

    public void agregar_valor_hora(double b) {
        valor_hora = b;
    }

    public double obtener_valor_hora() {
        return valor_hora;
    }

    public double calcular_sueldo_final() {
        double q = numero_horas * valor_hora;
        return q;
    }
     @Override //decorador
    public String toString() { // metodo sobreescribir

        return String.format("%s\nNumero horas: %.2f\nValor hora: %.2f\nSueldo final:%.2f",super.toString(),obtener_numero_horas(),obtener_valor_hora(),calcular_sueldo_final()); //presenta la salida
    }
}
