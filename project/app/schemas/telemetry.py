from pydantic import BaseModel, Field
from typing import Optional

# 1. Базова схема (Спільні поля)
class TelemetryBase(BaseModel):
    # Всі ці поля можуть бути порожніми (None), бо різні датчики міряють різне
    fire: Optional[bool] = Field(None, description="Статус тривоги (True - пожежа, False - спокійно)")
    pressure: Optional[int] = Field(None, description="Атмосферний тиск")
    temperature: Optional[float] = Field(None, description="Температура (наприклад, 24.5)")
    
    # Додамо перевірку: вологість може бути лише від 0 до 100 відсотків
    humidity: Optional[int] = Field(None, ge=0, le=100, description="Вологість у %")

# 2. Схема для створення (Отримання від датчика)
class TelemetryCreate(TelemetryBase):
    pass
    # Пам'ятаєш нашу розмову про "вкладені маршрути" (URL)?
    # Тут ми НЕ пишемо `device_id`. 
    # Коли сам датчик буде слати дані, він робитиме запит на кшталт:
    # POST /devices/{device_id}/telemetry
    # Тому `device_id` візьме Роутер з посилання, а сама схема буде перевіряти лише показники.

# 3. Схема для відповіді (Віддача на фронтенд або мобільний додаток)
class TelemetryResponse(TelemetryBase):
    id: int
    device_id: int # Тут ми вже віддаємо ID пристрою, щоб клієнт розумів, чиї це дані

    class Config:
        from_attributes = True # Дозвіл на роботу з моделлю SQLAlchemy