# Project Name

### Project Short Description

## About Project

## Installation

First, 

```bash
npm install
```

then,

- For development: 
```bash
npm run dev
```

- For production: 
```bash
npm run prod
```

If you do not need the server, run the following commands:

```bash
rm -rf client/api node_modules server
npm r axios express lodash module-alias morgan concurrently nodemon
npm install
```

Then in package.json, use the following for scripts:

```json
{
    "dev": "webpack-dev-server --mode development --devtool inline-source-map",
    "prod": "webpack --mode production"
}
```
