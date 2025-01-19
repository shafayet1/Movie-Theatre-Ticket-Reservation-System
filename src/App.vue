<template>
  <header>
    <ul >
  <li><router-link to="/home" v-if="isLoggedIn">Home</router-link></li>
  <li><router-link to="/">Sign In</router-link></li>
  <li><router-link to="/seats" v-if="isLoggedIn">Seats</router-link></li>
  <li><router-link to="/payment" v-if="isLoggedIn">Pay</router-link></li>
  <li><a href="about.asp">About</a></li>
  <li> <button @click="handleSignOut" v-if="isLoggedIn"> Sign Out</button></li>
  </ul>
   
  </header>
  <main>
    <router-view />
  </main>
  
</template>
<script setup>
import {useRouter} from 'vue-router'
import {onMounted, ref} from 'vue';
import {getAuth, onAuthStateChanged, signOut} from "firebase/auth"
const isLoggedIn = ref(false)
const router = useRouter()
let auth;
onMounted(() =>{
auth = getAuth()
onAuthStateChanged(auth, (user) =>{
  if(user){
    isLoggedIn.value = true;
  }else{
    isLoggedIn.value = false;
  }
})
})

const handleSignOut = ()=>{
  signOut(auth).then(() =>{
    router.push("/")
  })

}
</script>
<style lang="scss">
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
}

</style>

