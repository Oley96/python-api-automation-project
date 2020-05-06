address_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "_embedded": {
      "type": "object",
      "properties": {
        "address": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "street": {
                  "type": "string"
                },
                "number": {
                  "type": "string"
                },
                "country": {
                  "type": "string"
                },
                "city": {
                  "type": "string"
                },
                "postcode": {
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "_links": {
                  "type": "object",
                  "properties": {
                    "address": {
                      "type": "object",
                      "properties": {
                        "href": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "href"
                      ]
                    },
                    "self": {
                      "type": "object",
                      "properties": {
                        "href": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "href"
                      ]
                    }
                  },
                  "required": [
                    "address",
                    "self"
                  ]
                }
              },
              "required": [
                "street",
                "number",
                "country",
                "city",
                "postcode",
                "id",
                "_links"
              ]
            }
          ]
        }
      },
      "required": [
        "address"
      ]
    }
  },
  "required": [
    "_embedded"
  ]
}