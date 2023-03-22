import gradio as gr
from PIL import Image
from transformers import pipeline


MODEL_NAME = "./swin-tiny-patch4-window7-224/"
pipe = pipeline("image-classification", MODEL_NAME)
food_list = [
    "green_curry",
    "tepo_curry",
    "liang_curry",
    "taohoo_moosup",
    "mara_yadsai",
    "masaman",
    "orange_curry",
    "cashew_chicken",
    "omelette",
    "sunny_side_up",
    "palo_egg",
    "sil_egg",
    "nun_banana",
    "kua_gai",
    "cabbage_fish_sauce",
    "river_prawn",
    "shrimp_ob_woonsen",
    "kanom_krok",
    "mango_sticky_rice",
    "kao_kamoo",
    "kao_klook_kapi",
    "kaosoi",
    "kao_pad",
    "kao_pad_shrimp",
    "chicken_rice",
    "kao_mok_gai",
    "tom_ka_gai",
    "tom_yum_kung",
    "tod_mun",
    "poh_pia",
    "pak_boong_fai_daeng",
    "padthai",
    "pad_krapao",
    "pad_si_ew",
    "pad_fakthong",
    "eggplant_stirfry",
    "pad_hoi_lai",
    "foithong",
    "panaeng",
    "yum_tua_ploo",
    "yum_woonsen",
    "larb_moo",
    "pumpkin_custard",
    "sakoo_sai_moo",
    "somtam",
    "moopoing",
    "satay",
    "hor_mok",
]
id2food = {str(i).zfill(2): f for i, f in enumerate(food_list)}


def inference(gr_input):
    """Inference from gradio input."""
    image = Image.fromarray(gr_input.astype("uint8"), "RGB")
    predictions = pipe(image)
    predictions = {id2food[l["label"]]: l["score"] for l in predictions}
    return predictions


def main():
    """Main class for gradio."""
    inputs = gr.inputs.Image()
    outputs = gr.outputs.Label(num_top_classes=5)

    interface = gr.Interface(
        fn=inference, inputs=inputs, outputs=outputs, interpretation="default",
        examples=["padthai.png", "somtam.png"]
    ).launch(debug="True")
    interface.launch()


if __name__ == "__main__":
    main()