product_schema = {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "imageUrl": {
                  "type": "array",
                },
                "price": {
                  "type": "number"
                },
                "count": {
                  "type": "integer"
                },
                "tag": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "string"
                    }
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "description",
                "imageUrl",
                "price",
                "count",
                "tag"
              ]
}