import weaviate

client = weaviate.Client(
    # url="https://some-endpoint.weaviate.network",  # Replace with your endpoint
    url="http://localhost:8080/",  # Replace with your endpoint
)

# ===== add schema =====
pokemon_class = {
    "class": "Pokemon",
    "description": "An image of a pokemon",
    "vectorizer": "img2vec-neural",
    "moduleConfig": {
        "img2vec-neural": {
            "imageFields": [
                "image"
            ]
        },
        "properties": [
            {
                "name": "image",
                "dataType": ["blob"]
            },
        ],
    }
}


def create_schema():
    client.schema.create_class(pokemon_class)


if __name__ == '__main__':
    create_schema()
