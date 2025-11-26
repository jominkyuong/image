import streamlit as st
from PIL import Image
import io

st.title("Image → Grayscale Converter")

uploaded_file = st.file_uploader("이미지 업로드", type=["png", "jpg", "jpeg", "bmp"])
if uploaded_file is not None:
    # 업로드된 파일을 PIL 이미지로 열기
    img = Image.open(uploaded_file)
    st.subheader("원본 이미지")
    st.image(img, use_column_width=True)

    # 흑백 변환
    gray = img.convert("L")
    st.subheader("흑백 이미지")
    st.image(gray, use_column_width=True)

    # 변환된 이미지 다운로드 준비
    buf = io.BytesIO()
    # JPEG 로 저장 (원본이 PNG면 손실 있을 수 있음 — 필요하면 PNG로 변경)
    gray.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="흑백 이미지 다운로드",
        data=byte_im,
        file_name="grayscale.png",
        mime="image/png"
    )
