<template>
  <div class="home">
    <!-- <div class="feature-card">
      <router-link to="/movie/tt0126029">
        <img src="https://m.media-amazon.com/images/I/51D4tULTUEL._AC_UF894,1000_QL80_.jpg" alt="Shrek Poster" class="featured-img" />
        <div class="detail">
          <h3>Shrek</h3>
          <p>Comedy</p>
          <p>Shrek (Mike Myers) 
            goes on a quest to rescue the feisty Princess Fiona (Cameron Diaz)
             with the help of his loveable Donkey (Eddie Murphy) 
             and win back the deed to his swamp from scheming Lord Farquaad</p>
        </div>
      </router-link>
    </div> -->
    <!-- <form @submit.prevent="SearchMovies()" class="search-box">
      <input type="text" placeholder="What movie do you want to watch?" v-model="search" />
      <input type="submit" value="Search" />
    </form> -->

    <table>
      <tr>
        <th>Movie Poster</th>
        <th>Movie Name</th>
        <th>Duration (mins)</th>
        <th>Auditoriums</th>
        <th></th>
      </tr>
      <tr v-for="(movie, index) in movies" :key="index">
        <td>
          <img :src="movie.Image" alt="Movie Poster" width="100" height="150" />
        </td>
        <td>{{ movie.Name }}</td>
        <td>{{ movie.Duration_Mins }}</td>
        <td>{{ movie.Auditoriums }}</td>
        <td>
          <router-link :to="{ path: '/seats/' +  movie.Auditoriums}">
            <button>Book Now</button>
          </router-link>
        </td>
      </tr>
    </table>

      
  </div>
  
</template>

<script>
import axios from 'axios';

export default {
    name: 'SeatView',
    data(){
      return{
        movies:[]
          
        
      }
    },
    mounted() {
      this.getAllMovies();
    },
    methods: {

      getAllMovies() {
        axios.get(`http://127.0.0.1:5000/api/get_all_movie_info`, {
          headers:{
            'Access-Control-Allow-Origin': 'http://localhost:8080'
          }
        })
      .then(response => {
        if (response.data != null) {
          // Movie found, set the movieName
          this.movies = response.data
          console.log(response.data)
        } else {
            console.error('No movies found.');
          }
      })
      .catch(error => {
        console.error('Error fetching movie information:', error);
      });
  },

    },
}

</script>

<style lang="scss">
.home {
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;

    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }

    th {
      background-color: #42B883;
      color: #FFF;
    }

    td {
      img {
        width: 80px;
        height: 120px;
        object-fit: cover;
        border-radius: 8px;
      }

      button {
        background-color: #42B883;
        color: #FFF;
        padding: 10px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.4s;

        &:hover {
          background-color: #3B8070;
        }
      }
    }
  }
}
</style>
