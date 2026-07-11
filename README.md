# Sistema de Procesamiento de Transacciones Tolerante a Fallos

Este módulo proporciona una solución para la carga y validación de transacciones financieras a partir de archivos de texto planos. 
Está diseñado bajo el principio de **tolerancia a fallos**, lo que le permite omitir registros corruptos o incompletos sin detener 
la ejecución del programa principal.

## Requisitos

- **Python 3.x**
- Un archivo de origen de datos nombrado `transacciones_corruptas.txt`.

## Características Principales

1. **Encapsulamiento y Validación:** La clase `Transaccion` utiliza propiedades (`@property` y `@setter`)
    para asegurar que los montos sean enteros positivos y que no superen el límite financiero de 100 millones.
3. **Lectura Robusta (Tolerante a Fallos):** El cargador analiza línea por línea dentro de bloques `try/except`.
   Si un registro presenta datos insuficientes (`TypeError`) o valores fuera de rango/no numéricos (`ValueError`),
   se genera una alerta en la consola y el proceso continúa con la siguiente línea.

## Estructura del Archivo de Entrada

El archivo `transacciones_corruptas.txt` debe contener un registro por línea separado por comas con el formato: `ID_CLIENTE,TIPO_TRANSACCION,MONTO`.

**Ejemplo de contenido:**
```text
101,Depósito,50000
102,Retiro,-1500
103,Depósito
104,Retiro,120000000
105,Depósito,25000
