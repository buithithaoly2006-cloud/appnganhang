import streamlit as st 
st.imge("logo.jpg")
# Cấu hình trang
st.set_page_config(page_title="Tính Tiền Gửi Tiết Kiệm", page_icon="💰", layout="centered")

st.title("💰 Công Cụ Tính Tiền Gửi Tiết Kiệm")
st.write("Nhập thông tin khoản tiết kiệm của bạn để so sánh lãi đơn và lãi kép.")

st.divider()

# Tạo 2 cột để nhập dữ liệu
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi (VNĐ):", 
        min_value=0.0, 
        value=100000000.0, 
        step=1000000.0, 
        format="%.0f"
    )
    
    thoi_gian_thang = st.number_input(
        "Thời gian gửi (tháng):", 
        min_value=1, 
        value=12, 
        step=1
    )

with col2:
    lai_suat_nam = st.number_input(
        "Lãi suất (%/năm):", 
        min_value=0.0, 
        value=6.0, 
        step=0.1, 
        format="%.2f"
    )

st.divider()

# Nút thực hiện tính toán
if st.button("Tính toán", type="primary", use_container_width=True):
    # Đổi lãi suất năm sang lãi suất tháng
    r_thang = (lai_suat_nam / 100) / 12
    
    # 1. Tính Lãi Đơn
    # Công thức: Lãi = Gốc * r_thang * số_tháng
    tien_lai_don = so_tien_gui * r_thang * thoi_gian_thang
    tong_tien_don = so_tien_gui + tien_lai_don
    
    # 2. Tính Lãi Kép (Gộp lãi theo tháng)
    # Công thức: Tổng = Gốc * (1 + r_thang)^số_tháng
    tong_tien_kep = so_tien_gui * ((1 + r_thang) ** thoi_gian_thang)
    tien_lai_kep = tong_tien_kep - so_tien_gui
    
    # Hiển thị kết quả bằng 2 cột
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.subheader("📌 Lãi Đơn")
        st.metric(label="Tiền lãi nhận được", value=f"{tien_lai_don:,.0f} VNĐ")
        st.metric(label="Tổng số tiền nhận được", value=f"{tong_tien_don:,.0f} VNĐ")
        
    with res_col2:
        st.subheader("📈 Lãi Kép (Lãi gộp tháng)")
        st.metric(
            label="Tiền lãi nhận được", 
            value=f"{tien_lai_kep:,.0f} VNĐ", 
            delta=f"+{tien_lai_kep - tien_lai_don:,.0f} VNĐ so với lãi đơn"
        )
        st.metric(label="Tổng số tiền nhận được", value=f"{tong_tien_kep:,.0f} VNĐ")

    # Bảng chi tiết
    st.write("### 📊 Tóm tắt kết quả")
    st.table({
        "Phương thức": ["Lãi đơn", "Lãi kép"],
        "Tiền gốc (VNĐ)": [f"{so_tien_gui:,.0f}", f"{so_tien_gui:,.0f}"],
        "Tiền lãi (VNĐ)": [f"{tien_lai_don:,.0f}", f"{tien_lai_kep:,.0f}"],
        "Tổng tiền (VNĐ)": [f"{tong_tien_don:,.0f}", f"{tong_tien_kep:,.0f}"]
    })
