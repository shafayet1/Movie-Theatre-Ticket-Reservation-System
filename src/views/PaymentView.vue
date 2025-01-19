<template>
  <body>
    <div class="credit-card-form">
      <h2>Credit Card Payment</h2>
      <form @submit.prevent="payNow">
        <div class="form-group">
          <label for="card-number">Card Number</label>
          <input v-model="cardNumber" type="text" id="card-number" placeholder="Card number">
        </div>
        <div class="form-group">
          <label for="card-holder">Card Holder</label>
          <input v-model="cardHolder" type="text" id="card-holder" placeholder="Card holder's name">
        </div>
        <div class="form-row">
          <div class="form-group form-column">
            <label for="expiry-date">Expiry Date</label>
            <input v-model="expiryDate" type="text" id="expiry-date" placeholder="MM/YY">
          </div>
          <div class="form-group form-column">
            <label for="cvv">CVV</label>
            <input v-model="cvv" type="text" id="cvv" placeholder="CVV">
          </div>
        </div>
        <button type="submit" class="click-button">Pay Now</button>
      </form>
    </div>
  </body>
</template>

<script>
import axios from 'axios';
//import { useRouter } from 'vue-router';
export default {
  props: ['auditoriumId', 'seatIds'],
  data() {
    return {
      cardNumber: '',
      cardHolder: '',
      expiryDate: '',
      cvv: '',
    };
  },
  computed: {
    isFormValid() {
      // Add your validation logic here
      return (
        this.cardNumber.trim() !== '' &&
        this.cardHolder.trim() !== '' &&
        this.expiryDate.trim() !== '' &&
        this.cvv.trim() !== ''
      );
    },
  },
  created() {
    console.log(this.seatIds);
    this.reserveSeats(this.auditoriumId, this.seatIds);
  },
  methods: {
    payNow() {
      if (this.isFormValid) {
        this.reserveSeats(this.auditoriumId, this.seatIds);
        confirm("Payment Successful")
        this.$router.push("/reciept")
      }
    },
    reserveSeats(auditoriumId, seatIds) {
      const seatInfo = seatIds.split(',').map(id => id.split('-'));
      const formattedData = seatInfo.map(([seat, value]) => [
        seat.replace('Seat_', ''),
        value
      ]);
      formattedData.forEach(([row, col]) => {
      const formattedRow = row.padStart(2, '0');
      const formattedCol = col.padStart(2, '0');
      const seatId = `${auditoriumId}${formattedRow}${formattedCol}`;
      axios.get(`/api/reserve_seats/${seatId}`)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error('Error reserving seats:', error)
        });
    });
  },
  },
};
</script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500&family=Montserrat:wght@600&display=swap');
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background-color: #686868;
}
.credit-card-form {
  max-width: 400px;
  margin: auto;
  padding: 1em;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
  font-family: 'Montserrat', sans-serif;
  background-color: #dbdbdb;
  text-align: center;
  color: #424242;
  align-content: center;
}
.credit-card-form h2 {
  margin-bottom: 10%;
  font-size: 24px;
}
.credit-card-form .form-group {
  margin-bottom: 15px;
}
.credit-card-form label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
  color: #777;
}
.credit-card-form input[type="text"],
.credit-card-form select {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 1rem;
  font-size: 16px;
    font-family: 'Montserrat', sans-serif;
}
.credit-card-form .form-row {
  display: flex;
}
.credit-card-form button[type="submit"] {
  width: 100%;
  padding: 14px;
  background-color: #585858;
  color: #fff;
  border: none;
  border-radius: 1rem;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  font-family: 'Montserrat', sans-serif;
}
.credit-card-form button[type="submit"]:hover {
  background-color: #bebebe;
  color: #424242;
  font-family: 'Montserrat', sans-serif;
}
.credit-card-form button[type="submit"]:focus {
  outline: none;
  font-family: 'Montserrat', sans-serif;
}
</style>