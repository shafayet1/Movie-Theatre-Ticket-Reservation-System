<template> 
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <div class="card1">
          <h3>Forgot Password</h3>
          <form>
              <label>Email</label>
              <input v-model="email" type="email" placeholder="Enter your email">
              <button class="btn btn-primary btn-block" @click="handleSendResetEmail">Send</button> 
          </form>
  
      </div>
  
  
  </template>
  
  
  <script> 
  import { sendPasswordResetEmail } from "firebase/auth";
  //import { auth } from "../firebase";
  import { auth } from "@/firebase";
  import { ref } from 'vue';

  export default {
    name: 'ForgotView',
    setup() {
      const email = ref('');
      console.log(auth)
      const handleSendResetEmail = () => {
        sendPasswordResetEmail(auth, email.value)
          .then(() => {
            console.log("Password reset email sent!");
          })
          .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error(errorCode, errorMessage);
          });
      };

      return {
        email,
        handleSendResetEmail,
      };
    },
  };
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
    .card1 {
      width: 300px;
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
      text-align: center;
      margin: auto;
      width: 20%;
      border: 3px solid rgb(250, 250, 250);
      padding: 10px;
   
    }
    h3 {
      color: #007BFF;
      margin-bottom: 35px;
      align-items: center;
      margin-top: auto;
    
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
  
  </style>