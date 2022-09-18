## Автоматичеcкое тестирование приложений на Flask

### Windows
- Создайте venv и установите требования
    ```shell
    python -m venv venv 
    venv\Scripts\activate 
    pip install -r requirements.txt
    ```
- Запустит все тесты
    ```shell
    pytest
    ```

### MacOS/Linux
- Создайте venv и установите требования
    ```shell
    python3 -m venv venv
    source venv/bin/activate # Активация виртуального окружения
    pip install -r requirements.txt
    ```
- Запустит все тесты
    ```shell
    pytest
    ```

