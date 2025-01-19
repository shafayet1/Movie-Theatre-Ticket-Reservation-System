import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth} from 'firebase/auth';




const firebaseConfig = {
    apiKey: "AIzaSyAfNW3dB4AEArbAzYQbULlIVmtcPNJ5ESk",
    authDomain: "cps714-1b226.firebaseapp.com",
    projectId: "cps714-1b226",
    storageBucket: "cps714-1b226.appspot.com",
    messagingSenderId: "1097896905213",
    appId: "1:1097896905213:web:ecf61820e7093dafb63194",
    measurementId: "G-4PB8GS56SG"
  };

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app)

//export const auth = firebase.auth();