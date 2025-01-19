import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import SeatView from '../views/SeatView.vue'
import PaymentView from '../views/PaymentView.vue'
import ForgotView from '../views/ForgotView.vue'
import RecieptView from '../views/RecieptView.vue'
import {getAuth, onAuthStateChanged} from "firebase/auth"
import {auth} from '../firebase'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    meta:{
      requiresAuth: true,
    }
  },
  {
    path: '/movie/:id',
    name: 'Movie Detail',
    component : MovieDetail
  },
  {
    path: '/seats/:auditorium',
    name: 'Seat Selection',
    component: SeatView
  },
 {
  path: '/payment/:auditoriumId/:seatIds',
  component: PaymentView,
  props: true,
},
{
  path: '/forgot',
  name: 'Forgot',
  component: ForgotView
},
{
  path: '/reciept',
  name: 'Reciept',
  component: RecieptView
}
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
// const getCurrentUser = () => {
//   return new Promise((resolve, reject) =>{
//     const removeListener = onAuthStateChanged(
//       getAuth(),
//       (user) => {
//         removeListener();
//         resolve(user);
//       },
//       reject
//     )
//   })
// }
// router.beforeEach(async (to, from, next) =>{
//   if(to.matched.some((record) => record.meta.requiresAuth)){
//     if( getAuth().currentUser){
//       return next();
//     }else{
//       alert("you don't have access")
//        next("/")
//     }
//    next()
//   }
// });


export default router
