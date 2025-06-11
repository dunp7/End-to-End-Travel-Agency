# Travel-Agency

```
travel-bot-api/
├── app/
│   ├── __init__.py
│   ├── main.py                # Entry point chính để chạy API
│   ├── config.py              # Cấu hình chung (biến môi trường, kết nối DB)
│   ├── routers/               # Các route (endpoint) chính
│   │   ├── __init__.py
│   │   ├── destinations.py    # Endpoint liên quan đến điểm đến
│   │   ├── itineraries.py     # Endpoint liên quan đến lịch trình
│   │   ├── transport.py       # Endpoint liên quan đến phương tiện
│   │   └── accommodations.py  # Endpoint liên quan đến chỗ ở
│   ├── models/                # Định nghĩa các schema dữ liệu (Pydantic)
│   │   ├── __init__.py
│   │   ├── destination.py
│   │   ├── itinerary.py
│   │   ├── transport.py
│   │   └── accommodation.py
│   ├── services/              # Business logic (tính toán/gợi ý)
│   │   ├── __init__.py
│   │   ├── destination_service.py
│   │   ├── itinerary_service.py
│   │   └── weather_service.py
│   └── db/                    # Kết nối và quản lý cơ sở dữ liệu
│       ├── __init__.py
│       ├── database.py        # Kết nối cơ sở dữ liệu
│       └── seed_data.py       # Khởi tạo dữ liệu mẫu
|
|
|
├── .env                       # File chứa biến môi trường (API keys, config)
├── .gitignore                 # Danh sách file cần bỏ qua trong Git
├── requirements.txt           # Các thư viện cần thiết
├── Dockerfile                 # File cấu hình Docker
├── docker-compose.yml         # File cấu hình Docker Compose
└── README.md                  # Mô tả dự án
```