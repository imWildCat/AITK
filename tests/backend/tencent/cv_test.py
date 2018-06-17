from aitk.backend.tencent import TencentCV
import os


def get_id_key():
    t_id = os.getenv('TENCENT_APP_ID')
    key = os.getenv('TENCENT_APP_KEY')
    return t_id, key


def test_cv_init():
    cv = TencentCV()
    t_id, key = get_id_key()

    assert t_id == cv.app_id
    assert key == cv.app_key
