# Codegeneration
This readme contains information about codegeneration based on an openapi schema specification.

## Typescript codegen

### First time setup 

Setting up npm environment and installing [openapi-ts package](https://www.npmjs.com/package/@hey-api/openapi-ts):

```bash
npm init
npm install @hey-api/client-fetch && npm install @hey-api/openapi-ts -D
```

Next it is necessary to create a `openapi-ts.config.ts` file in correspondance with the [openapi-ts documentation](https://heyapi.dev/openapi-ts/configuration).

Lastly add the following lines to the `package.json` file:

```json
"scripts": {
    "codegen_typescript": "openapi-ts"
  },
```

Then it is possible to run:

```bash
npm run codegen_typescript
```

### Second time use

If the environment has already been configured it is sufficient to run:

```bash
cd codegen/typescript
npm install
npm run codegen_typescript
```

## CPP codegeneration

Prerequisites: [Java version 11 (JDK)](https://adoptium.net/en-GB/temurin/releases/?version=11)

### First time setup 

Setting up npm environment and installing [openapi-generator-cli package](https://www.npmjs.com/package/@openapitools/openapi-generator-cli):

```bash
npm init
npm install @openapitools/openapi-generator-cli
```

Lastly add the following lines to the `package.json` file:

```json
"scripts": {
    "codegen_cpp": "openapi-generator-cli generate -i ../../openapi/openapi.json -g cpp-pistache-server -o ."
  },
```

Then it is possible to run:

```bash
npm run codegen_cpp
```

To see options for codegeneration using openapi-generator-cli one can use:

```bash
npx openapi-generator-cli list  
```

### Second time use

If the environment has already been configured it is sufficient to run:

```bash
cd codegen/cpp
npm install
run codegen_cpp
```


## Julia codegeneration

Prerequisites: [Java version 11 (JDK)](https://adoptium.net/en-GB/temurin/releases/?version=11)

### First time setup 

Setting up npm environment and installing [openapi-generator-cli package](https://www.npmjs.com/package/@openapitools/openapi-generator-cli):

```bash
npm init
npm install @openapitools/openapi-generator-cli
```

Lastly add the following lines to the `package.json` file:

```json
"scripts": {
    "codegen_julia": "openapi-generator-cli generate -i ../../openapi/openapi.json -g julia-client -o ."
  },
```

Then it is possible to run:

```bash
npm run codegen_julia
```

To see options for codegeneration using openapi-generator-cli one can use:

```bash
npx openapi-generator-cli list  
```

### Second time use

If the environment has already been configured it is sufficient to run:

```bash
cd codegen/julia
npm install
run codegen_julia
```