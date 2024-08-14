---
tags:
  - Entity
---
Son Unidades Organizativas dentro de un [[País]] que agrupan [[Ontology/Cliente|Clientes]] en función de un criterio, generalmente pertenecientes a un mismo  [[Sector]]. 


Los [[Gerente|Gerentes]] y [[Director|Directores]]] están asociados a una [[Oficina]] y opcionalmente a una [[Unidad de Negocio]]



# Atributos

| Nombre        | Descripción                                                         | Tipo         |
| ------------- | ------------------------------------------------------------------- | ------------ |
| Código*       | Identificador único de la Unidad                                    | Autonumérico |
| Nombre*       | Nombre de la Unidad                                                 | Alfanumérico |
| [[Oficina]]   |                                                                     | [[Oficina]]  |
| Responsable   |                                                                     | [[Usuario]]  |
| Fecha de Baja | Si existe una fecha de baja la Unidad de Negocio está deshabilitada | Fecha        |

# Reglas

- Las Unidades de Negocio que tienen una fecha de baja informada (no nula) no estarán disponibles en la aplicación. Por ejemplo, no se mostrarán en los selectores de Unidad de Negocio. 
- Para poder dar de baja una Unidad de Negocio será necesario que no exista ningún Usuario asociado a ella