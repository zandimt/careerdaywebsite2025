from io import BytesIO

import qrcode


def generate_qr_code(content: str) -> BytesIO:
    """
    Generate a QR code for the participant.
    :return: QR code image.
    """
    data = f"{content}"
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer
