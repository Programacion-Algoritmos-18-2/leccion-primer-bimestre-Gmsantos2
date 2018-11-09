package Ejercicio_1;

import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Usuario
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // metodo entrada para el scanner
        Empleado e = new Empleado(); //le damos el objeto e  a la clase empleado
        e.agregar_nombre("Luis"); //mandamos valores a cada uno de los metodos siguientes que llamamos con e
        e.agregar_apellido("Benitez");
        e.agregar_cedula("1110001");
        e.toString(); //llamo al metodo presentar datos

        EmpleadoPorHoras e1 = new EmpleadoPorHoras();
        System.out.println("Ingrese su su nombre:\n");//pedimos por teclado que ingrese el nombre y alamcenamos en una variable
        String nombre = entrada.nextLine();
        e1.agregar_nombre(nombre);   // le mandamos  lo que ingreso el usuario a la funcion 
        e1.agregar_apellido("Andrade"); // mandamos valores a cada uno de los siguientes  funciones 
        e1.agregar_cedula("112233");
        e1.agregar_numero_horas(20.2);
        e1.agregar_valor_hora(15);
        System.out.println(e.presentar_datos()); //presentamos los datos print
        
        EmpleadoFijo e2 = new EmpleadoFijo(); //le damos el objeto e2 a la clase empleado fijo
        e2.agregar_sueldo(300.2); // mandamos valores float a la funcion agregar sueldo
        e2.descuento_seguro = 10 ;//porcentaje 
        System.out.println("Ingrese comision:\n"); // pedimos por teclado que ingrese la comision y alamcenamos en una variable
        float comision = entrada.nextFloat();
        e2.agregar_comision_fija(comision); //la variable con el nuevo tipo le mandamos a la funcion e2
        e2.nombre = "Ana"; // mandamos valores a cada uno de los siguientes  funciones e2
        e2.apellido = "Diaz";
        System.out.println(e2.presentar_datos()); //presentamos los datos
    }

}
