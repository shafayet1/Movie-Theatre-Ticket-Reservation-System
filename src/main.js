
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

createApp(App).use(router).mount("#app");

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyAfNW3dB4AEArbAzYQbULlIVmtcPNJ5ESk",
    authDomain: "cps714-1b226.firebaseapp.com",
    projectId: "cps714-1b226",
    storageBucket: "cps714-1b226.appspot.com",
    messagingSenderId: "1097896905213",
    appId: "1:1097896905213:web:ecf61820e7093dafb63194",
    measurementId: "G-4PB8GS56SG"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };

