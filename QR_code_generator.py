import pyqrcode

qr = pyqrcode.create(
    "https://github.com/matlaczj/ASM-Method-for-Local-Email-Categorization"
)
svg = qr.svg("file_path.svg", scale=8)
