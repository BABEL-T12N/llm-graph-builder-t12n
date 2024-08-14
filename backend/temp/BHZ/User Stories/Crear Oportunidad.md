
**ID:** HU-001

**Descripción:** Como [[Gerente]], quiero crear una nueva [[Oportunidad]] 



**Criterios de Aceptación:**

1. **Pantalla de Creación:**
    - La pantalla de creación debe estar accesible desde la pantalla principal a través de un acceso rápido o desde el menú de Gestión de Oportunidades.
    - La pantalla de creación de Oportunidades estará dividida en varios pasos: Selección o creación del cliente, Datos generales, Selección o creación de contactos y Detalle de la oportunidad.
2. **Paso 1: Selección o creación del [[Cliente]]:**
    - BHZ permite seleccionar un Cliente existente mediante un campo autorellenable.
    - Si el [[Cliente]] no existe previamente no aparecerá en el listado, y el Usuario deberá salir de este flujo y [[Crear un Cliente]].
3. **Paso 2: Datos generales:**
    - Campos obligatorios:
        - Título.
        - Descripción.
        - Oficina a la que pertenece la oportunidad (prellenado con la oficina del Cliente pero modificable).
        - Unidad de Negocio asignada a la oportunidad (prellenado con la unidad de negocio del cliente pero modificable).
    - Campos opcionales:
        - Importe de la Oportunidad.
        - Descuento aplicado.
        - Moneda de la Oportunidad.
        - Probabilidad de ganar la [[Oportunidad]] (valores posibles: 10-25-50-75-90%).
4. **Paso 3: Selección o creación de [[Contactos]]:**
    - Debe permitir seleccionar [[Contactos]] existentes del Cliente mediante un campo autorellenable.
    - Debe haber una opción para crear nuevos contactos sin abandonar el formulario de la oportunidad.
5. **Paso 4: Detalle de la [[Oportunidad]]:**
    - Estado inicial de la oportunidad: Borrador.
    - El Responsable puede guardar la Oportunidad en estado Borrador en cualquier momento y finalizarla para cambiar su estado a Identificada.
    - Otros estados posibles: Preparación de [[Propuesta]], En Validación, Validada, Propuesta Enviada, Ganada, Perdida, Descartada.
6. **Transiciones de Estado:**
    - La Oportunidad pasa de Borrador a Identificada automáticamente cuando está completada al 100% y se pulsa "Finalizar".
    - Solo [[Colaborador|Colaboradores]] y Responsables de la Oportunidad pueden cambiar su estado.
    - Una vez validada, se pueden hacer modificaciones que reinicien el ciclo de validación, manteniendo el historial de versiones de Propuestas.
7. **Notificaciones:**
    - Enviar notificaciones a los colaboradores y responsables cuando la oportunidad cambia de estado.
    - Notificar a los interesados tanto en la aplicación como por correo electrónico cuando una oportunidad requiere su validación o ha sido modificada.
8. **Restricciones:**
    - Solo se pueden crear Oportunidades para clientes en estado Prospect o Activo.
    - No se permite crear Clientes nuevos desde el formulario de creación de Oportunidades.
9. **Campos Adicionales:**
    - Documentación: Permitir adjuntar documentos a la Oportunidad.
    - Fecha de detección y creación de la oportunidad (rellenadas automáticamente).
    - Responsable de la oportunidad y colaboradores (campos autorellenables).

