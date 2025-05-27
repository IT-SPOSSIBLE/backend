Sure! Here's a professional README file for your Django SMS parser API project incorporating your initial snippet and extending it with documentation relevant to your SMS parsing feature:

````markdown
# drf-user-api

## Project Overview
This Django REST Framework (DRF) project provides backend APIs covering user authentication features including registration, login, profile management, password reset, and password forgot functionalities.

Additionally, this project includes an SMS Transaction Parser API endpoint that processes transactional SMS messages (in English and Kiswahili) and extracts structured data such as transaction type, amount, sender and receiver information, remaining balance, transaction reference, and vendor identification.

---

## Features

### User Authentication
- User registration
- User login
- Profile retrieval and update
- Password forgot (request password reset)
- Password reset (perform password update)

### SMS Transaction Parser
- Accepts raw SMS text messages related to financial transactions.
- Supports parsing messages in both English and Kiswahili.
- Extracts transaction details:
  - Transaction Type (Send/Receive or Tuma/Pokea)
  - Transaction Amount with currency
  - Sender Name and Phone Number
  - Receiver Name and Phone Number
  - Remaining Balance
  - Transaction Reference Number
  - Vendor (Airtel, Vodacom, Tigo, Halotel or "-")
- Automatically identifies whether the user is the sender or receiver and labels accordingly.
- Returns a clean, structured JSON response.

---

## Backend Setup

### Requirements
- Python 3.8+
- Django 3.x or higher
- Django REST Framework
- Requests (for external API calls)
- OpenRouter API key (environment variable `OPENROUTER_API_KEY`)

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/drf-user-api.git
   cd drf-user-api
````

2. Create and activate a virtual environment

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenRouter API key as an environment variable

   ```bash
   export OPENROUTER_API_KEY="your_openrouter_api_key_here"
   ```

5. Run migrations and start the server

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## API Endpoints

### SMS Parser Endpoint

* **URL:** `/api/parse-sms/`
* **Method:** POST
* **Payload:**

  ```json
  {
    "message": "Umelipa 1,000.00 Tsh kwenda YATOSHA BUNDLE. Makato Tsh 0.00. Salio 132,193.64 Tsh TID:MP250525.1327.Q61819"
  }
  ```
* **Response:**

  ```json
  {
    "type": "Send",
    "amount": "1,000.00 Tsh",
    "sender_name": "You",
    "sender_number": "You",
    "receiver_name": "YATOSHA BUNDLE",
    "receiver_number": "-",
    "balance": "132,193.64 Tsh",
    "reference": "MP250525.1327.Q61819",
    "vendor": "Vodacom"
  }
  ```

---

## Notes

* The SMS Parser relies on the OpenRouter API using the `mistralai/mistral-7b-instruct` model.
* Please ensure your API key is valid and you have sufficient quota to avoid errors.
* The parser supports both English and Kiswahili transactional SMS formats.
* Vendor detection is based on keywords in the SMS text.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, please open an issue or contact \[[your.email@example.com](mailto:your.email@example.com)].

```

---

Would you like me to generate a `requirements.txt` or help with other parts?
```
