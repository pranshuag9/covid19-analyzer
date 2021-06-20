from sklearn.model_selection import train_test_split
from tensorflow.python.keras.callbacks import ModelCheckpoint

from api.response_templates.error_response_template.error_response_template import \
    ErrorResponse
from api.response_templates.response_template import ResponseTemplate
from api.response_templates.success_response_template.success_response_template import \
    SuccessResponse
from app_utils import load_data_from_disk
from config import DATASET_DIR, MODEL_CHECKPOINT_PATH, log
from data.architectures.model1.model1 import get_model1


def handle_train_model_request(request_json) -> tuple[ResponseTemplate, int]:
    res = ResponseTemplate(error=True, success=False), 400
    try:
        data, target = load_data_from_disk(DATASET_DIR)
        input_shape = data.shape[1:]
        model = get_model1(input_shape=input_shape)
        train_data, test_data, train_target, test_target = train_test_split(data, target,
                                                                            test_size=0.1)
        checkpoint = ModelCheckpoint(
            filepath=MODEL_CHECKPOINT_PATH,
            monitor='val_loss',
            verbose=0,
            save_best_only=True,
            mode='auto'
        )
        history = model.fit(
            x=train_data,
            y=train_target,
            epochs=20,
            callbacks=[checkpoint],
            validation_split=0.1
        )
        msg = "Successfully trained the model"
        log.info(f"{msg}")
        data = {
            "loss": history.history["loss"],
            "val_loss": history.history["val_loss"]
        }
        res: tuple[ResponseTemplate, int] = SuccessResponse(message=msg, data=data, type="json"), 200
    except Exception as e:
        res: tuple[ResponseTemplate, int] = ErrorResponse(message="Couldn't finish training!! Please try again later"), 400
    log.info(f"RESPONSE: {res[0].to_dict()}")
    return res