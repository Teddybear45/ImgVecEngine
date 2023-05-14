import weaviate
import os

client = weaviate.Client(
    # url="https://some-endpoint.weaviate.network",  # Replace with your endpoint
    url="http://localhost:8080/",  # Replace with your endpoint
)

dir_images = "../static/images/pokemon"

def vectorize_data(dir_images):
    with client.batch as batch:
        batch.batch_size = 10

        for i, d in enumerate(os.listdir(dir_images)):
            print(f"importing pokemon: {i + 1}")

            b64_image = weaviate.util.image_encoder_b64(os.path.join(dir_images, d))

            properties = {
                "labelName": d.split(".")[0],
                "image": b64_image,
            }
            client.batch.add_data_object(properties, "Pokemon")


if __name__ == '__main__':
    vectorize_data(dir_images)





