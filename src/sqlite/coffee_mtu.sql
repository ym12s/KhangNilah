CREATE TABLE tb_User (
    uid TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    vaiTro INTEGER CHECK (vaiTro IN (0,1)), 
    ngayTao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    idNhanVien TEXT UNIQUE, 
    FOREIGN KEY (idNhanVien) REFERENCES tb_NhanVien(idNhanVien) ON DELETE SET NULL
);

CREATE TABLE tb_KhachHang (
    idKhachHang TEXT PRIMARY KEY,
    hoTen TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    diemTichLuy INTEGER DEFAULT 0
);

CREATE TABLE tb_NhanVien (
    idNhanVien TEXT PRIMARY KEY CHECK (idNhanVien LIKE 'NV%'), -- Bắt đầu bằng "NV"
    hoTen TEXT NOT NULL,
    chucVu TEXT NOT NULL CHECK (chucVu IN ('Quản lý', 'Thu ngân', 'Pha chế', 'Phục vụ')),
    sdt INTEGER UNIQUE NOT NULL,
    luong REAL NOT NULL
);

CREATE TABLE tb_Mon (
    idMon INTEGER PRIMARY KEY AUTOINCREMENT,
    tenMon TEXT NOT NULL,
    loaiMon TEXT NOT NULL,
    giaMon REAL NOT NULL,
    ghiChu TEXT,
    hinhAnh TEXT
);

CREATE TABLE tb_DonHang (
    idDonHang INTEGER PRIMARY KEY AUTOINCREMENT,
    ngayTaoDonHang TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    idNhanVien TEXT,
    trangThaiDH TEXT NOT NULL CHECK (trangThaiDH IN ('Chờ xử lý', 'Đang làm', 'Hoàn thành', 'Đã hủy')),
    tongTien REAL NOT NULL,
    FOREIGN KEY (idNhanVien) REFERENCES tb_NhanVien(idNhanVien)
);

CREATE TABLE tb_ChiTietDonHang (
    idChiTietDonHang INTEGER PRIMARY KEY AUTOINCREMENT,
    idDonHang INTEGER NOT NULL,
    tongSoLuong INTEGER NOT NULL,
    thanhTien REAL NOT NULL,
    fileHtml TEXT,
    FOREIGN KEY (idDonHang) REFERENCES tb_DonHang(idDonHang) ON DELETE CASCADE
);

CREATE TRIGGER taoIdTuDongKH
BEFORE INSERT ON tb_KhachHang
FOR EACH ROW
WHEN NEW.idKhachHang IS NULL
BEGIN
    UPDATE tb_KhachHang
    SET idKhachHang = 'KH_' || printf('%03d', 
        (SELECT IFNULL(MAX(CAST(SUBSTR(idKhachHang, 4) AS INTEGER)), 0) + 1 FROM tb_KhachHang))
    WHERE rowid = NEW.rowid;
END;