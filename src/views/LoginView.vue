<template>
    <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login and Signup Form</title>
  </head>
  <body>
    <div class="container">
  <div class="card">
    <h2>Login Form</h2>
    <form>
      <label for="username">Email</label>
      <input type="text" id="email" placeholder="Enter your email" v-model="email">

      <label for="password">Password</label>
      <input type="password" id="password" placeholder="Enter your password" v-model="password">
        <!-- <p v-if="errMsg"> {{errMsg}} </p> -->
      <button type="button" class="btn btn-primary" @click="handleSignIn">Login</button>
      
    </form>
    <div class="switch">Don't have an account? <a @click="switchCard()">Register here</a></div>
    <p class="forgot-password text-right" >
    <router-link to="/forgot">Forgot your password? </router-link>
  </p>
  </div>

  <div class="card" style="display: none;">
    <h2>Register Form</h2>
    <form>
      <label for="fullname">Full Name</label>
      <input type="text" id="fullname" placeholder="Enter your full name">

      <label for="email">Email</label>
      <input type="email" id="new-email" placeholder="Enter your email" v-model="newemail">

      <label for="new-password">New Password</label>
      <input type="password" id="new-password" placeholder="Enter your new password" v-model="newpassword">
      <label for="reenter password">Reenter Password</label>
      <input type="password" id="reenter-password" placeholder="Reenter your password">
      <button type="button" @click="handleRegistration">Register</button>
    </form>
    <div class="switch">Already have an account? <a @click="switchCard()">Login here</a></div>
    <p class="forgot-password text-right" >
    <router-link to="/forgot">Forgot your password? </router-link>
  </p>
  </div>
</div>
  </body>
  </html>
</template>




<script setup>
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword , onAuthStateChanged , signOut } from "firebase/auth";
import {useRouter} from 'vue-router'
import {ref , onMounted } from 'vue'
import emailjs from '@emailjs/browser';

// const auth = getAuth();
const router = useRouter()
const email = ref('')
const password = ref('')
const newemail = ref('')
const newpassword = ref('')
const errMsg = ref()
const isLoggedIn = ref(false)
const auth = getAuth()
const handleSignIn = () => {
signInWithEmailAndPassword(auth, email.value, password.value)
  .then(() => {
    // Signed in 
    console.log("SUCCESS")

    router.push("/home")
  })
  .catch((error) => {
    console.log(error)
    switch (error.code) {
          case 'auth/invalid-email':
              errMsg.value = 'Invalid email'
              break
          case 'auth/user-not-found':
              errMsg.value = 'No account with that email was found'
              break
          case 'auth/wrong-password':
              errMsg.value = 'Incorrect password'
              break
          default:
              errMsg.value = 'Email or password was incorrect'
              break
    }
  });
  }
  const handleRegistration = () => {
  createUserWithEmailAndPassword(getAuth(), newemail.value, newpassword.value)
    .then((userCredential) => {
      const user = userCredential.user;
      emailjs.init("m_xCEuO4xIl8qxYD_")
    emailjs.send("service_esmj7bj","template_kmzosgr",{
      email: newemail.value,
    })
    .then((response) => {
      console.log('Email sent successfully:', response);
    })
    .catch((error) => {
      console.error('Error sending email:', error);
    });
      console.log("SUCCESS")
      console.log(user)
      router.push("/home")
      // Handle successful registration
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      // Handle registration error
      //add error message to appear 
    console.log(errorCode + errorMessage)
    });
};

const handleSignOut = () => {

}

function switchCard() {
    const loginCard = document.querySelector('.container .card:nth-child(1)');
    const registerCard = document.querySelector('.container .card:nth-child(2)');
    if (loginCard.style.display === 'none') {
      loginCard.style.display = 'block';
      registerCard.style.display = 'none';
    } else {
      loginCard.style.display = 'none';
      registerCard.style.display = 'block';
    }
  }

  onMounted(() => {
  onAuthStateChanged(auth, (user) => {
    if (user) {
      // User is signed in.
      console.log("User is signed in:", user);
      isLoggedIn.value = true;
    } else {
      // User is signed out.
      console.log("User is signed out");
      isLoggedIn.value = false;
    }
  });
});

</script>




<style>
    body {
      background-image: url(../imgs/login-background.jpg);
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .card {
      width: 300px;
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      text-align: center;
    }
    h2 {
      color: #007BFF;
      margin-bottom: 20px;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    label {
      text-align: left;
      margin-bottom: 5px;
    }
    input {
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }
    button {
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .switch {
      margin-top: 15px;
      font-size: 14px;
    }
    .switch a {
      color: #007BFF;
      text-decoration: none;
      cursor:pointer;
    }
</style>




