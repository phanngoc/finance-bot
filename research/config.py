# config.py
from typing import Literal

entities = Literal[
    "mã_cổ_phiếu", "công_ty", "lợi_nhuận", "giá_cổ_phiếu", "khối_lượng_giao_dịch", "ngày_giao_dịch",
    "tài_sản", "khoản_phải_thu", "dự_án", "doanh_thu", "lợi_nhuận_gộp", "lãi_ròng",
    "lợi_nhuận_sau_thuế", "tồn_kho", "khoản_phải_thu_ngắn_hạn", "bên_liên_quan", "ngành_công_nghiệp"
]

relations = Literal[
    "sở_hữu", "thuộc_về", "là", "là_một_phần_của", "tăng", "giảm", "giao_dịch_vào_ngày",
    "công_bố", "triển_khai", "đạt", "phát_sinh", "trừ", "lên_đến", "chiếm", "hợp_tác", "liên_quan_tới"
]

schema = {
    "mã_cổ_phiếu": ["sở_hữu", "thuộc_về", "là", "thuộc_về_ngành_công_nghiệp"],
    "công_ty": ["sở_hữu", "thuộc_về"],
    "lợi_nhuận": ["tăng", "giảm"],
    "giá_cổ_phiếu": ["tăng", "giảm"],
    "khối_lượng_giao_dịch": ["giao_dịch_vào_ngày"],
    "ngày_giao_dịch": ["giao_dịch_vào_ngày"],
    "tài_sản": ["tăng", "giảm"],
    "khoản_phải_thu": ["tăng", "giảm"],
    "dự_án": ["triển_khai", "thuộc_về"],
    "doanh_thu": ["đạt"],
    "lợi_nhuận_gộp": ["đạt"],
    "lãi_ròng": ["đạt"],
    "lợi_nhuận_sau_thuế": ["đạt"],
    "tồn_kho": ["tăng", "giảm"],
    "khoản_phải_thu_ngắn_hạn": ["tăng", "giảm"],
    "bên_liên_quan": ["hợp_tác"],
    "ngành_công_nghiệp": ["liên_quan_tới"]
}