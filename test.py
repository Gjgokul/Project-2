Software testing code 
Index.html 
<!DOCTYPE html>
<html>
<head>
    <title>Movie Ticket Booking</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }
        form {
            display: inline-block;
            text-align: left;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        select, input {
            width: 100%;
            padding: 8px;
            margin: 10px 0;
        }
        .summary {
            margin-top: 20px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h2>🎟️ Movie Ticket Booking</h2>
    <form method="POST">
        <label for="movie">Select Movie:</label><br>
        <select name="movie" required>
            {% for movie in movies %}
            <option value="{{ movie }}" {% if movie == selected_movie %}selected{% endif %}>{{ movie }}</option>
            {% endfor %}
        </select>

        <label for="tickets">Number of Tickets:</label><br>
        <input type="number" name="tickets" min="1" required>

        <button type="submit">Book Tickets</button>
    </form>

    {% if selected_movie %}
    <div class="summary">
        <h3>✅ Booking Summary</h3>
        <p><strong>Movie:</strong> {{ selected_movie }}</p>
        <p><strong>Tickets:</strong> {{ num_tickets }}</p>
        <p><strong>Total Price:</strong> ₹{{ total_cost }}</p>
        <p>Thank you for booking with us!</p>
    </div>
    {% endif %}

    {% if error %}
    <p class="error">{{ error }}</p>
    {% endif %}
</body>
</html>
