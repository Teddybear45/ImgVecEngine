import weaviate
import os

client = weaviate.Client(
    # url="https://some-endpoint.weaviate.network",  # Replace with your endpoint
    url="http://localhost:8080/",  # Replace with your endpoint
)


def search_by_near_image(img_obj_path, class_name):
    """
    Search by image
    :param imgObj: image object path
    :return:
    """
    q_limit = 4
    certainty = 0.9
    # ----------------- process -----------------
    encoded_image = weaviate.util.image_encoder_b64(img_obj_path)
    nearImage = {"image": encoded_image, "certainty": certainty}
    return client.query.get(class_name, "image").with_near_image(nearImage, encode=False).with_limit(q_limit).do()


def decode_queried_image(queried_image):
    """
    Decode queried image
    :param queried_image:
    :return:
    """
    return weaviate.util.image_decoder_b64(queried_image)


if __name__ == '__main__':
    search_file = "jiggly.png"
    search_loc = "search/query"
    results_loc = "search/results"
    search_file_loc = os.path.join(search_loc, search_file)
    result = search_by_near_image(search_file_loc, "Pokemon")

    # struct => ['data']['Get']['Pokemon'][0]['image']
    for i, d in enumerate(result['data']['Get']['Pokemon']):
        # decode queried image
        bin_image = decode_queried_image(d['image'])
        # save image
        with open(os.path.join(results_loc, f"{i}.png"), "wb") as f:
            f.write(bin_image)

    # print(result['data']['Get']['Pokemon'][0]['image'])
