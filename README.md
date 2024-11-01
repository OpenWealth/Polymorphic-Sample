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

- Bundle API using `redocly bundle`
- Lint/Validate API using `redocly lint`
- generate boiler plate code for your programming language of choice using ` openapi-generator`

## Specification bundeling

In order to create a single bundled file containing all references ther is a simple bundeling CLI available here:
<https://redocly.com/docs/cli/guides/>

Install the CLI with this command (npm) (you need to have node installed):

```console
npm i -g @redocly/cli@latest
```

Bundle a specification with this command

```console
redocly bundle src/API.yaml --ext yaml --output dist/instrumentAPI.yaml
```

where 'API.yaml' is the OAS source file and 'instrumentAPI.yaml' denotes the bundled output file in YAML format.

## Specification linting/validation

Redocly cli has a default set uf rules embedded when linting and validating your api. In addition rules sets can be configured in an additional configuration file. Custom rules can also be written. The operation also validates embedded/refernced examples.

```console
redocly lint dist/instrumentAPI.yaml
```

## API Server/Client creation

The following project supports the creation of a code basis in various languages for OpenWealth providers (Server) and OpenWealth consumers (clients). This typically consists of an auto-generated object oriented class design of the OAS as well as code for serving and consuming requests.
<https://openapi-generator.tech/>

Installation (npm)

```console
npm install @openapitools/openapi-generator-cli -g
```

Example of creating an AspNetCore server:

```console
openapi-generator-cli generate -i dist/instrumentAPI.yaml -g aspnetcore --package-name API --output generated/aspnetcore --additional-properties=targetFramework=net8.0,useNewtonsoft=false,targetVersion=8.0,nullableReferenceTypes=true,pocoModels=true
```

where the `--additional-properties` define aspnetcore specific depndencies etc.
Note that in the generated code the library `JsonSubTypes` is used to define the discriminator based deserialization into the correct sub class. There are also other techniques that can be used, such as writing a custom JsonConverter in the base class.

Example of a Python FastAPI server:

```console
openapi-generator-cli generate -i dist/instrumentAPI.yaml -g python-fastapi --package-name API --output generated/python-fastapi
```

where 'api-bundled.yaml' is the OAS spec file. There are a number of parameters such as targetFramework, naming conventions etc that can be added to the command.
