---
tags:
  - UserStory
---
## Gestionar Clientes


### Contexto

**Como**: [[Gerente]], [[Director]] o [[Director de Operaciones]]
**Quiero**: Crear y  [[Gestión de Clientes]] en BHZ
**Para**: Mantener un registro actualizado y detallado de los clientes, facilitando la comunicación y gestión de oportunidades.

### Criterios de aceptación

1. **Creación de Cliente**:
    
    - Puedo crear un [[Cliente]] introduciendo información básica y detallada en varios pasos.
    - Puedo guardar la información en estado “Borrador” y finalizar la creación cuando toda la información obligatoria esté completa.
    - El cliente debe pasar por los estados “Borrador”, “Objetivo”, “En validación” y “Prospect” antes de ser activado.
2. **Validación y Activación**:
    - El Control de Gestión debe validar y activar el cliente, asignándole un código correlativo.
    - Recibir notificaciones y correos electrónicos cuando un cliente pase a estado “En validación” y “Prospect”.
3. **Gestión de Clientes**:
    - Puedo modificar datos del cliente y cambiar su estado si soy el [[Responsable de Unidad de Negocio]] o [[Administrador]].
    - Puedo ver información útil del cliente, como contactos y oportunidades abiertas, desde su ficha
4. **Integración**:
    
    - La herramienta debe comunicarse con otros sistemas como SAP y la Intranet para mantener los datos actualizados

