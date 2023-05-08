from ultralytics import YOLO
import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--model_path",
    default="runs/detect/train/weights/best.pt", 
    type=str,
    help="path of the model",
)
# default model path appears after training the model in egg_detection_notebook.ipynb

model_name = parser.parse_args().model_path
model = YOLO(model_name)
id2label = {0: "Crack", 1: "Egg"}
font = ImageFont.truetype("arial.ttf", 170)  # choose a font and size


def inference(gr_input):
    """
    Inference function for gradio.
    """
    pred = model(gr_input)
    draw_prediction = ImageDraw.Draw(gr_input)
    boxes_predict = pred[0].boxes
    boxes = boxes_predict.xyxy.tolist()
    scores = boxes_predict.conf.tolist()
    labels = boxes_predict.cls.tolist()
    for score, label, box in zip(scores, labels, boxes):
        x, y, x2, y2 = tuple(box)
        if label == 0:
            draw_prediction.rectangle((x, y, x2, y2), outline="red", width=15)
        else:
            draw_prediction.rectangle((x, y, x2, y2), outline="blue", width=15)
        result = id2label[label]
        draw_prediction.text(
            (x, y), result, fill="white", font=font
        )  # draw label text with chosen font
    return gr_input


def main():
    """
    Main class for gradio.
    """
    imagein = gr.inputs.Image(label="Input Image", type="pil")
    imageout = gr.outputs.Image(label="Predicted Image", type="pil")

    interface = gr.Interface(
        fn=inference,
        inputs=imagein,
        outputs=imageout,
        title="Egg_Detection",
        interpretation="default",
        examples=["egg_1.jpg", "egg_2.jpg"],
    ).launch(debug="True", share=True)
    interface.launch()


if __name__ == "__main__":
    main()
