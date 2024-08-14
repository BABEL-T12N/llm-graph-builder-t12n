---
tags:
  - UI_Component
---
Este Componente permite seleccionar un [[Cliente]] como parte generalmente de un flujo más grande. 
Este Componente sustituiría a la lista de selección ya que la lista de Clientes es muy larga y no sería manejable. 
El Usuario debe seleccionar el [[Cliente]] marcando la casilla a la derecha del nombre de cada Cliente. 
Para localizar el Cliente rápidamente el Usuario puede recorrer la lista completa o utilizar el filtro superior que filtra por  código o nombre del Cliente. 

![[Selector de Clientes Component.png]]

El componente tiene los siguientes componentes:
- Título. Este título es dinámico y se establece al cargar el componente. Por tanto puede mostrar distintos títulos en función del flujo que le invoca. En la imagen por ejemplo, aparece cómo "Crear Oportunidad"
- Caja de Texto para filtrar la lista de Clientes por código o nombre
- Lista en forma de tabla con la siguiente estructura: selector, nombre del Cliente y estado. Sólo se puede seleccionar un Cliente
- Botón Continuar. Este botón sólo está activo si hay un Cliente Seleccionado. Una vez se pulsa Continuar el componente deja paso al resto del flujo. 