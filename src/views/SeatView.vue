<template>
  <div>
    <div id="app"></div>

    <div class="header">
      <h1> {{ movieName }} </h1>
    </div>

    <ul class="seat_help_tab">
      <li>
        <div class="seat"></div>
        <small>Available</small>
      </li>
      <li>
        <div class="seat selected"></div>
        <small>Selected</small>
      </li>
      <li>
        <div class="seat occupied"></div>
        <small>Occupied</small>
      </li>
    </ul>

    <div class="container">
      <div class="screen"></div>

      <div class="row" v-for="(seats, row) in seatingPlan" :key="row">
        <div
          class="seat"
          :class="{ seat: true, selected: isSelected(seat.id), occupied: seat.occupied }"
          @click="toggleSeat(seat)"
          v-for="(seat, seatIndex) in seats"
          :key="seatIndex"
        ></div>
      </div>

      <div class="selected-counter">
        <p>Selected Seats: {{ selectedSeats.length }}</p>
      </div>

      <router-link :to="{ path: '/payment/' + AuditoriumID + '/' + selectedSeats.join(',') }">
        <button class="buy-button" @click="buyTickets" :disabled="selectedSeats.length === 0">
          Buy Tickets Now
        </button>
      </router-link>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SeatView',
  data() {
    return {
      movieName: '',
      AuditoriumID: 0,
      selectedSeats: [],
      seatingPlan: [],
    };
  },
  created() {
    this.AuditoriumID = this.$route.params.auditorium;
    this.getMovieInfo(this.AuditoriumID);
    this.getSeatingPlan(this.AuditoriumID);
  },
  methods: {
    toggleSeat(seat) {
      if (!seat.occupied) {
        const index = this.selectedSeats.indexOf(seat.id);
        if (index !== -1) {
          this.selectedSeats.splice(index, 1);
        } else {
          this.selectedSeats.push(seat.id);
        }
      }
    },
    isSelected(seatId) {
      return this.selectedSeats.includes(seatId);
    },
    getMovieInfo(ID) {
      axios.get(`/api/get_movie_info/${ID}`)
        .then(response => {
          if ('Name' in response.data) {
            this.movieName = response.data.Name;
          } else if ('message' in response.data) {
            this.movieName = response.data.message;
          }
        })
        .catch(error => {
          console.error('Error fetching movie information:', error);
        });
    },
    getSeatingPlan(ID) {
      axios.get(`/api/get_seating_plan/${ID}`)
        .then(response => {
          console.log(response.data);
          this.seatingPlan = response.data;
        })
        .catch(error => {
          console.error('Error fetching movie information:', error);
        });
    },
    buyTickets() {
      console.log('Buying tickets for selected seats:', this.selectedSeats);
    },
  },
};
</script>

<style scoped>
  /* Fixes up the rows for the seating */
  .row {
    display: flex;
    margin-top: 5px;
  } 

  /* Showcase the theatre screen */
  .screen {
    margin-bottom: 10px;
    background-color: #fff;
    height: 50px;
    width: 37%;
  } 
  
  .header{
    text-align: center;
    color: white;
    font-size: 30px;
  }

  /* Creates the seat help tab */
  .seat_help_tab {
    justify-content: center;
    color: #f8f7f7;
    display: flex;
    margin: 20px 0; 
  }

  /* Curser won't be able to hover the options in the seat help tab */
  .seat_help_tab .seat:not(.occupied):hover {
    cursor: default;
    transform: scale(1);
  }
  
  /* Spaces out the seat help tab */
  .seat_help_tab li {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 20px;
  }
  
  /* Avaiable seats are default blue colour */
  .seat {
    background-color: #1f3681;
    height: 45px;
    width: 68px;
    margin: 2px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }
  
 /* Sold seat color is changed to gray */
  .seat.occupied {
    background-color: #666161;
  }
  
  /* This lets the user hover over the avaiable seats and not the occupied ones*/
  .seat:not(.occupied):hover {
    cursor: pointer;
    transform: scale(1.2);
  }
  
  .seat.selected {
    background-color: green;
  }
  .container {
    flex-direction: column; 
    height: 650px;
  }

  .selected-counter {
    text-align: center;
    margin-top: 10px;
  }

  .buy-button {
    margin-top: 10px;
    padding: 10px;
    background-color: #1f3681;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .buy-button:disabled {
    background-color: #666161;
    cursor: not-allowed;
  }
</style>
