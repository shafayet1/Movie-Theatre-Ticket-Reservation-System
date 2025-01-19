from flask import Flask, request, jsonify
import mysql.connector
import pandas as pd
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow requests from 'http://localhost:8080'

def create_connection():
    host = "movies.cr4qxihfcdeh.us-east-2.rds.amazonaws.com"
    user = "admin"
    password = "cpsproject"
    database = "Movie_System"

    try: 
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            return connection
        else:
            print("Connection Failed.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

@app.route('/api/reserve_seats/<int:seat_id>', methods=['GET'])
def reserve_seat(seat_id):   
    try:
        connection = create_connection()
        cursor = connection.cursor()

        if seat_id:
            # Check if the seat_id exists in the Seat table
            cursor.execute("SELECT 1 FROM Seat WHERE ID = %s", (seat_id,))
            seat_exists = cursor.fetchone()

            if seat_exists:
                # Update the Seat_Reserved value to 1 for the specified seat
                cursor.execute("UPDATE Seat SET Seat_Reserved = 1 WHERE ID = %s", (seat_id,))
                connection.commit()
                auditorium_id = str(seat_id)[0]
                update_auditorium_percent(auditorium_id)
                cursor.close()
                return jsonify({'success': True, 'message': f'Seat {seat_id} reserved successfully'})
            else:
                return jsonify({'success': False, 'message': f'Seat {seat_id} not found'})

        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'success': False, 'message': f'Error: {err}'}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()

    

def update_auditorium_percent(auditorium_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE Auditorium AS a
            SET a.Percent_Booked = (
                SELECT (COUNT(s.ID) / 100.0) * 100
                FROM Seat AS s
                WHERE s.Auditorium_ID = a.ID AND s.Seat_Reserved = 1
            )
            WHERE a.ID = %s;
        """, (auditorium_id,))

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()

    if connection:
        connection.close()

@app.route('/api/get_percentage/<int:ID>', methods=['GET'])
def getAuditoriumPercentage(ID):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT Percent_Booked FROM Auditorium WHERE ID = %s", (ID,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    if result:
        return result
    
@app.route('/api/get_movie_info/<int:ID>', methods=['GET'])
def getMovieInfo(ID):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT Name, Duration_Mins, Auditoriums FROM Movie WHERE ID = %s", (ID,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    if result:
        # Construct a dictionary with movie information
        movie_info = {'Name': result[0], 'Duration_Mins': result[1], 'Auditoriums': result[2]}
        return jsonify(movie_info)
    else:
        return jsonify({'message': 'Movie not found'})
    
@app.route('/api/get_all_movie_info', methods=['GET'])
def getAllMovieInfo():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT Name, Duration_Mins, Auditoriums, Image FROM Movie")
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    if results:
        # Create a list of dictionaries containing movie information
        movie_list = []
        for result in results:
            movie_info = {'Name': result[0], 'Duration_Mins': result[1], 'Auditoriums': result[2], 'Image':result[3]}
            movie_list.append(movie_info)

        return jsonify(movie_list)
    else:
        return jsonify({'message': 'No movies found'})

@app.route('/api/get_seating_plan/<int:ID>', methods=['GET'])
def getSeatingPlan(ID):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    SELECT Seat_Row, Seat_Col, Seat_Reserved
    FROM Seat
    WHERE Auditorium_ID = %s
    """
    cursor.execute(query, (ID,))
    result = cursor.fetchall()

    # Organize the result into the desired format
    organized_result = {}

    for row in result:
        seat_row, seat_col, seat_reserved = row
        seat_id = f"Seat_{seat_row}-{seat_col}"

        if seat_row not in organized_result:
            organized_result[seat_row] = []

        organized_result[seat_row].append({"id": seat_id, "occupied": seat_reserved})

    # Print the organized result for verification
    for row, seats in organized_result.items():
        print(f"Seat Row: {row}")
        for seat in seats:
            print(f"  Seat ID: {seat['id']}, Occupied: {seat['occupied']}")

    # Don't forget to close the cursor and connection when done
    cursor.close()
    connection.close()

    return organized_result

if __name__ == '__main__':
   app.run()