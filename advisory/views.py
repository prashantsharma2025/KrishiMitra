
from pathlib import Path

import joblib
import pandas as pd

from django.conf import settings
from django.shortcuts import render

from .forms import CropInputForm


MODEL_PATH = Path(settings.BASE_DIR) / "ml" / "crop_model.joblib"
model = joblib.load(MODEL_PATH)

FEATURES = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
]


def home(request):
    result = None

    if request.method == "POST":
        form = CropInputForm(request.POST)

        if form.is_valid():
            values = form.cleaned_data

            input_data = pd.DataFrame(
                [[values[name] for name in FEATURES]],
                columns=FEATURES,
            )

            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]

            result = {
                "crop": str(prediction),
                "confidence": round(
                    float(probabilities.max()) * 100, 1
                ),
            }
    else:
        form = CropInputForm()

    return render(
        request,
        "advisory/home.html",
        {"form": form, "result": result},
    )
