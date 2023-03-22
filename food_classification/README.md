# Food classification

`thai_food_classification_transformers.ipynb` is a notebook for training
image classification using `transformers`.

## Gradio application

Install all dependencies

```sh
pip install gradio
pip install datasets
pip install git+https://github.com/huggingface/transformers
```

Put the trained model in this folder and change `MODEL_NAME` in `app.py`.
Then run an gradio application.

```sh
gradio app.py
```
