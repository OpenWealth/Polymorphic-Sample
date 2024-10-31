# Polymorphic-Sample

A minimal API to display approaches to polymorphic behaviour.

Polymorphism and inheritance are core principles of object-oriented programming (OOP).

**Inheritance** allows a class (called a "subclass" or "derived class") to inherit attributes and methods from another class (called a "superclass" or "base class"). Think of it as the process of a child inheriting traits from their parent.

**Polymorphism** means "many forms". It allows methods to do different things based on the object it is acting upon, even if they share the same name.

In our OAS3.1 specifications we make use of the polymorphism and inheritance feature. It is described in detail under the following two links:

[Composition and Inheritance](https://spec.openapis.org/oas/latest.html#composition-and-inheritance-polymorphism)
[Discriminator usage](https://spec.openapis.org/oas/latest.html#discriminator-object)

Redocly - a widely used toolset for OAS - describes the strategies of polymorphism implementation [here](https://redocly.com/docs/resources/discriminator)

In general there are two techniques described:

- oneOf/anyOf in combination with discriminator understood as a 'super schema'
- discriminator in the 'parent schema' combined with allOf in the 'child schema'


The allOf approach shows advantages in code generation, such as proper implementation of inheritance in the class model whereas the onOff approach makes use of common JsonSchema validation techniques and technologies, yet is less clean in code creation.

This repository displays the two techniques as a sample api definition (OAS3.1) in two versions.

The components of the api's can be found in the [src](./src) folder.
The bundled api's are located in the [dist](./dist) folder:
- [API with oneOf approach](./dist/instrumentAPI-oneOf.yaml) with [Documentation as html](./dist/instrumentAPI-oneOf.html)
- [API with allOf approach](./dist/instrumentAPI.yaml) with [Documentation as html](./dist/instrumentAPI.html)

The [generated](./generated) folder contains samples of generated code in common languages as csharp, java and python.

In order to reproduce the bundling and code generation process follow these steps:

TBD
