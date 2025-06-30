from flask import Flask, render_template, request

app = Flask(__name__)

# Movie list and price
movies = ["Jawan", "Leo", "RRR", "Vikram"]
ticket_price = 150

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_movie = request.form.get("movie")
        num_tickets = request.form.get("tickets")

        try:
            num_tickets = int(num_tickets)
            if num_tickets <= 0:
                raise ValueError("Ticket count must be positive.")

            total_cost = num_tickets * ticket_price
            return render_template("index.html", movies=movies,
                                   selected_movie=selected_movie,
                                   num_tickets=num_tickets,
                                   total_cost=total_cost)
        except ValueError:
            error = "Please enter a valid number of tickets."
            return render_template("index.html", movies=movies, error=error)

    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
