
# Fonoma Back-end Test

Api desarrollada con FastApi y desplegada utilizando contenedores de Docker. Utiliza redis para el manejo de caché.





## Demo

Documentacion ofrecida por OpenApi:
https://fonoma-back-end-test.onrender.com/docs

## API Reference

#### Get all items

```http
  POST /solution?criterion={criterion}
```

| Parameter | Type     | Description                | Value       |
| :-------- | :------- | :------------------------- | :-----------|
| `orders` | `array` | **Required**. Orders array | []: array
| `criterion` | `string` | **Required**. Query parameter | [ "completed", "pending", "canceled", "all" ]



