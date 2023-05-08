 # Egg Detection

`egg_detection_notebook.ipynb` is a notebook for training
object detection by using `YOLOv8` by ultralytics.


## Gradio application

Install all dependencies

```sh
pip install gradio
```

Put the trained model in this folder and change `MODEL_NAME` in `app.py`.
Then run an gradio application.

```sh
python app.py
```
- `--model_path` : path to the trained model default: `runs/detect/train/weights/best.pt` which appeared after training process